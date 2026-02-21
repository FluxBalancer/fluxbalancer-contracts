import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT / "src"
PROTO = SRC_DIR / "contracts" / "metrics" / "metrics.proto"

subprocess.check_call(
    [
        "python",
        "-m",
        "grpc_tools.protoc",
        f"-I{SRC_DIR}",
        f"--python_out={SRC_DIR}",
        f"--grpc_python_out={SRC_DIR}",
        str(PROTO),
    ]
)
