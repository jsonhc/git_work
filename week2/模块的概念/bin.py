# Author: wadeson
# date: 2017/12/3

# import calculate      # 通过搜索路径找到calculate.py后，将py里面的所有代码都进行解析了一遍，如果有print语句，则这里直接进行打印出来了
from calculate import plus, sub
import sys
print(sys.path)
# print(calculate.plus(1, 2))
print(plus(1, 2))
