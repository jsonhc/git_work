# Author: wadeson
# date: 2017/12/3

import os

print(os.getcwd())  # 打印当前路径，类似于linux下面的pwd
os.chdir(r"D:\study\new_test\study_for_python")  # 改变到指定目录，类似cd
# print(os.getcwd())
#
# print(os.curdir)   # 返回.,代表当前路径
# print(os.pardir)   # 返回..，代表上一级目录
# # os.makedirs(r"abc\abc")      # 可以看见在D:\study\new_test\study_for_python（因为上面已经change到了此目录）此目录下面创建了abc\abc多级目录
# # os.removedirs(r"abc\abc")      # 可以看见将上面创建的abc\abc都给删除了(abc\abc各级目录都是空目录才会被一起删除，如果任何有内容的目录将不会被删)，也就是只删除空文件
# # os.mkdir(r"abc")     # 可以看见在目录下面创建了abc文件夹（此命令并不能多级创建文件夹）
# # os.rmdir("abc")       # 删除单个文件夹对应mkdir，当目录不为空删除不了，只能删除空目录
# os.remove("test.py")      # 删除文件，不能删除文件夹


L = os.listdir(r"D:\study\new_test\study_for_python")  # 列出指定目录下面的所有文件和目录，以列表格式输出，类似于ls -l
print(L)

# os.rename("README.md", "README.MD")         # 重命名文件或者目录，前者为源文件名，后者为命名后的文件名 print(os.stat("homework"))      #
# 获取文件或者目录的信息：os.stat_result(st_mode=16895, st_ino=1970324836985797, st_dev=2225790372, st_nlink=1, st_uid=0,
# st_gid=0, st_size=4096, st_atime=1512231761, st_mtime=1512231761, st_ctime=1512231761)
print(os.sep)  # 输出操作系统路径的分隔符
print(os.pathsep)
print(os.name)  #
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





print(os.path.isfile("test.py"))      # 判断文件是否存在，返回True或者False
print(os.path.abspath("week2"))  # 打印当前文件或目录的绝对路径
print(os.path.abspath("README.MD"))

s = os.path.split(r"D:\study\new_test\study_for_python\README.MD")      # 将文件路径进行切割，返回一个元祖
print(s)

print(os.path.dirname(r"D:\study\new_test\study_for_python\README.MD"))         # 类似于shell下面的dirname命令

print(os.path.basename(r"D:\study\new_test\study_for_python\README.MD"))        # 类似于shell下面的basename命令

# print(os.path.exists(r"D:\study\new_test\study_for_python"))           # 判断文件或目录是否存在，返回True或者False
#
# print(os.path.isabs("README.MD"))         # 判断给定的文件或目录是否是绝对路径，返回True或者False

print(os.path.isfile("README.MD"))          # 判断是否是一个文件，返回True或者False

print(os.path.isdir("README.MD"))          # 判断是否是一个目录，返回True或者False

abc_path = os.path.join(r"D:\study\new_test\study_for_python", "README.MD")        # 将给定的多个目录进行拼接在一起
print(abc_path)

print(os.path.getatime(r"D:\study\new_test\study_for_python"))                # 返回文件或者目录的属性信息atime

print(os.path.getmtime(r"README.MD"))                     # 返回文件或者目录的属性信息mtime

print(os.path.getsize(r'/root/script/thread/thread_condition.py'))   # 获取指定文件的大小

os.walk: os.walk(top, topdown=True, onerror=None, followlinks=False)
  top是要遍历的目录。
  topdown是代表要从上而下遍历还是从下往上遍历。
  onerror可以用来设置当便利出现错误的处理函数(该函数接受一个OSError的实例作为参数)，设置为空则不作处理。
  followlinks表示是否要跟随目录下的链接去继续遍历，要注意的是，os.walk不会记录已经遍历的目录，所以跟随链接遍历的话有可能一直循环调用下去。
  os.walk返回的是一个3个元素的元组 (root, dirs, files) ，分别表示遍历的路径名，该路径下的目录列表和该路径下文件列表。注意目录列表和文件列表不是具体路径，需要具体路径(从root开始的路径)的话可以用 os.path.join(root,dir) 和 os.path.join(root,dir)

#!/usr/bin/python

import os

for dirpath, dirnames, filenames in os.walk(r'/root/script',True):
    print(dirpath)
    for dir in dirnames:
        print(dir)
    for f in filenames:
        f_path=os.path.join(dirpath,f)
        f_size=os.path.getsize(f_path)
        print(f,f_size)

执行结果：
/root/script
/root/script/mysql
mysql_connect4.py 322
mysql_connect_thread.py 854
mysql_connect.py 329
mysql_connect3.py 322
mysql_connect_thread1.py 666
mysql_connect2.py 314
mysql_connect1.py 568
business.sql 942










