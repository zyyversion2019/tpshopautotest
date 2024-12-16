from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class IndexPage(BaseAction):

    # 登录链接 按钮
    login_link_btn = By.CLASS_NAME, "red"
    # 搜索 输入框
    search_input = By.ID, "q"
    # 搜索 按钮
    search_btn = By.CLASS_NAME, "ecsc-search-button"
    # 我的订单 链接
    my_order_link = By.CSS_SELECTOR, ".top-ri-header > li:nth-child(1) > a:nth-child(1)"
    # 我的购物车 链接
    my_cart_link = By.CSS_SELECTOR, ".c-n"

    # 点击登录链接
    def click_login_link(self):
        return self.click(self.login_link_btn)
    # 输入关键字
    def input_keywords(self, content):
        return self.input(self.search_input, content)
    # 点击搜索按钮
    def click_search_btn(self):
        return self.click(self.search_btn)
    # 点击我的订单链接
    def click_my_order_link(self):
        return self.click(self.my_order_link)
    # 点击我的购物车链接
    def click_my_cart_link(self):
        return self.click(self.my_cart_link)