#!/usr/bin/python3
age_of_origin=80

guess_age=int(input("input your age:"))

if guess_age == age_of_origin:
    print("yes")
elif guess_age > age_of_origin:
    print("try to guess smaller")
else:
    print("try to guess large")

