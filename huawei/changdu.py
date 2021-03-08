'''计算输入一行字符串最后空格的长度'''
import sys

for line in sys.stdin:
    a = line.split()
    print(len(a[-1]))
    break