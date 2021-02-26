from BasePage import *
from selenium.webdriver.common.by import By
class NeweamilPage(Page):
    quxiaofengbiefasong_loc = (By.CLASS_NAME,'bg-purple-light right_distanceone')
    def type_quxiaofengbiefasong(self):
        self.find_element(*self.quxiaofengbiefasong_loc).click()
    def click_quxiaofengbiefasong(self):
        self.type_quxiaofengbiefasong()
