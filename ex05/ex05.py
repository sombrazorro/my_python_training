import argparse
import sys

parser = argparse.ArgumentParser(prog='ex05.py')
parser.add_argument('infile', nargs='*', type=argparse.FileType('r'),
                    default=sys.stdin)
parser.add_argument('-o', help='output files')

args = parser.parse_args()
print(args)
print(type(args))
if args.o:
    print('output')
    print(args.o)
    writer = open(args.o, 'w')
    for f in args.infile:
        writer.write(f.read())
        f.close()
    writer.close()

else:
    for f in args.infile:
   # ipt = open(f, 'r')
        print(f.read())
        f.close()
