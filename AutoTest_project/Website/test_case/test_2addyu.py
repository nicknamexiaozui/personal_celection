import unittest
from model import function,myunit
from page_object.LoginPage import *
from page_object.ManagePage import *
from page_object.Addyu import *
from time import sleep
from test_data import login_data as LD
from test_data  import addyu_data as AD

class YuaddTest(myunit.StartEnd):
    def test_add1_normal(self):
        '''正常新增域'''
        po = LoginPage(self.driver)
        po.Login_action(LD.sysadmin_data["user"],LD.sysadmin_data["passwd"],LD.sysadmin_data["yanzm"])
        sleep(2)
        button = ManagePage(self.driver)
        button.click_systemmanage()
        sleep(1)
        button.click_yumanage()
        sleep(1)
        button.click_add()
        add =Addyu(self.driver)
        add.type_action(AD.normal_data["sysadminpasswd"],AD.normal_data["yuname"],AD.normal_data["maxusers"],
                        AD.normal_data["yusuperaccount"],AD.normal_data["yusuperofname"],AD.normal_data["yusystempasswd"],
                        AD.normal_data["confirmpasswd"])
        self.assertEqual(button.print_add_succes_hit(),'新增域成功！')
        function.insert_img(self.driver,'test_add1_normal.png')
        sleep(1)
    def test_add2_error(self):
        '''系统管理员密码错误时'''
        po = LoginPage(self.driver)
        po.Login_action(LD.sysadmin_data["user"],LD.sysadmin_data["passwd"],LD.sysadmin_data["yanzm"])
        sleep(2)
        button = ManagePage(self.driver)
        button.click_systemmanage()
        sleep(1)
        button.click_yumanage()
        sleep(1)
        button.click_add()
        add =Addyu(self.driver)
        add.type_action(AD.systempasswdwrong_data["sysadminpasswd"],AD.systempasswdwrong_data["yuname"],AD.systempasswdwrong_data["maxusers"],
                        AD.systempasswdwrong_data["yusuperaccount"],AD.systempasswdwrong_data["yusuperofname"],AD.systempasswdwrong_data["yusystempasswd"],
                        AD.systempasswdwrong_data["confirmpasswd"])
        self.assertEqual(button.print_add_succes_hit(),'检验账号密码失败')
        function.insert_img(self.driver,'test_add2_error.png')
        sleep(1)
    def test_add3_error(self):
        '''域超级管理员账号已经注册'''
        po = LoginPage(self.driver)
        po.Login_action(LD.sysadmin_data["user"],LD.sysadmin_data["passwd"],LD.sysadmin_data["yanzm"])
        sleep(2)
        button = ManagePage(self.driver)
        button.click_systemmanage()
        sleep(1)
        button.click_yumanage()
        sleep(1)
        button.click_add()
        add =Addyu(self.driver)
        add.type_action(AD.nameused_data["sysadminpasswd"],AD.nameused_data["yuname"],AD.nameused_data["maxusers"],
                        AD.nameused_data["yusuperaccount"],AD.nameused_data["yusuperofname"],AD.nameused_data["yusystempasswd"],
                        AD.nameused_data["confirmpasswd"])
        self.assertEqual(button.print_add_succes_hit(),'域超级管理员账号已经注册')
        function.insert_img(self.driver,'test_add3_error.png')
        sleep(1)
    def test_add4_error(self):
        '''域超级管理员账号已经注册'''
        po = LoginPage(self.driver)
        po.Login_action(LD.sysadmin_data["user"],LD.sysadmin_data["passwd"],LD.sysadmin_data["yanzm"])
        sleep(2)
        button = ManagePage(self.driver)
        button.click_systemmanage()
        sleep(1)
        button.click_yumanage()
        sleep(1)
        button.click_add()
        add =Addyu(self.driver)
        add.type_action(AD.yunameused_data["sysadminpasswd"],AD.yunameused_data["yuname"],AD.yunameused_data["maxusers"],
                        AD.yunameused_data["yusuperaccount"],AD.yunameused_data["yusuperofname"],AD.yunameused_data["yusystempasswd"],
                        AD.yunameused_data["confirmpasswd"])
        self.assertEqual(button.print_add_succes_hit(),'域名称已经注册')
        function.insert_img(self.driver,'test_add4_error.png')
        sleep(1)
    # def test_add5_error(self):
    #     '''输入为空，校验必输项'''
    #     po = LoginPage(self.driver)
    #     po.Login_action(LD.sysadmin_data["user"],LD.sysadmin_data["passwd"],LD.sysadmin_data["yanzm"])
    #     sleep(2)
    #     button = ManagePage(self.driver)
    #     button.click_systemmanage()
    #     sleep(1)
    #     button.click_yumanage()
    #     sleep(1)
    #     button.click_add()
    #     add =Addyu(self.driver)
    #     add.type_action(AD.kong_data["sysadminpasswd"],AD.kong_data["yuname"],AD.kong_data["maxusers"],
    #                     AD.kong_data["yusuperaccount"],AD.kong_data["yusuperofname"],AD.kong_data["yusystempasswd"],
    #                     AD.kong_data["confirmpasswd"])
    #     self.assertEqual(button.print_add_succes_hit(),'域名称已经注册')
    #     function.insert_img('test_add5_error.png')
if __name__ == '__main__':
    unittest.main()
