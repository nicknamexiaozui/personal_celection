import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
import os
'''读取项目相对路径到scrennshot文件夹'''
def insert_img(driver,filename):
    '''读取function.py文件所在的目录'''
    func_path=os.path.dirname(__file__)
    print(func_path)
    '''读取上一级目录'''
    base_dir = os.path.dirname(func_path)
    print(base_dir)
    '''完成字符串转换和替换符号'''
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\' , '/')
    '''拆分目录为列表'''
    base = base_dir.split('/Website')[0]
    print(base)
    '''拼接完整的路径和文件名'''
    filepath = base + '/Website/test_report/screenshot/' + filename
    driver.get_screenshot_as_file(filepath)
'''获取最新的测试报告'''
def get_report_file():
    '''获取最新的测试报告'''
    '''读取function.py文件所在的目录'''
    func_path=os.path.dirname(__file__)
    print(func_path)
    '''读取上一级目录'''
    base_dir = os.path.dirname(func_path)
    print(base_dir)
    '''完成字符串转换和替换符号'''
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\' , '/')
    '''拆分目录为列表'''
    base = base_dir.split('/Website')[0]
    print(base)
    '''拼接完整的路径和文件名'''
    filepath = base + '/Website/test_report/'
    reportpath=filepath
    lists = os.listdir(reportpath)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(reportpath, fn)))
    # 找到最新生成的报告文件
    reportfile = os.path.join(reportpath, lists[-1])
    return reportfile

'''运行163邮箱发送测试报告'''
def send_email(receiver):

        #发送邮箱服务器
        smtpserver='smtp.163.com'
        # 创建一个带附件的邮件实例
        msg=MIMEMultipart()

        #发送邮箱用户名密码
        user='nicknamexz@163.com'
        passwd='aaa13145200'

        #发送邮箱和接收邮箱
        sender='nicknamexz@163.com'
        # receivers = ['hb.tianxiaoyun@aisino.com','568337691@qq.com']

        #发送邮件的主题和内容
        subject='web自动化测试报告'
        text='测试结果请查看HTML附件'
        #构造html附件
        a=get_report_file()
        att3 = MIMEText(open(a, 'rb').read(), 'base64', 'utf-8')
        att3["Content-Type"] = 'application/octet-stream'
        att3["Content-Disposition"] = 'attachment; filename="result.html"'
        msg.attach(att3)
        #HTML邮件正文
        zhengwen=MIMEText(text,'plain','utf-8')
        msg.attach(zhengwen)
        msg['Subject']=Header(subject,'utf-8')
        msg['From']=sender
        msg['To']=Header(','.join(receiver))
        #SSL协议端口号使用465
        smtp=smtplib.SMTP_SSL(smtpserver,465)
        #向服务器标识用户身份
        smtp.helo(smtpserver)
        smtp.ehlo(smtpserver)
        smtp.login(user,passwd)
        print('开始发送邮件。。。')
        smtp.sendmail(sender,receiver,msg.as_string())
        smtp.quit()
        print('邮件发送完成！')

if __name__ == '__main__':
    driver = webdriver.Firefox()
    # driver.get("http://www.sogou.com")
    # insert_img(driver,'sougou.png')
    # driver.quit()
    a=get_report_file()
    print(a)
