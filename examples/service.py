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
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )
    pb2_grpc.add_HelloWorldServicer_to_server(HelloWorld(), grpc_server)
    grpc_server.add_insecure_port('[::]:50051')
    grpc_server.start()
    grpc_server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    run()