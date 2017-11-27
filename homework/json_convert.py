#!/usr/bin/python3
import json

with open("username.json","r") as f:
    user_dict=json.load(f)

print(user_dict)
print(user_dict["name"])
print(user_dict["password"])
