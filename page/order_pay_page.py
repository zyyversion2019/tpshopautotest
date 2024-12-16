from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class OrderPayPage(BaseAction):

    # 订单状态信息
    tips_info = By.CSS_SELECTOR, ".erhuh h3"
    # 货到付款 选框
    arrived_pay = By.CSS_SELECTOR, "[value='pay_code=cod']"
    # 确认支付方式 按钮
    pay_btn = By.CLASS_NAME, "button-confirm-payment"

    # 获取订单状态信息
    def get_tips_info(self):
        return self.find_el(self.tips_info).text
    # 点击货到付款选框
    def click_arrived_pay(self):
        return self.click(self.arrived_pay)
    # 点击确认支付按钮
    def click_pay_btn(self):
        return self.click(self.pay_btn)
