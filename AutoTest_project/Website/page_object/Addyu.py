from BasePage import *
from selenium.webdriver.common.by import By
class Addyu(Page):
    #系统管理员密码
    sysadminpasswd_loc = (By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/form/div[1]/div/div[1]/input')
    #域名称
    yuname_loc = (By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/form/div[2]/div/div[1]/input')
    #域最大用户数
    maxusers_loc = (By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/form/div[7]/div/div[1]/input')
    #启用状态
    usestate_loc = (By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/form/div[9]/div/div/div/input')
    #启用
    use_loc = (By.XPATH,'/html/body/div[4]/div[1]/div[1]/ul/li[1]')
    #停用
    stop_loc = (By.XPATH,'/html/body/div[4]/div[1]/div[1]/ul/li[2]')
    #域超级管理员账号
    yusuperaccount_loc = (By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/form/div[10]/div/div[1]/input')
    #域超级管理员名称
    yusuperofname_loc = (By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/form/div[11]/div/div[1]/input')
    #域管理员密码
    yusystempasswd_loc = (By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/form/div[12]/div/div/input')
    #确认密码
    confirmpasswd_loc = (By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/form/div[13]/div/div/input')
    #确认按钮
    quedingbutton_loc = (By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[3]/span/button[1]')
    #取消按钮
    cancelbutton_loc = (By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[3]/span/button[2]')
    #弹窗X
    close_loc = (By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/button/i')
    def type_sysadminpasswd(self,sysadminpasswd):
        self.find_element(*self.sysadminpasswd_loc).clear()
        self.find_element(*self.sysadminpasswd_loc).send_keys(sysadminpasswd)
    def type_yuname(self,yuname):
        self.find_element(*self.yuname_loc).clear()
        self.find_element(*self.yuname_loc).send_keys(yuname)
    def type_maxusers(self,maxusers):
        self.find_element(*self.maxusers_loc).clear()
        self.find_element(*self.maxusers_loc).send_keys(maxusers)
    def type_usestate(self):
        self.find_element(*self.usestate_loc).click()
    def type_use(self):
        self.find_element(*self.use_loc).click()
    def type_yusuperaccount(self,yusuperaccount):
        self.find_element(*self.yusuperaccount_loc).clear()
        self.find_element(*self.yusuperaccount_loc).send_keys(yusuperaccount)
    def type_yusuperofname(self,yusuperofname):
        self.find_element(*self.yusuperofname_loc).clear()
        self.find_element(*self.yusuperofname_loc).send_keys(yusuperofname)
    def type_yusystempasswd(self,yusystempasswd):
        self.find_element(*self.yusystempasswd_loc).clear()
        self.find_element(*self.yusystempasswd_loc).send_keys(yusystempasswd)
    def type_confirmpasswd(self,confirmpasswd):
        self.find_element(*self.confirmpasswd_loc).clear()
        self.find_element(*self.confirmpasswd_loc).send_keys(confirmpasswd)
    def type_condirmbutton(self):
        self.find_element(*self.quedingbutton_loc).click()
    def type_cancel(self):
        self.find_element(*self.cancelbutton_loc).click()

    def type_action(self,sysadminpasswd,yuname,maxusers,yusuperaccount,
                    yusuperofname,yusystempasswd,confirmpasswd):
        sleep(1)
        self.type_sysadminpasswd(sysadminpasswd)
        self.type_yuname(yuname)
        self.type_maxusers(maxusers)
        self.type_yusuperaccount(yusuperaccount)
        self.type_yusuperofname(yusuperofname)
        self.type_yusystempasswd(yusystempasswd)
        self.type_confirmpasswd(confirmpasswd)
        self.type_usestate()
        self.type_use()
        self.type_condirmbutton()
#新增域时，必输项提示元素定位
