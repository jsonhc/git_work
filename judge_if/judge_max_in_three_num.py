#!/usr/bin/python3

num1 = int(input("please input num1:"))
num2 = int(input("please input num2:"))
num3 = int(input("please input num3:"))
max_num = 0


def max_fun(n1,n2):
    if n1 > n2:
        print("the max number is ",n1)
    else:
        print("the max number is ",n2)

# 先两两num比较，得出最大的那一个，然后在和num3进行比较,得出三个中最大的那一个
if num1 > num2:
    max_num = num1
    max_fun(max_num,num3)
else:
    max_num = num2
    max_fun(max_num,num3)

