import unittest
from model import function,myunit
from page_object.LoginPage import *
from time import sleep
from test_data import login_data as LD

class LoginTest(myunit.StartEnd):
    def test_login1_normal(self):
        '''正常用户正常登录测试'''
        print("test_login1_normal is started...")
        po=LoginPage(self.driver)
        po.Login_action(LD.success_data["user"],LD.success_data["passwd"],LD.success_data["yanzm"])
        sleep(2)
        self.assertEqual(self.driver.title,'航信邮件管理系统 | 首页')
        function.insert_img(self.driver,'test_login1_normal.png')
        print("test_login1_nomal is ended...")
    def test_login2_error(self):
        '''无此用户登录测试'''
        po=LoginPage(self.driver)
        po.Login_action(LD.nouser_data["user"],LD.nouser_data["passwd"],LD.nouser_data["yanzm"])
        self.assertEqual(po.print_errorinfo_hit(),'用户不存在')
        function.insert_img(self.driver, 'test_login2_error.png')
    def test_login3_error(self):
        '''用户密码错误登录测试'''
        po=LoginPage(self.driver)
        po.Login_action(LD.errorpasswd_data["user"],LD.errorpasswd_data["passwd"],LD.errorpasswd_data["yanzm"])
        self.assertEqual(po.print_errorinfo_hit(),'用户密码错误')
        function.insert_img(self.driver, 'test_login3_error.png')
    def test_login4_bishu(self):
        '''用户名和密码必输项测试'''
        po=LoginPage(self.driver)
        po.Login_action(LD.kong_data["user"],LD.kong_data["passwd"],LD.kong_data["yanzm"])
        self.assertEqual(po.print_usernamebishu_hit(),'请输入用户名')
        self.assertEqual(po.prin_passwdbishu_hit(),'请输入密码')
        function.insert_img(self.driver, 'test_login4_error.png')


if __name__ == '__main__':
    unittest.main()
