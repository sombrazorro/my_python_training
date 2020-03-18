import argparse
import sys


def prog_args():
    parser = argparse.ArgumentParser(prog="ex08_cut.py")
    parser.add_argument("-d", type=str, metavar="delimiter")
    parser.add_argument("-f", type=str, metavar="column")
    parser.add_argument("input", nargs='*', default=sys.stdin)
    return parser.parse_args()

def cut(word, delimiter, col):
    splitted = word.split(delimiter)
    if col <= len(splitted):
        return splitted[col-1]
    else:
        return None
     

args = prog_args()
#print(args.input)
#print(args.f)
cols = [int(s) for s in args.f.split(',')]
#print(cols)
#for f in args.input:
if sys.stdin.isatty():
    reader = open(args.input)
    words = reader.readlines()
    words = [x.replace("\n", "") for x in words]
   # print(cols)
    for w in words:
        results = [cut(w, args.d, n) for n in cols]
        print(*results)
    reader.close()
else:
    input_list = [x.replace("\n", "") for x in sys.stdin.readlines()]
    for line in input_list:
        results = [cut(line, args.d, n) for n in cols]
        results = [x for x in results if x is not None]
        print(*results)
        #print(cut(line, args.d, 3))
      #  print(line.split(args.d))
#print(results)
#for s in results:
#    print(s)

        
