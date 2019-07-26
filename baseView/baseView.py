# -*- coding:utf-8 -*-

class BaseView():
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,*args):
        return self.driver.find_element(*args)

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self,start_x,start_y,end_x,end_y,duration):
        return self.driver.swipe(start_x,start_y,end_x,end_y,duration)

    def close_app(self):
        return self.driver.quit()






