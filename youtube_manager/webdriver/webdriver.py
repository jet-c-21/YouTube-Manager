# coding: utf-8
"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 4/18/23
"""
from selenium import webdriver
from selenium.webdriver import Chrome
import chromedriver_autoinstaller


def get_webdriver(chrome_options=None) -> Chrome:
    chromedriver_autoinstaller.install()
    return webdriver.Chrome(options=chrome_options)
