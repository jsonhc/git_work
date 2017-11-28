#!/usr/bin/python3

L = ["user1","user2","user3"]

with open("list_convert_file.txt","w") as f:
    for i in L:
        f.write("%s\n" % i)
