import pandas as pd
import os

path = os.getcwd()+'/iOSCompany.csv'

f = open(path, encoding='utf-8')

#从文件获取数据
data = pd.read_csv(f)

#数据预览前5行
#headdata = data.head(5)
#print(headdata)

#数据统计
#des = data.describe()
#print(des)

#获取某行所有的数据
#print(data.ix[1,:])

#获取多行
#print(data.ix[[1,2,3],:])

#通用格式data.ix[行,列]

items = data.ix[1:59,7]
for item in items:
    print(item)