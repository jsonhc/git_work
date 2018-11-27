# install psutil module
# sudo apt install python-pip
# pip install psutil

# sudo apt-get update
# sudo apt install python3-pip
# pip3 install psutil


# import psutil
# mem = psutil.virtual_memory()
# print(mem)
# print(mem.used/1024/1024/1024)
# print(mem.total/1024/1024/1024)
# mem_rate = int(float(mem.used/mem.total)*100)
# print("%s%%" % mem_rate)   # 打印内存使用率百分号
#
# cpu_count = psutil.cpu_count()
# print(cpu_count)   # 获取cpu的逻辑核数
# print(psutil.cpu_count(logical=False))   # 获取cpu的物理核数
#
# p = psutil.Process(13606)
# print(p.memory_percent())   # 获取该pid消耗的内存使用率
# print(p.num_threads())  # 获取该进程开启的线程数
# print(p.cpu_times())  # 进程cpu的时间信息 pcputimes(user=0.0, system=0.0, children_user=0.77, children_system=0.27)


import psutil, sys, subprocess


def get_process_memory(cmd):
    print(cmd)
    result = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = result.communicate()
    print(stdout)
    pid = int(stdout.decode('utf8'))
    p = psutil.Process(pid)
    return p.memory_percent()


process_name = sys.argv[1]
# print(process_name)
cmd = ("ps -ef|grep %s|grep -v grep|awk '{print $2}'|head -1" % process_name)
if __name__ == '__main__':
    print(get_process_memory(cmd))
