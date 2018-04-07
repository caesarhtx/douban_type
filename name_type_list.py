# -*- coding: utf-8 -*-
# @Time    : 2018/4/5 下午9:33
# @Author  : Caesar
# @Email   : Caesarhtx@163.com
# @File    : name_type_list.py
# @Software: PyCharm

import pandas as pd
import os

name_list_file = './sourcedata/name_type.xlsx'


beforedf = pd.DataFrame()
for parent, dirnames, filenames in os.walk('./danpian_result/'):
    for filename in filenames:
        if filename.startswith('danpian'):
            print('processing %s' % filename)
            thisdf = pd.read_excel('./danpian_result/' + filename, 'cleandata', index_col=None, head=0)
            thisdf = thisdf.loc[:, ['影片名称', '节目类型']]
            thisdf = thisdf.drop_duplicates()
            beforedf = beforedf.append(thisdf)
            beforedf = beforedf.drop_duplicates()
    beforedf.to_excel(name_list_file, index=False, columns=['影片名称', '节目类型'], header=False)


