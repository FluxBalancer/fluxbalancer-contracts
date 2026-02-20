import os

os.system("""
python -m grpc_tools.protoc \
  -I metrics \
  --python_out=metrics \
  --grpc_python_out=metrics \
  ./metrics/metrics.proto
""")