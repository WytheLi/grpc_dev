#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
import grpc
import hello_world_pb2 as pb2
import hello_world_pb2_grpc as pb2_grpc


def run():
    conn = grpc.insecure_channel('localhost:50051')
    client = pb2_grpc.HelloWorldStub(channel=conn)
    # response = client.show_msg(pb2.HelloGrpcReq(
    #     name='willi',
    #     age=23
    # ))
    # print(response.result)
    response = client.send_stream(pb2.SendStreamReq(
        data='item1'
    ))
    for item in response:
        print(item.result)


if __name__ == '__main__':
    run()
