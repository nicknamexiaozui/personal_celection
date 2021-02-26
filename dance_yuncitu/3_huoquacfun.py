#-- coding: utf-8 --
#@Time : 2021/2/4 8:52
#@Author : XXXX
#@Email : XXXX@qq.com
#@File : huoquacfun.py
#@Software: PyCharm
from selenium import webdriver
import time
import datetime
import re
now_time = datetime.datetime.now()
print(now_time)
driver=webdriver.Firefox()
driver.get('https://www.acfun.cn/v/ac23596655')
time.sleep(10)
driver.refresh()
time.sleep(5)
driver.find_element_by_class_name('danmaku-fold').click()
source=driver.page_source
#print(type(source))
txt=re.findall("data-message=\"(.*?)\"", source)
now_time1 = datetime.datetime.now()
print(now_time1)
print(txt)
print(type(txt))
print(len(txt))
with open('./bullet.txt','a',encoding='utf-8') as q:
	for i in range(len(txt)):
		q.write(txt[i])
		q.write('\n')
q.close()
