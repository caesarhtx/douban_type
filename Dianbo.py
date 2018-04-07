# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 下午9:46
# @Author  : Caesar
# @Email   : Caesarhtx@163.com
# @File    : Dianbo.py
# @Software: PyCharm

import pandas as pd
import re
import Douban_crawl as dbcrawl
import time


def brackets_remover(oldstring):
    noBrackets = re.compile("\(.*?\)")
    newstring = noBrackets.sub('', oldstring)
    nosquare = re.compile("【.*?】")
    newstring = nosquare.sub('', newstring)
    if('：'  in newstring):
        newstring =newstring.split('：')[0]
    return newstring


def date_remover(oldstring):
    if (oldstring[-1].isdigit() and not oldstring[-2].isdigit()):
        oldstring=oldstring[:-1]

    if (oldstring[:2]=='熊出没'):
        oldstring=oldstring[:2]

    if (oldstring[:4]=='星际小蚂蚁'):
        oldstring=oldstring[:4]


    nodate = re.compile("\d\d月\d\d日 ")
    newstring = nodate.sub('',oldstring)
    noseason = re.compile("第.季")
    newstring = noseason.sub('', newstring)
    return newstring


if __name__ == "__main__":
    xlsfile = './sourcedata/dianbo.xlsx'
    df = pd.read_excel(xlsfile, 'dianbo', index_col=None, head=0)

    print(df.head())

    df["节目名称"] = df['节目名称'].apply(lambda x: brackets_remover(x))
    df["节目名称"] = df['节目名称'].apply(lambda x: date_remover(x))

    df["节目类型"] = '-'

    cnt = 0
    for i in df['节目名称']:
        cnt += 1
        print("%stype:%s" % (cnt,'/'.join(dbcrawl.down_the_type(i))))
        df.ix[df['节目名称'] == i, "节目类型"] = '/'.join(dbcrawl.down_the_type(i))
        time.sleep(5)

    with pd.ExcelWriter('purename.xls') as writer:
        df.to_excel(writer, sheet_name='cleandata', index=False)

    print('After:')
    print(df.head())

