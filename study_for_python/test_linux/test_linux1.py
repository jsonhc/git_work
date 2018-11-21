# __author__ = 'Administrator'
# coding=utf8


import os

base_dir = os.path.dirname(os.path.abspath(__file__))  # 打印当前位置的上级绝对路径，os.path.dirname打印当前位置的上一级目录
print(__file__)
print("=====================================")
print(os.getcwd())
# os.path.abspath(file) 打印file内容的绝对路径
base_abs = os.path.abspath(__file__)
print(base_dir)
print(base_abs)


str_bytes_path = os.path.join(base_dir, 'str_bytes.py')
print(str_bytes_path)

# 获取文件的大小
# file_size = os.stat(str_bytes_path).st_size
# f_size = os.path.getsize(str_bytes_path)
file_size = os.stat(base_abs).st_size
f_size = os.path.getsize(base_abs)
print(file_size)
print(f_size)
