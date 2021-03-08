'''
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是0。
'''
s=input()
s=s[::-1]
y=''
for i in s:
    if i not in y and i not in '0':
        y=y+i
print(y)