# Author: wadeson
# date: 2017/12/3

import os

print(os.getcwd())  # 打印当前路径，类似于linux下面的pwd
os.chdir(r"D:\study\new_test\study_for_python")   # 改变到指定目录，类似cd
# print(os.getcwd())
#
# print(os.curdir)   # 返回.,代表当前路径
# print(os.pardir)   # 返回..，代表上一级目录
# # os.makedirs(r"abc\abc")      # 可以看见在D:\study\new_test\study_for_python（因为上面已经change到了此目录）此目录下面创建了abc\abc多级目录
# # os.removedirs(r"abc\abc")      # 可以看见将上面创建的abc\abc都给删除了(abc\abc各级目录都是空目录才会被一起删除，如果任何有内容的目录将不会被删)，也就是只删除空文件
# # os.mkdir(r"abc")     # 可以看见在目录下面创建了abc文件夹（此命令并不能多级创建文件夹）
# # os.rmdir("abc")       # 删除单个文件夹对应mkdir，当目录不为空删除不了，只能删除空目录
# os.remove("test.py")      # 删除文件，不能删除文件夹


L = os.listdir(r"D:\study\new_test\study_for_python")      # 列出指定目录下面的所有文件和目录，以列表格式输出，类似于ls -l
print(L)

# os.rename("README.md", "README.MD")         # 重命名文件或者目录，前者为源文件名，后者为命名后的文件名
# print(os.stat("homework"))      # 获取文件或者目录的信息：os.stat_result(st_mode=16895, st_ino=1970324836985797, st_dev=2225790372, st_nlink=1, st_uid=0, st_gid=0, st_size=4096, st_atime=1512231761, st_mtime=1512231761, st_ctime=1512231761)
print(os.sep)     # 输出操作系统路径的分隔符
print(os.pathsep)
print(os.name)    #
# os.system("dir")   # 运行终端命令，win的cmd命令行串口，linux下面的终端命令行
'''
>>> os.system("ls -l")
total 0
drwxrwxrwx 0 root root 512 Nov 28 21:47 study_for_python

>>> os.system("free -m")
              total        used        free      shared  buff/cache   available
Mem:          20377        6342       13803          17         230       13897
Swap:         13349          35       13313
0
'''
# print(os.environ)    # 获取系统的环境变量





print(os.path.isfile("test.py"))        # 判断文件是否存在，返回True或者False
print(os.path.abspath("week2"))         # 打印当前
print(os.path.abspath("README.MD"))

