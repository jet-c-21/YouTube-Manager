# coding: utf-8
"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 5/31/23
"""
import time
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from .webdriver.webdriver import get_webdriver


def get_channel_id_from_url(channel_url: str):
    options = Options()
    options.add_argument("--headless")  # Ensure GUI is off
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    webdriver = get_webdriver(chrome_options=options)
    webdriver.get(channel_url)
    html = webdriver.page_source
    webdriver.close()
    doc = pq(html)

    link_el = doc('link[rel="canonical"]')
    url_with_channel_id = link_el.attr('href')
    url_with_channel_id: str
    channel_id = url_with_channel_id.replace('https://www.youtube.com/channel/', '')
    return channel_id
