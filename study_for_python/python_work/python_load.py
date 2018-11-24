with open("/proc/loadavg", "r") as f:
    con = f.read()
f.close()

# read()方法返回的是str类型
con_result = con.split()
print(con_result)


with open("/proc/loadavg", "r") as f1:
    result = f1.readlines()
f1.close()

# readlines()方法返回是list类型
print(result)


def getload():
    with open("/proc/loadavg", "r") as f2:
        con2 = f2.read().split()
    f.close()
    return con2


print(getload()[0])
