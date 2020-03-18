import ex26_hexdump
import subprocess


def test_hex():
    exe = ["echo"]
    subprocess.run(exe)

def test_one_byte_oct():
    pass

def test_reshape():
    even = [1,2,3,4,5,6,7,8]
    assert ex26_hexdump.reshape(even, 2) == [[1,2],[3,4],[5,6],[7,8]]
    assert ex26_hexdump.reshape(even, 5) == [[1,2,3,4,5],[6,7,8]]
