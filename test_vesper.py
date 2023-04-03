import subprocess
import sys

"""
Integration test for vesper.py

Run with `pytest`
"""


def test_to_many_arguments():
    # Don't just silently ignore unknown arguments
    proc = subprocess.run([sys.executable, "vesper.py", "--wrong"], capture_output=True)
    assert proc.stderr.find(b"error: unrecognized arguments") != -1
    assert proc.returncode == 2

    proc2 = subprocess.run([sys.executable, "vesper.py", "192.168.10.1"], capture_output=True)
    assert proc2.stderr.find(b"error: unrecognized arguments") != -1
    assert proc2.returncode == 2

