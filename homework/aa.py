#!/usr/bin/python3

n = int(input("please input a number: "))
init_num = int(input("pleasr input a init number: "))
total = 0
num1 = 0

for i in range(n):
    num1 = num1 + (10**i)*init_num 
    total = total + num1

print(total)
