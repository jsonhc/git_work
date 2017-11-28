#!/usr/bin/python3
import subprocess

CMD1 = ["free","-m"]
CMD2 = "awk '/^Mem/{print $2}'"
child1 = subprocess.Popen(CMD1,stdout=subprocess.PIPE)
child2 = subprocess.Popen(CMD2,shell=True,stdin=child1.stdout,stdout=subprocess.PIPE)

out,err = child2.communicate()
mem_used = out.decode('utf-8')
print("mem_used is %s" % mem_used)
