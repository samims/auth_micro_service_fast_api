### To generate source code from `.proto` file
```bash
 python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. user.proto
```

### change import statement on *_pb2_grpc.py 
```python
from . import user_pb2 as user__pb2
```
