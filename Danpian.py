# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 下午2:35
# @Author  : Caesar
# @Email   : Caesarhtx@163.com
# @File    : test.py
# @Software: PyCharm

import pandas as pd
import Douban_crawl as dbcrawl
import time
from Dianbo import brackets_remover, date_remover

groupby = 200

if __name__=="__main__":
    xlsfile = './sourcedata/danpian.xlsx'
    nrow = int(input('请输入开始行数'))
    check_frame = pd.read_excel('./sourcedata/name_type.xlsx', 'Sheet1', index_col=None, header=None)
    check_frame = check_frame.drop_duplicates()
    df = pd.read_excel(xlsfile, 'danpian', index_col=None, head=0)
    df = df.loc[nrow:]
    print(df.head())

    df["影片名称"] = df['影片名称'].apply(lambda x: brackets_remover(x))
    df["影片名称"] = df['影片名称'].apply(lambda x: date_remover(x))

    df["节目类型"] = '-'

    cnt = nrow
    name_of_200 = []

    alarm = []
    for i in df['影片名称']:

        if(i in list(check_frame[0])):
            cnt += 1
            type_str = check_frame.ix[check_frame[0] == i].reset_index(drop=True).loc[0, 1]
            df.ix[df['影片名称'] == i, "节目类型"] = type_str

            print("No.%s type:%s" % (cnt, type_str))

        elif(i in name_of_200):
            cnt += 1
            type_str = df.ix[df['影片名称'] == i].reset_index(drop=True).loc[0, '节目类型']
            df.ix[df['影片名称'] == i, "节目类型"] = type_str

            print("No.%s type:%s" % (cnt, type_str))
        else:
            print('search from internet...')
            cnt += 1
            thistype = dbcrawl.down_the_type(i)
            if(thistype == '-'):
                alarm.append(0)
                if(alarm[-7:len(alarm)]==[0, 0, 0, 0, 0, 0, 0]):
                    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!\n!!!!')
            else:
                alarm.append(1)
            print("name:%s,  No.%s type:%s" % (i, cnt, '/'.join(thistype)))
            df.ix[df['影片名称'] == i, "节目类型"] = '/'.join(thistype)
            name_of_200.append(i)
            time.sleep(5)
        if(cnt%groupby==0):
            print('Writing......danpian_%s-%s' % (cnt-groupby, cnt-1))
            thisdf = df.loc[cnt - groupby: cnt - 1]
            name_of_200 = []
            alarm=[]
            check_frame = check_frame.append(thisdf.loc[:, ['影片名称', '节目类型']].rename(columns={'影片名称': 0, '节目类型': 1}))
            check_frame = check_frame.drop_duplicates()
            with pd.ExcelWriter('./sourcedata/name_type.xlsx') as checker:
                check_frame.to_excel(checker, sheet_name='Sheet1', index=False)
            with pd.ExcelWriter('./danpian_result/danpian_%s-%s.xls' % (cnt-groupby, cnt-1)) as writer:
                thisdf.to_excel(writer, sheet_name='cleandata', index=False)
        if(cnt==10209):
            print('Writing......danpian_%s-%s' % (cnt-groupby, cnt-1))
            thisdf = df.loc[cnt - groupby: cnt - 1]
            name_of_200 = []
            alarm=[]
            check_frame = check_frame.append(thisdf.loc[:, ['影片名称', '节目类型']].rename(columns={'影片名称': 0, '节目类型': 1}))
            check_frame = check_frame.drop_duplicates()
            with pd.ExcelWriter('./sourcedata/name_type.xlsx') as checker:
                check_frame.to_excel(checker, sheet_name='Sheet1', index=False)
            with pd.ExcelWriter('./danpian_result/danpian_%s-%s.xls' % (cnt-groupby, cnt-1)) as writer:
                thisdf.to_excel(writer, sheet_name='cleandata', index=False)


