from grpc_hub import user_pb2
from grpc_hub import user_pb2_grpc
from service import user_service
from db.models.user import User


class UserService(user_pb2_grpc.UserServiceServicer):
    def SignUp(self, request, context):
        user_obj = User(
            email=request.email,
            username=request.username,
            name=request.name,
            password=request.password
        )
        resp = user_service.signup(user_obj=user_obj)
        response = user_pb2.LoginResponse(
            token="dummy_token",
            user=user_pb2.User(
                id=resp["user"].id,
                name=resp["user"].name,
                email=resp["user"].email,
                username=resp["user"].username
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
