#!/usr/bin/python3

num = 1

while num <= 4:
    num1 = 1
    while num1 <= num:
        print("*", end="")
        num1 = num1 + 1

    print("")
    num = num + 1
