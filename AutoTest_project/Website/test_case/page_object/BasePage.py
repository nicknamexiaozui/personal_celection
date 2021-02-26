from time import sleep
from selenium import webdriver
class Page():
    def __init__(self,driver):
        self.driver=driver
        self.base_url="http://192.168.10.205:81/#/login"
        self.timeout=10

    def _open(self,url):
        url_ = self.base_url+url
        print("Test page is %s" %url_)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        assert self.driver.current_url==url_ ,'Did not land on %s' %url_

    def open(self):
        self._open(self.url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.implicitly_wait(20)
    driver.maximize_window()
    main=Page(driver)
