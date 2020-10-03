from pathlib import Path

import grpc

from grpc_hub.router import serve
from dotenv import load_dotenv


def run():
    channel = grpc.insecure_channel("localhost:50051")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    serve()
