from BasePage import *
from selenium.webdriver.common.by import By
class IndexPage(Page):
    newemail_loc = (By.XPATH,'/html/body/div[1]/div/div[3]/div[2]/div[1]/div/ul/li[1]/i')
    def type_newemael(self):
        self.find_element(*self.newemail_loc).click()
    def click_newmail(self):
        self.type_newemael()
