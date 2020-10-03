import os
import grpc

from grpc_hub.router import serve

GRPC_PORT = os.environ["GRPC_PORT"]


def run():
    channel = grpc.insecure_channel(f"localhost:{GRPC_PORT}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    serve()
