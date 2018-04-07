# -*- coding: utf-8 -*-
# @Time    : 2018/3/31 下午2:26
# @Author  : Caesar
# @Email   : Caesarhtx@163.com
# @File    : testdf.py
# @Software: PyCharm

# -*- coding: utf-8 -*-

"""
加载cookies文件，使用requests库爬取数据并动态更新cookies，可以使cookies不失效
"""

import pickle
import time
import requests
import random


class Spider:
    def __init__(self, domain='douban.com'):
        self.headers_douban = {
            'Host': 'erebor.douban.com',
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            'Accept': "*/*",
            'Accept-Language': """zh-CN,zh;q=0.9""",
            'Referer': "https://movie.douban.com/",
            'Connection': 'keep-alive',
            'Accept - Encoding': 'gzip, deflate, br'
        }
        self.s = requests.Session()
        self.s.headers = self.headers_douban
        self.__domain = domain
        self.timeOut = 30
        self.cookies = {}


    def SetLoginDomain(self,domain='douban.com'):
        """设置登录域名"""
        self.__domain = domain
        return self.__domain

    def SetTimeOut(self,timeOut=30):
        self.__timeOut=timeOut
        return self.__timeOut

    def set_cookies(self):
        """读取cookie文件 该文件由另外一个登录程序获取"""
        with open('./cookies.txt') as f:
            cookies = pickle.loads(f.read())
        for cookie in cookies:
            self.cookies[cookie['name']] = cookie['value']
        self.s.cookies.update(self.cookies)

    def open_url(self, url, data=None):
        """页面请求方法"""
        # 请求页面方法
        MaxTryTimes = 20
        waite_time = random.uniform(0, 1)  # 初始化等待时间
        for i in range(MaxTryTimes):
            time.sleep(waite_time)
            try:
                req = self.s.post(url,data=data,headers=self.headers_douban,timeout=self.timeOut)
                content=req.text
                if req.cookies.get_dict():
                    self.s.cookies.update(req.cookies)
                break
            except :
                content = ''
        return content


if __name__ == '__main__':
    spider = Spider()
    spider.set_cookies()
    content = spider.open_url(url='http://ehire.51job.com/Jobs/JobSearchPost.aspx?IsHis=N')
    print(content)