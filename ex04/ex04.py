import sys
cmds = sys.argv
print(cmds)
if len(cmds) <= 1:
    print("Wrong command syntax. Please see the help.")
else:
    print(cmds)

if sys.argv[1] in ("-h", "--help"):
    print("Usage: {0} -abc -o1 arg1 -o2 arg2 -o3 -arg3 input").format(sys.argv[0])
elif len(cmds) < 5:
    print("There should be at least four arguments")
