'''
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。
'''
num = int(input())
def func(num):
    prime_num = 1
    for i in range(2,int(num**0.5+2)):
        if num%i == 0:
            prime_num = 0
            b = int(num/i)
            print(str(i),end=' ')
            func(b)
            break
    if prime_num == 1:
        print(str(num),end=' ')
func(num)

