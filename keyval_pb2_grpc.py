# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import keyval_pb2 as keyval__pb2


class KeyValueStub(object):
    """The protocol description for a simple remote key-value store with
    basic read/write/delete/list operations.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Read = channel.unary_unary(
                '/keyval.KeyValue/Read',
                request_serializer=keyval__pb2.ReadRequest.SerializeToString,
                response_deserializer=keyval__pb2.ReadResponse.FromString,
                )
        self.Write = channel.unary_unary(
                '/keyval.KeyValue/Write',
                request_serializer=keyval__pb2.WriteRequest.SerializeToString,
                response_deserializer=keyval__pb2.WriteResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/keyval.KeyValue/Delete',
                request_serializer=keyval__pb2.DeleteRequest.SerializeToString,
                response_deserializer=keyval__pb2.DeleteResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/keyval.KeyValue/List',
                request_serializer=keyval__pb2.ListRequest.SerializeToString,
                response_deserializer=keyval__pb2.ListResponse.FromString,
                )


class KeyValueServicer(object):
    """The protocol description for a simple remote key-value store with
    basic read/write/delete/list operations.
    """

    def Read(self, request, context):
        """Read the value of the given key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request, context):
        """Write the given value for the given key under certain conditions
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete the given key if the key exists.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """List all the keys, values and versions in the key value store
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KeyValueServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=keyval__pb2.ReadRequest.FromString,
                    response_serializer=keyval__pb2.ReadResponse.SerializeToString,
            ),
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=keyval__pb2.WriteRequest.FromString,
                    response_serializer=keyval__pb2.WriteResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=keyval__pb2.DeleteRequest.FromString,
                    response_serializer=keyval__pb2.DeleteResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=keyval__pb2.ListRequest.FromString,
                    response_serializer=keyval__pb2.ListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'keyval.KeyValue', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class KeyValue(object):
    """The protocol description for a simple remote key-value store with
    basic read/write/delete/list operations.
    """

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/keyval.KeyValue/Read',
            keyval__pb2.ReadRequest.SerializeToString,
            keyval__pb2.ReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/keyval.KeyValue/Write',
            keyval__pb2.WriteRequest.SerializeToString,
            keyval__pb2.WriteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/keyval.KeyValue/Delete',
            keyval__pb2.DeleteRequest.SerializeToString,
            keyval__pb2.DeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/keyval.KeyValue/List',
            keyval__pb2.ListRequest.SerializeToString,
            keyval__pb2.ListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
