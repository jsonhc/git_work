#!/usr/bin/python3
def subprocess_fun(CMD):
    import subprocess
    child = subprocess.Popen(CMD,stdout=subprocess.PIPE)
    out,err = child.communicate()
    result = out.decode('utf-8')
    return result

L = []
import sys
L.append(sys.argv[1])
arg2 = sys.argv[2]
L.append(arg2)

if __name__ == "__main__":
    print(subprocess_fun(L))
