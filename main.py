import grpc

from grpc_hub.router import serve


def run():
    channel = grpc.insecure_channel("localhost:50051")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    serve()
