from BasePage import *
from selenium.webdriver.common.by import By
class ManagePage(Page):
    url = ''
    #系统管理
    systemmanage_loc = (By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[1]/div/ul/li/div/span')
    #域管理
    yumanage_loc = (By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[1]/div/ul/li/ul/li[2]/span')
    #域管理下的新增
    add_loc = (By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[1]/form/div[3]/button')
    #点击系统管理，展现下拉菜单
    def click_systemmanage(self):
        self.find_element(*self.systemmanage_loc).click()
    #点击域管理
    def click_yumanage(self):
        self.find_element(*self.yumanage_loc).click()
    #点击新增
    def click_add(self):
        self.find_element(*self.add_loc).click()
    #新增域成功时，提示元素定位
    add_succes_loc = (By.XPATH,'/html/body/div[5]/p')
    def print_add_succes_hit(self):
        return self.find_element(*self.add_succes_loc).text
