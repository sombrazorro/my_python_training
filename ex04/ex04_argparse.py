import argparse

parser = argparse.ArgumentParser(prog='ex04_argparse.py')
parser.add_argument("inputs", metavar='f',
                    help="input files manipulated by the command")
parser.add_argument('-a', help='argument "a" of %(prog)s', action="store_true")
parser.add_argument('-b', help='argument "b" of %(prog)s', action="store_true")
parser.add_argument('-c', help='argument "c" of %(prog)s', action="store_true")
parser.add_argument('-o1', help='argument "o1" of %(prog)s')
parser.add_argument('-o2', help='argument "o2" of %(prog)s')
parser.add_argument('-o3', help='argument "o3" of %(prog)s')
parser.print_help()
args = parser.parse_args()
if args.a:
    print("Argument 'a' turned on")
if args.b:
    print("Argument 'b' turned on")
if args.c:
    print("Argument 'c' turned on")
print(args)
