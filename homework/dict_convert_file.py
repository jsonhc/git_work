#!/usr/bin/python3

d = {"name": "wadeson","passwd": "redhat"}
with open("dict_convert_file.txt","w") as f:
    for i in d:
        f.write("%s\t%s\n" % (i,d[i]))
