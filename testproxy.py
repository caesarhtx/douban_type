# -*- coding: utf-8 -*-
# @Time    : 2018/3/30 上午12:25
# @Author  : Caesar
# @Email   : Caesarhtx@163.com
# @File    : testproxy.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import giveproxy as gp

def download_page(realurl):
    url = 'http://www.xicidaili.com/nn/'
    # 伪装浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.132 Safari/537.36'}
    ip_list = gp.get_ip_list(url, headers=headers)
    proxies = gp.get_random_ip(ip_list)
    print(proxies)
    data = requests.get(realurl, headers=headers, proxies=proxies).text
    return data


'''''   解析html  '''


def parse_search(html):
    soup = BeautifulSoup(html, "html.parser")
    movie_soup = soup.find('div', attrs={'class': "div_main", 'style': "text-align:center;"})

    movie_cooksoup = movie_soup.find('font', attrs={'style': "font-family:Arial,Helvetica,Sans Serif;font-size: 24pt;"}).b

    return movie_cooksoup


def main(text):
    with open('html.txt', 'w') as html_doc:
        html_doc.write(text)


if __name__ == '__main__':
    url = "http://www.myip.cn/"
    htmldata = download_page(url)
    #print(htmldata)
    a = parse_search(htmldata)
    print(a)



