import argparse
import sys


parser = argparse.ArgumentParser(prog="ex11_uniq.py")
parser.add_argument("files", nargs='*', help="inuput files", default=sys.stdin)

args = parser.parse_args()

input_list = []
if sys.stdin.isatty():
    input_files = args.input
    for f in input_files:
        reader = open(str(f))
        input_list = input_list + reader.readlines()
        reader.close()
else:
    input_list = args.files.readlines()

input_list = [x.replace("\n", "") for x in input_list]

out_list = []
i = 0
m = len(input_list)
while i < (m - 1):
    if input_list[i+1] == input_list[i]:
        if i < (m - 2):
            pass
        else:
            out_list.append(input_list[i])
        #    break

    else:
        out_list.append(input_list[i])
        if i < (m-2):
            pass
        else:
            # out_list.append(input_list[i])
            out_list.append(input_list[i+1])
        #    break
    i = i + 1

for s in out_list:
    print(s)
