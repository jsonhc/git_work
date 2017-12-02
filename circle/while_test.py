#!/usr/bin/python3

age_of_origin = 60
while True:
    get_age = int(input("please input your age:"))
    if get_age == age_of_origin:
        print("yes")
        break
    elif get_age < age_of_origin:
        print("you should try to change bigger")
    else:
        print("you should try to change smaller")


print("END the game")
