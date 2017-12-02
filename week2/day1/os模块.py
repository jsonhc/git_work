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
# # os.removedirs(r"abc\abc")      # 可以看见将上面创建的abc\abc都给删除了
# # os.mkdir(r"abc")     # 可以看见在目录下面创建了abc文件夹（此命令并不能多级创建文件夹）
# # os.rmdir("abc")       # 删除单个文件夹对应mkdir


L = os.listdir(r"D:\study\new_test\study_for_python")      # 列出指定目录下面的所有文件和目录，以列表格式输出
print(L)



