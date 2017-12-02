#!/usr/bin/python3

num = 1
line = 4

while num <= line:
    num1 = 0
    while num1 <= line - num:
        print("*", end="")
        num1 = num1 + 1

    print("")
    num = num + 1
