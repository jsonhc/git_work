#!/usr/bin/python3

height = int(input("please input the height:"))
width = int(input("please input the width:"))
init_height = 1

while init_height <= height:
    init_width = 1
    while init_width <= width:
        print("#",end="")
        init_width = init_width + 1
    init_height = init_height + 1
    print("")
