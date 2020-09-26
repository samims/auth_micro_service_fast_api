import logging

from concurrent import futures
import grpc

from grpc_hub import user_pb2_grpc
from .user_service import UserService


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
