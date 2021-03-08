import re
n=float(input())
str_n=str(n)
a=re.findall('\.(\d)',str_n)
# print(a)
if int(a[0])>=5:
    print(int(n)+1)
else:
    print(int(n))