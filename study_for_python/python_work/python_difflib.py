import difflib
test1 = '''
this is A
this is B
this is C
'''
test1_lines = test1.splitlines()   # splitlines()以行作为分割
# print(type(test1_lines))
# for l in test1_lines:
#     print(l)      # 得到每一行的数据
test2 = '''
this is A
this is B
this is c
'''
test2_lines = test2.splitlines()
# d = difflib.Differ()
# diff = d.compare(test1_lines, test2_lines)
# print("\n".join(list(diff)))

d = difflib.HtmlDiff()
print(d.make_file(test1_lines, test2_lines))    # 比对出不同的地方的结果以html的格式输出出来
