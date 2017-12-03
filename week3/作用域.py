# Author: wadeson
# date: 2017/12/3

# 作用域的作用范围顺序：L-E-G-B，其中L为local局部变量，E(enclosing)嵌套变量，G全局变量，B是python中的内置变量
# 如果local找不到就找E区，E区找不到就找G区，最后找B

a = 10
def external():
    x = 5
    def inner():
        print(a)
    inner()
    print(a)


if __name__ == "__main__":
    external()
