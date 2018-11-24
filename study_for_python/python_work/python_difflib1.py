import difflib
import sys
try:
    testfile1 = sys.argv[1]
    testfile2 = sys.argv[2]
except Exception as e:
    print(e)
    print("Usage: python3 %s filename1 filename2" % (__file__))
    sys.exit()


def readfile(filename):
    try:
        file = open(filename, "r")
        # text = file.read().splitlines()     # read()方法将文件的内容都读出来,返回的是str类型,splitlines()以行为分割
        text = file.readlines()   # readlines()方法将文件以行的方式读出来保存在一个list中
        file.close()
        return text
    except Exception as e:
        print(e)
        sys.exit()


testfile1_lines = readfile(testfile1)
testfile2_lines = readfile(testfile2)
d = difflib.HtmlDiff()
print(d.make_file(testfile1_lines, testfile2_lines))
