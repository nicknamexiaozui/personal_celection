from BasePage import *
from selenium.webdriver.common.by import By
class LoginPage(Page):
    url=''
    username_loc = (By.XPATH,"//input[@placeholder='账号']")
    password_loc = (By.XPATH,'//input[@placeholder="密码"]')
    yanzm_loc = (By.XPATH,'//input[@placeholder="验证码"]')
    submit_loc = (By.XPATH,'//button')

    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)


    def type_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_yanzm(self,yanzm):
        self.find_element(*self.yanzm_loc).clear()
        self.find_element(*self.yanzm_loc).send_keys(yanzm)

    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    def Login_action(self,username,password,yanzm):
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_yanzm(yanzm)
        self.type_submit()


    #用户不存在或者密码错误定位
    login_errorinfo_loc = (By.XPATH,'/html/body/div[2]/p')
    def print_errorinfo_hit(self):
        return self.find_element(*self.login_errorinfo_loc).text
    #用户名和密码必输项提示
    login_usernamebishu_loc = (By.XPATH,'/html/body/div/div/div/div/div/div/form/div[2]/div/div[2]')
    login_passwdbishu_loc = (By.XPATH,'/html/body/div/div/div/div/div/div/form/div[3]/div/div[2]')
    def print_usernamebishu_hit(self):
        return self.find_element(*self.login_usernamebishu_loc).text
    def prin_passwdbishu_hit(self):
        return self.find_element(*self.login_passwdbishu_loc).text

