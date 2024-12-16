# 获取/关闭浏览器驱动的类
import logging

from selenium import webdriver


class DriverUtils:
    __driver = None
    __switch = False

    # 获取浏览器驱动
    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            logging.info("creat chrome driver")
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(10)
        else:
            logging.info("use existed chrome driver")
        return cls.__driver

    # 关闭浏览器驱动
    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None and cls.__switch is False:
            logging.info("quit chrome driver")
            cls.__driver.quit()
            cls.__driver = None
        else:
            logging.info("chrome driver is still alive")

    @classmethod
    def set_switch(cls, switch):
        cls.__switch = switch