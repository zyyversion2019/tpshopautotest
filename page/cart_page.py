from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class CartPage(BaseAction):

    # 去结算 按钮
    go_to_pay_btn = By.CLASS_NAME, "gwc-qjs"

    # 点击去结算按钮
    def click_go_to_pay_btn(self):
        return self.click(self.go_to_pay_btn)
