#!/usr/bin/python3
import subprocess

CMD1 = ["free","-m"]
CMD2 = ["awk","/^Mem/"]
CMD3 = ["awk","{print $2}"]
child1 = subprocess.Popen(CMD1,stdout=subprocess.PIPE)
child2 = subprocess.Popen(CMD2,stdin=child1.stdout,stdout=subprocess.PIPE)
child3 = subprocess.Popen(CMD3,stdin=child2.stdout,stdout=subprocess.PIPE)

out,err = child3.communicate()
mem_used = out.decode('utf-8')
print("mem_used is %s" % mem_used)
