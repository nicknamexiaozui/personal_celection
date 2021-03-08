'''计算最小公倍数和最大公约数'''
def fun_print():
    n=input('')
    xin_list=[]
    list=n.split(' ')
    for i in range(len(list)):
        xin_list.append(int(list[i]))
    a=xin_list[0]
    b=xin_list[1]
    sum=a*b
    while b !=0:
        temp=a%b
        a=b
        b=temp
    sum=sum/a
    return int(sum)
print(fun_print())
