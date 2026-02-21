import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROTO_DIR = ROOT / "src" / "contracts" / "metrics"
PROTO = PROTO_DIR / "metrics.proto"

subprocess.check_call(
    [
        "python",
        "-m",
        "grpc_tools.protoc",
        f"-I{PROTO_DIR}",
        f"--python_out={PROTO_DIR}",
        f"--grpc_python_out={PROTO_DIR}",
        str(PROTO),
    ]
)
