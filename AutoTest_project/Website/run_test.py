import unittest
from function import *
from BSTestRunner import BSTestRunner
import time
report_dir = './test_report'
test_dir = './test_case'
print("run test case")
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+'result.html'
print("result is writed")
with open(report_name, 'wb')as f:
    runer = BSTestRunner(stream=f, title='Test Report', description='Test case result')
    runer.run(discover)
f.close()
print("send email")

send_email('568337691@qq.com',)
