# -*- coding:utf-8 -*-


import unittest
import sys

sys.path.append("../")
from tools.unit_StartEnd import StartEnd
from businessView.loginView import LoginView
import logging

class TestLogin(StartEnd):


    def test_Login_True(self):
        logging.info("========login true user password========")
        login = LoginView(self.driver)
        login.login_action('18403558945','111111Qq')
        self.assertEqual(1, 1)

    def test_login_error(self):
        logging.info("========login false user password========")
        login = LoginView(self.driver)
        login.login_action("18403558946","111111Qq")
        self.assertEqual(1, 2)

    



if __name__ == '__main__':
    unittest.main()




