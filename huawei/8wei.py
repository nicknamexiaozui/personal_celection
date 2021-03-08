'''
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
'''
while True:
    try:
        a = input()
        if len(a) < 8:
            n = 8 - len(a)
            print(a + '0' * n)
        # if len(a) == 8:
        #     print(a)
        if len(a) >=8:
            x = len(a) % 8   #0
            l=int(len(a)/8)  #1
            for i in range(l):
                b=a[0+8*i:8+8*i]
                print(b)
            if x!=0:
                c = a[8*l:len(a)] + '0' * (8 - x)
                print(c)
    except:
        break