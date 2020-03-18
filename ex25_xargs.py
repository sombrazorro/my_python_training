import sys
import subprocess
import argparse
import re
parser = argparse.ArgumentParser(prog='ex25_xargs.py')
parser.add_argument("inputs", metavar='f', nargs=argparse.REMAINDER,
            help="input files manipulated by the command")
parser.add_argument('-n',
            metavar='max-args',
            type=int, 
            help='Use at most max-args arguments per comman            d line'
            )
#cmd = " ".join(sys.argv[1:])
#cmd = sys.argv[1:]

#print(sys.argv)
print(parser.parse_args())
args = parser.parse_args()
cmd = args.inputs
#print(cmd)
#print(sys.stdin)
#print(sys.stdin)
#sys.exit(0)
if cmd == []:
    cmd = ["echo"]
else:
    pass
print(cmd)
if args.n:
   # print(args.n)
    steps = args.n
   # print(type(steps))
   # print(sys.stdin.readlines())
    #std_lines = [x for x in sys.stdin.readlines()]
    # From the manual:  xargs reads items from the standard input, delimited by blanks  
    std_lines = [x for x in re.split('\s|\n',sys.stdin.read()) if x != ""]
    
    print(std_lines)
    for i in range(0, len(std_lines), steps):
        exe = cmd + std_lines[i:i+steps]
        print(exe)
        status = subprocess.run(exe)
else:
   
    print(sys.stdin)

    for line in sys.stdin:
        print(line)
        exe = cmd + [line.strip()]
        print(exe)
        status = subprocess.run(exe)
       # print(cmd)

