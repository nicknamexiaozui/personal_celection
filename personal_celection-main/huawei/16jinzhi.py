'''
输出该数值的十进制字符串。不同组的测试用例用\n隔开。
'''
while True:
    try:
        a=input()
        print(int(a, 16))
    except:
        break