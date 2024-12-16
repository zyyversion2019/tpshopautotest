import logging
import time

import pytest

from base.base_analyze import analyze_data
from page.index_page import IndexPage
from page.login_page import LoginPage
from utils.driver_utils import DriverUtils


class TestLogin:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.index_page = IndexPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.driver.get("http://localhost/")

    def teardown(self):
        time.sleep(3)
        DriverUtils.quit_driver()

    @pytest.mark.parametrize("params", analyze_data("login_data.json"))
    def test_login(self, params):
        self.index_page.click_login_link()
        logging.info("login with {}--{}--{}".format(params["username"], params["password"], params["code"]))
        self.login_page.input_username(params["username"])
        self.login_page.input_password(params["password"])
        self.login_page.input_verify_code(params["code"])
        self.login_page.click_login_btn()
        # 登录成功需要时间, 暂停几秒等页面跳转
        logging.info("wait 5s for page display")
        time.sleep(5)
        assert params["msg"] in self.driver.title
