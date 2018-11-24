import filecmp
print(filecmp.cmp('python_difflib.py', 'python_difflib1.py'))   # 比对两个文件的差异
print(filecmp.dircmp('/home/wadeson'))
