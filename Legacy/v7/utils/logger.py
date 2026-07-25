from pathlib import Path

LOG=Path("dashboard.log")

def log(message):
    from .helpers import timestamp
    LOG.open("a",encoding="utf-8").write(f"[{timestamp()}] {message}\n")
