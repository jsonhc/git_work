#!/usr/bin/python3

L = []
with open("lock_user.txt","r") as f:
    for i in f.readlines():
        L.append(i.strip())
print(L)
