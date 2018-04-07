# -*- coding: utf-8 -*-
# @Time    : 2018/4/4 下午2:17
# @Author  : Caesar
# @Email   : Caesarhtx@163.com
# @File    : cookie_maker.py
# @Software: PyCharm

from selenium import webdriver
import pickle
import os
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
def cookie_maker(url_login = 'https://www.douban.com/'):

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome('/Users/caesarhtx/Documents/browser/chromedriver',options=chrome_options)
    driver.get(url_login)
    # driver.find_element_by_xpath('//input[@name="form_email"]').send_keys('13122270703')
    # driver.find_element_by_xpath('//input[@name="form_password"]').send_keys('htx123456')
    # driver.find_element_by_xpath('//input[@type="submit" and @value="登录豆瓣"]').click()


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

    return cookie_dict


def get_cookie_from_cache():

    cookie_dict = {}
    for parent, dirnames, filenames in os.walk('./cookies/'):
        for filename in filenames:
            if filename.endswith('.douban'):
                # print(filename)
                with open('./cookies/' + filename, 'rb') as f:
                    d = pickle.load(f)

                    if 'name'in d and 'value' in d and 'expiry' in d:
                        expiry_date = int(d['expiry'])
                        if expiry_date > int(time.time()):
                            cookie_dict[d['name']] = d['value']
                        else:
                            return {}

    return cookie_dict


def get_cookie():
    cookie_dict = get_cookie_from_cache()
    if not cookie_dict:
        cookie_dict = cookie_maker()

    return cookie_dict


if __name__ == "__main__":
    cookdic = get_cookie()
    search_url = 'https://movie.douban.com/subject/4920389/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
    timeout = 5
    r = requests.get(search_url, headers=headers, cookies=cookdic, timeout=timeout)

    soup = BeautifulSoup(r.text, "html.parser")
    genre_soup = soup.find_all('span', attrs={'property': 'v:genre'})
    genre_list = []
    for each_soup in genre_soup:
        genre_list.append(each_soup.string)
    print(genre_list)
