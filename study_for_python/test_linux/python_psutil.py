# __author__ = 'Administrator'
# pip install psutil
# You should consider upgrading via the 'pip install --upgrade pip' command.
# pip install --upgrade pip
# error: command 'gcc' failed with exit status 1
# yum install python2-devel
# pip install psutil
import psutil, sys, subprocess


def get_process_memory(cmd):
    result = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = result.communicate()
    pid = int(stdout.decode('utf8'))
    print(pid)
    p = psutil.Process(pid)
    return p.memory_percent()


process_name = sys.argv[1]
# print(process_name)
cmd = "ps -ef|grep %s|grep -v grep|awk '{print $2}'|head -1" % process_name
if __name__ == '__main__':
    print(get_process_memory(cmd))

