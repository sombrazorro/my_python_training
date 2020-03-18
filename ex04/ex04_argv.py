import sys
cmds = sys.argv
print(cmds)
print(sys.argv[0])
allargs = ["-a", "-b", "c"
           "-o1", "-o2", "-o3"]
opt = {"-o1": "arg1", "-o2": "arg2", "-o3": "arg3"}
if (set(cmds) - set(allargs)) == set():
    print("Input files needed!")
    sys.exit(2)

if len(cmds) <= 1:
    print("Please see the help.")
    sys.exit(0)

elif sys.argv[1] in ("-h", "--help"):
    print(("Usage: {} -abc -o1 arg1 -o2 arg2"
           "-o3 -arg3 inputs").format(cmds[0]))
else:
    pass

for f in ["-a", "-b", "-c"]:
    if f in cmds:
        print("Flag 'a' on")

for o in opt:
    if (o in cmds) and (opt[o] in cmds):
        print("{} on".format(opt[o]))
        continue
    elif (o in cmds) and (opt[o] not in cmds):
        print("{} needed!".format(opt[o]))
        sys.exit(2)
    else:
        pass
