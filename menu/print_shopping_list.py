#!/usr/bin/python3

shop_list = {}

with open("shopping_list.txt","r") as f:
    for i in f.readlines():
        (item,price) = i.strip().split()
        shop_list[item] = price

print(shop_list)

for index in enumerate(shop_list):
    print(index)
