import argparse
import fnmatch
import os
import subprocess
import sys
from pathlib import Path
#import glob

parser = argparse.ArgumentParser(prog='ex06.py')
parser.add_argument("dir", metavar='directory',
                    help="input directory to be manipulated")
parser.add_argument('-name', metavar='NAME string',
                    help='patterns to be satisfied')
parser.add_argument('-type', metavar='NAME string',
                    help='type patterns to be satisfied')
parser.add_argument('-exec', metavar='COMM string',
                    help='command to be applied on the found files')
args = parser.parse_args()
print(args)
#print(args.name)
start_path = args.dir
#print(start_path)
#print(Path().rglob(args.name))

def pattern_search(path, name, type_name=None):
    if type_name is None:
        return Path(path).rglob(name)
           # yield f
    elif type_name == "f":

        return  [f for f in Path(path).rglob(name) if f.is_file()]
             #   print(f)
    elif type_name == "d":
        return  [f for f in Path(path).rglob(name) if f.is_dir()]
    #    for f in Path(path).rglob(name):
    #        if f.is_dir():
    #            print(f)
    else:
        print("Some errors.")
        sys.exit(1)
   # return None

#def type_search(path, type_name):
#    for f in Path(path).rglob(type_name):
#        print f

if args.exec:
   # print(pattern_search(start_path, args.name, args.type))

    if "rm" in args.exec:
        print("Do not use rm in this script")
        sys.exit(0)
    else:
        for f in pattern_search(start_path, args.name, args.type):
            cmd =  args.exec.split() + [str(f)]
        #    print(cmd)
            subprocess.run(cmd)


elif args.type:
    for f in pattern_search(start_path, args.name, args.type):
        print(f)

elif args.name:
    for f in pattern_search(start_path, args.name):
        print(f)

#
#for f in item_list:
#    if fnmatch.fnmatch(f, args.name):
# #       print(glob.glob(f))
#        if args.exec:
#            #print(args.exec.split())
#            #pass
#            #subprocess.run(args.exec.split().append(f))
#            print(f)
#            cmd =  args.exec.split() + [f]
#            print(cmd)
#            subprocess.run(cmd)
#        else:
#            print(f)
#
