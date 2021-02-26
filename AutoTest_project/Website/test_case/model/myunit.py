import unittest
from driver import *

class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver=browser()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
    def tearDown(self):
        #pass
        self.driver.close()
