#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
import logging
import time
from concurrent import futures

import grpc
import hello_world_pb2 as pb2
import hello_world_pb2_grpc as pb2_grpc


def _abort(code, detail):
    def terminate(ignored_request, context):
        context.abort(code, detail)
    return grpc.unary_unary_rpc_method_handler(terminate)


# 拦截器
class SingleInterceptor(grpc.ServerInterceptor):
    def __init__(self, key, value, code, detail):
        self.key = key
        self.value = value
        self._abort = _abort(code, detail)

    def intercept_service(self, continuation, handler_call_details):
        """

        Args:
            continuation: 函数执行器
            handler_call_details:  metadata

        Returns:

        """
        headers = dict(handler_call_details.invocation_metadata)
        # if (self.key, self.value) not in handler_call_details.invocation_metadata:
        if headers.get(self.key) != self.value:
            return self._abort
        return continuation(handler_call_details)


class HelloWorld(pb2_grpc.HelloWorldServicer):
    def show_msg(self, request, context):
        name = request.name
        age = request.age

        if not all([name, age]):
            context.set_code(grpc.StatusCode.CANCELLED)
            context.set_details('缺少必要参数！')
            raise context

        headers = context.invocation_metadata()
        print(headers[0].key, headers[0].value)
        context.set_trailing_metadata((('key1', 'value1'), ('key2', 'value2')))

        context.set_compression(grpc.Compression.Gzip)  # 给单个响应设置压缩

        result = 'My name is %s, i am %s years old!' % (name, age)
        return pb2.HelloGrpcReply(result=result)

    def send_stream(self, request, context):
        index = 0
        while context.is_active():
            data = request.data

            if data == 'close':
                print('data is close, request will cancel')
                context.cancel()    # 服务器关闭连接

            time.sleep(1)
            index += 1
            yield pb2.SendStreamReply(result='send %d %s' % (index, data))

    def recv_stream(self, request_iterator, context):
        for request in request_iterator:
            data = request.data
            print(data)
            return pb2.RecvStreamReply(result='ok')

    def double_stream(self, request_iterator, context):
        for request in request_iterator:
            data = request.data
            print('service recv data: %s' % data)
            yield pb2.DoubleStreamReply(result=data)


def run():
    # 实例化拦截器
    validator = SingleInterceptor('name', 'root', grpc.StatusCode.UNAUTHENTICATED, 'Access denined')
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        # compression=grpc.Compression.Gzip,   # 全局设置响应压缩
        interceptors=(validator, ),
        options=[   # 传输最大值的设置
            ('grpc.max_send_message_length', 50 * 1024 * 1024),
            ('grpc.max_receive_message_length', 50 * 1024 * 1024)
        ]
    )
    pb2_grpc.add_HelloWorldServicer_to_server(HelloWorld(), grpc_server)
    grpc_server.add_insecure_port('[::]:50051')
    grpc_server.start()
    grpc_server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    run()