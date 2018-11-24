
# with open("/proc/meminfo", "r") as f:
#     for line in f.readlines():
#         if line.split(":")[0] == "MemTotal":
#             print(line)
#         elif line.split(":")[0] == "MemFree":
#             print(line)
#         # else:
#         #     print("it is wrong")
# f.close()


def getmemmory():
    with open("/proc/meminfo", "r") as f1:
        for line in f1.readlines():
            if line.split(":")[0] == "MemTotal":
                print(line)
            elif line.split(":")[0] == "MemFree":
                print(line)
    f1.close()


if __name__ == '__main__':
    print(__name__)
    getmemmory()