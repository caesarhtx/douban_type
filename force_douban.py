# -*- coding: utf-8 -*-
# @Time    : 2018/4/5 下午9:13
# @Author  : Caesar
# @Email   : Caesarhtx@163.com
# @File    : force_douban.py
# @Software: PyCharm

from selenium import webdriver
import pickle
import os
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

def type_finder(url_login = 'https://www.douban.com/'):

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome('/Users/caesarhtx/Documents/browser/chromedriver', options=chrome_options)
    driver.get(url_login)
    #driver.find_element_by_xpath('//input[@name="form_email"]').send_keys('13122270703')
    #driver.find_element_by_xpath('//input[@name="form_password"]').send_keys('htx123456')
    #driver.find_element_by_xpath('//input[@type="submit" and @value="登录豆瓣"]').click()



    cookie_list = driver.get_cookies()
    # print(cookie_list)
    print('Making new cookies')

    cookie_dict = {}
    for cookie in cookie_list:
        # 写入文件
        f = open('./cookies/'+cookie['name'] + '.douban', 'wb')
        pickle.dump(cookie, f)
        f.close()

        if 'name' in cookie and 'value' in cookie:
            cookie_dict[cookie['name']] = cookie['value']