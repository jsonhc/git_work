# Author: wadeson
# date: 2017/12/2

name = input("please input your name:")
age = input("please input your age:")
job = input("please input your job:")
salary = input("please input your salary:")

if salary.isdigit():   # 判断输入的字符串是否全部是整数
    salary = int(salary)   # 强制将字符串转换为整形
else:
    print("please input digit!")
    exit()  # exit方法退出整个程序
    # 或者直接将字符串写入到exit方法中
    # exit("please input digit!")  这种方式就不需要print方法了

# 格式化输出，选中一段代码进行注释：ctrl+?（不需要加上shift）
msg = '''
-----------info of %s------------------
name: %s
age: %s
job: %s
salary: %s
-----------end-------------------------
''' % (name, name, age, job, salary)

print(msg)
