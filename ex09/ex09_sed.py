import argparse
import sys
from pathlib import Path
import re

def prog_args():
    parser = argparse.ArgumentParser(prog="ex09_sed.py")
   # parser.add_argument("-d", type=str, metavar="delimiter")
   # parser.add_argument("-f", type=str, metavar="column")
    parser.add_argument("command", type=str)
#    parser.add_argument("input", nargs='?', default=sys.stdin)
    parser.add_argument("input", nargs='*', default=sys.stdin)

    return parser.parse_args()


def sed_insert(lt, word, n=None):
    if isinstance(n, int):
        lt.insert(n-1, word+'\n')
        return lt
    else:
        result = []
        for e in lt:
            result.append(word+'\n')
            result.append(e)
        return result

    
def sed_replace(lt, word, n=None):
    if isinstance(n, int):
        lt.pop(n-1)
        lt.insert(n-1, word+'\n')
        return lt
    else:
        result = [word+'\n' for e in lt]
        return result

    
def sed_append(lt, word, n=None):
    if n is not None:
        lt.insert(n, word+'\n')
        return lt
    else:
        result = []
        for e in lt:
            result.append(e)
            result.append(word+'\n')
        return result


def sed_append(lt, word, n=None):
    if n is not None:
        lt.insert(n, word+'\n')
        return lt
    else:
        result = []
        for e in lt:
            result.append(e)
            result.append(word+'\n')
        return result

def sed_substitude(lt, old_word, new_word):
    p = re.compile((old_word))
    result = []
    for e in lt:
        result.append(p.sub(new_word, e))

    return result

        
args = prog_args()
cmd = args.command
# print(args.input)


# Read from files or the stdin
input_list = []
if sys.stdin.isatty():
    input_files = args.input
    for f in input_files:
        reader = open(str(f))
        input_list = input_list + reader.readlines()
        reader.close()
else:
    input_list = args.input.readlines()

# print(input_list)




# insert: i\ text
if 'i\\' in cmd:
    splitted = cmd.split('i\\')
    splitted = list(filter(None, splitted)) #  Remove empty string.
                                            #  This way is faster.

    if len(splitted) == 2:
        try:
            n = int(splitted[0])
            final = sed_insert(input_list, splitted[1], n)
            print(*final)

        except ValueError:
            print("Oops!  That was no valid number.")
    elif len(splitted) == 1:
        final = sed_insert(input_list, splitted[0])
        print(*final)

    else:
        print("Something wrong!")
        sys.exit(1)

# append: a\ text
elif 'a\\' in cmd:
    splitted = cmd.split('a\\')
    print(splitted)
    splitted = list(filter(None, splitted)) 

    if len(splitted) == 2:
        try:
            n = int(splitted[0])
            final = sed_append(input_list, splitted[1], n)
            print(*final, end="")

        except ValueError:
            print("Oops!  That was no valid number.")
    elif len(splitted) == 1:
        final = sed_append(input_list, splitted[0])
        print(*final, end="")

    else:
        print("Something wrong!")
        sys.exit(1)

# change: c\ text
elif 'c\\' in cmd:
    splitted = cmd.split('c\\')
    splitted = list(filter(None, splitted)) 

    if len(splitted) == 2:
        try:
            n = int(splitted[0])
            final = sed_replace(input_list, splitted[1], n)
           # print(*final, end="")
            for f in final:
                print(f, end="")
        except ValueError:
            print("Oops!  That was no valid number.")
    elif len(splitted) == 1:
        final = sed_replace(input_list, splitted[0])
        print(*final)
        

    else:
        print("Something wrong!")
        sys.exit(1)


# s///g
elif 's/' in cmd:
    if '/g' in cmd:
#        oldword = cmd.split("/")[1]
#        newword = cmd.split("/")[2]
        oldword, newword = cmd.split("/")[1:3]     
        final = sed_substitude(input_list, oldword, newword)
       # print(*final)
        for s in final:
            print(s, end="")
    else:
        print("command may be wrong.")

else:
    pass
