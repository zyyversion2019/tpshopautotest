import time
from page.cart_page import CartPage
from page.home_page import HomePage
from page.index_page import IndexPage
from page.order_page import OrderPage
from page.order_pay_page import OrderPayPage
from utils.driver_utils import DriverUtils


class TestOrder:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.index_page = IndexPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.order_page = OrderPage(self.driver)
        self.order_pay_page = OrderPayPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.driver.get("http://localhost/")

    def teardown(self):
        time.sleep(3)
        DriverUtils.quit_driver()

    # 运行于类的结束, 而不是测试方法的结束, 执行完全部测试脚本后, 关闭浏览器驱动
    def teardown_class(self):
        DriverUtils.set_switch(False)
        DriverUtils.get_driver().get_screenshot_as_file("./screenshot/tpshop.png")
        DriverUtils.quit_driver()

    def test_submit_order(self):
        self.index_page.click_my_cart_link()
        self.cart_page.click_go_to_pay_btn()
        # 地址信息加载慢, 等一会
        time.sleep(8)
        self.order_page.click_submit_btn()
        # 支付页面跳转慢, 也等一会
        time.sleep(5)
        assert "订单提交成功，请您尽快付款！" == self.order_pay_page.get_tips_info()

    def test_pay(self):
        self.index_page.click_my_order_link()
        # 打开新窗口, 需要切换窗口
        self.index_page.switch_window()     # 使用其他page对象调用 switch_window() 方法也是可以的
        self.home_page.click_to_be_pay_link()
        self.home_page.click_pay_btn()
        # 又打开了新窗口
        self.home_page.switch_window()
        self.order_pay_page.click_arrived_pay()
        self.order_pay_page.click_pay_btn()
        # 等待支付结果
        time.sleep(5)
        assert "订单提交成功，我们将在第一时间给你发货！" == self.order_pay_page.get_tips_info()