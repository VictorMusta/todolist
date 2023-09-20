# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Task_pb2 as Task__pb2


class TaskServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createTask = channel.unary_unary(
            "/TaskService/createTask",
            request_serializer=Task__pb2.TaskRequest.SerializeToString,
            response_deserializer=Task__pb2.TaskResponse.FromString,
        )
        self.getTasks = channel.unary_unary(
            "/TaskService/getTasks",
            request_serializer=Task__pb2.ListRequest.SerializeToString,
            response_deserializer=Task__pb2.TaskListResponse.FromString,
        )
        self.modifyTask = channel.unary_unary(
            "/TaskService/modifyTask",
            request_serializer=Task__pb2.TaskRequest.SerializeToString,
            response_deserializer=Task__pb2.TaskResponse.FromString,
        )


class TaskServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def createTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def getTasks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def modifyTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_TaskServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "createTask": grpc.unary_unary_rpc_method_handler(
            servicer.createTask,
            request_deserializer=Task__pb2.TaskRequest.FromString,
            response_serializer=Task__pb2.TaskResponse.SerializeToString,
        ),
        "getTasks": grpc.unary_unary_rpc_method_handler(
            servicer.getTasks,
            request_deserializer=Task__pb2.ListRequest.FromString,
            response_serializer=Task__pb2.TaskListResponse.SerializeToString,
        ),
        "modifyTask": grpc.unary_unary_rpc_method_handler(
            servicer.modifyTask,
            request_deserializer=Task__pb2.TaskRequest.FromString,
            response_serializer=Task__pb2.TaskResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "TaskService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class TaskService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def createTask(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/TaskService/createTask",
            Task__pb2.TaskRequest.SerializeToString,
            Task__pb2.TaskResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def getTasks(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/TaskService/getTasks",
            Task__pb2.ListRequest.SerializeToString,
            Task__pb2.TaskListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def modifyTask(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/TaskService/modifyTask",
            Task__pb2.TaskRequest.SerializeToString,
            Task__pb2.TaskResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
