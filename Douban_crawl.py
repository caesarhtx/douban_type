# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 下午4:17
# @Author  : Caesar
# @Email   : Caesarhtx@163.com
# @File    : Douban_crawl.py
# @Software: PyCharm
# 爬取豆瓣类型

import requests
from bs4 import BeautifulSoup
import giveproxy as gp
import random
from cookie_maker import get_cookie

def download_page(url):
    proxies_list = [
        {'http': 'http://110.72.20.80:8123'},
        {'http': 'http://117.64.224.129:18118'},
        {'http': 'http://60.168.206.120:18118'}

    ]
    # 伪装浏览器
    headers = [
        {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50 '}
    ]
    mycook = get_cookie()
    proxy = random.choice(proxies_list)
    header = random.choice(headers)

    try:
        data = requests.get(url, headers=header, proxies=proxy, cookies=mycook).text
        return data
    except:
        return download_page(url)


'''''   解析html  '''


def parse_search(html):
    soup = BeautifulSoup(html, "html.parser")
    movie_soup = soup.find('div', attrs={'class': 'result'})
    movie_cooksoup = movie_soup.find('div', attrs={'class': 'content'}).find('div', attrs={'class': 'title'}).h3.a['href']
    return movie_cooksoup


def what_genre(search_url):
    soup = BeautifulSoup(search_url, "html.parser")
    genre_soup = soup.find_all('span', attrs={'property': 'v:genre'})
    genre_list = []
    for each_soup in genre_soup:
        genre_list.append(each_soup.string)
    return genre_list


def down_the_type(name):
    DownLoad_url = 'https://www.douban.com/search?cat=1002&q=%s' % name
    try:
        search_result = parse_search(download_page(DownLoad_url))
    except:
        return ['-']
    return what_genre(download_page(search_result))

def danpian_type(name):
    DownLoad_url = 'https://www.douban.com/search?cat=1002&q=%s' % name
    try:
        danpian_html = download_page(DownLoad_url)
        soup = BeautifulSoup(danpian_html, "html.parser")
        danpianType = soup.find('div', attrs={'class': 'meta abstract'})


    except:
        return ['-']
    return danpianType


if __name__ == '__main__':
    a = down_the_type('海底小纵队')
    print(a)

