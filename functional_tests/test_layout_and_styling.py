# from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import skip
import time
import os
import unittest
from .base import FunctionalTest


class LayoutAndSytlingTest(FunctionalTest):
    
    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_text')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )



if __name__ == '__main__':
    unittest.main(warnings='ignore')