import logging
import os

from concurrent import futures
import grpc

from grpc_hub import user_pb2_grpc
from .user_service import UserService

logger = logging.getLogger(__file__)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    logger.info("GRPC: Adding UserService....")
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    logger.info("GRPC: UserService added")
    grpc_port = os.environ["GRPC_PORT"]
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
