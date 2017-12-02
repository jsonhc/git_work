#!/usr/bin/python3


line = 4
num = line
while line > 0:
    num1 = 0
    while num1 <= num - line:
        print("*", end="")
        num1 = num1 + 1

    print("")
    line = line - 1
