#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
import random
import time

import grpc
import hello_world_pb2 as pb2
import hello_world_pb2_grpc as pb2_grpc


def func():
    for j in range(10):
        time.sleep(1)
        data = str(random.random())
        yield pb2.RecvStreamReq(data=data)
    # while 1:
    #     time.sleep(1)
    #     data = str(random.random())
    #     yield pb2.RecvStreamReq(data=data)


def run():
    conn = grpc.insecure_channel('localhost:50051')
    client = pb2_grpc.HelloWorldStub(channel=conn)
    try:
        response, call = client.show_msg.with_call(pb2.HelloGrpcReq(
            name='willi',
            age=23
        ), metadata=(('name', 'root'),),
        compression=grpc.Compression.Gzip)
        print(response.result)

        headers = call.trailing_metadata()
        print(headers[0].key, headers[0].value)
    except Exception as e:
        print(dir(e))
        if 'code' in dir(e) and 'details' in dir(e):
            print(e.code(), e.details())

    # response = client.send_stream(pb2.SendStreamReq(
    #     data='item1'
    # ))
    # for item in response:
    #     print(item.result)

    # response = client.recv_stream(func())
    # print(response.result)

    # response = client.double_stream(func(), timeout=3)
    # for res in response:
    #     print('service send data: %s' % res.result)


if __name__ == '__main__':
    run()
