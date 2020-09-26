from grpc_hub import user_pb2
from grpc_hub import user_pb2_grpc


class UserService(user_pb2_grpc.UserServiceServicer):

    def SignUp(self, request, context):
        response = user_pb2.LoginResponse(
            token="dummy_token",
            user=user_pb2.User(
                id=1,
                name=request.name,
                email=request.email,
                username=request.username
            )
        )
        return response

    def Login(self, request, context):
        response = user_pb2.LoginResponse(
            token="dummy_token",
            user=user_pb2.User(
                id=1,
                name="Dummy Name",
                email=request.email,
                username="dummy"
            )
        )
        return response

    def GetUser(self, request, context):
        response = user_pb2.User(
            id=request.id,
            name="Dummy Name",
            email="dummy@example.com",
            username="dummy"
        )
        return response

