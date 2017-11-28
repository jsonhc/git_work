#!/usr/bin/python3

import subprocess

CMD1=["ls","-l"]
cmd_result = subprocess.Popen(CMD1,shell=False,stdout=subprocess.PIPE)
out,err = cmd_result.communicate()
print("parent")
print(out.decode('utf-8'))

CMD2 = ["free","-m"]
cmd_result2 = subprocess.Popen(CMD2,shell=True,stdout=subprocess.PIPE)
out,err = cmd_result2.communicate()
print(out.decode('utf-8'))
