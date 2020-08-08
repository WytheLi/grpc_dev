# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import hello_world_pb2 as hello__world__pb2


class HelloWorldStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.show_msg = channel.unary_unary(
                '/test.HelloWorld/show_msg',
                request_serializer=hello__world__pb2.HelloGrpcReq.SerializeToString,
                response_deserializer=hello__world__pb2.HelloGrpcReply.FromString,
                )


class HelloWorldServicer(object):
    """Missing associated documentation comment in .proto file."""

    def show_msg(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HelloWorldServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'show_msg': grpc.unary_unary_rpc_method_handler(
                    servicer.show_msg,
                    request_deserializer=hello__world__pb2.HelloGrpcReq.FromString,
                    response_serializer=hello__world__pb2.HelloGrpcReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'test.HelloWorld', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HelloWorld(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def show_msg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/test.HelloWorld/show_msg',
            hello__world__pb2.HelloGrpcReq.SerializeToString,
            hello__world__pb2.HelloGrpcReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
