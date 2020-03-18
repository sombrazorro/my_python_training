import argparse
from pathlib import Path
import re

parser = argparse.ArgumentParser(prog="ex07.py")
parser.add_argument("word", metavar="Pattern")
parser.add_argument("input", metavar="input_in_string")
args = parser.parse_args()

print(args)
print(args.input)
p = Path(args.input).expanduser()  # To handle the occurence of ~
print(Path(p.parent))
print(Path(p.name))
p_name = p.name

input_files = p.parent.rglob(p_name)

for files in input_files:
    reader = open(str(files))
    words = reader.readlines()
    print(words)
    for w in words:
        result = re.search(args.word, w)

        if result:
            print(str(files), w.strip("\n"))
        else:
            pass
    reader.close()
