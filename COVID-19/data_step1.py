# 本脚本是针对中国新冠病毒各省市历史发病数据的清洗工具
# 作者 https://github.com/Avens666  mail: cz_666@qq.com
# 源数据来自 https://github.com/BlankerL/DXY-COVID-19-Data/blob/master/csv/DXYArea.csv
# 本脚本将各省市每天的数据进行去重处理，每个省市只保留最新的一条数据 （也可选择保留当天最大数值）
# 因为省市的“疑似数据 suspectedCount”参考意义不大，没有进行处理和导出
# 用户通过修改 inputfile  和  outputfile 定义源数据文件和输出文件

import pandas
from datetime import timedelta
from datetime import datetime

input_file = "data3.13.csv"  # "t15.csv"
output_file = "out1.csv"

# 从这一天开始处理，避免从头处理，提升速度
date_start = datetime(2020, 1, 24, 0, 0)

# pandas显示配置 方便调试
# 显示所有列
pandas.set_option('display.max_columns', None)
# 显示所有行
pandas.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pandas.set_option('max_colwidth', 200)

# ！！！ 根据需要选择合适的字符集
try:
    dataf = pandas.read_csv(input_file, encoding='UTF-8')
except:
    dataf = pandas.read_csv(input_file, encoding='gb2312')

dataf['updateTime'] = pandas.to_datetime(dataf['updateTime'])

# 过滤指定时间之前的数据
# dataf = dataf.loc[(dataf['updateTime'] >= date_start), :]

# 处理一个数据在前一天采集的问题
# for index, data in dataf.iterrows():
#    if "甘肃省" in data['provinceName']:
#        dataf.loc[index, 'updateTime'] += timedelta(hours=3)
dataf['updateTime'] = dataf['updateTime'] + timedelta(hours=3)

dataf['date'] = dataf['updateTime'].apply(lambda x: x.strftime('%Y-%m-%d'))
dataf['date'] = pandas.to_datetime(dataf['date'])
# print(type(dataf))  print(dataf.dtypes)   print(dataf.head())

# 提取省列表
df_t = dataf['provinceName']
df_province = df_t.drop_duplicates()  # 去重 这个返回Series对象
# df_province = df_t.unique()  # 去重 这个返回 ndarray


df = pandas.DataFrame(index=None)

df_t = dataf['date']
df_date = df_t.drop_duplicates()  # 去重 返回Series对象
df_date = df_date.sort_values()

NewList = []

for date_t in df_date:
    for name in df_province:
        print(date_t.strftime('%Y-%m-%d') + name)  # 输出处理进度
        df1 = dataf.loc[(dataf['provinceName'].str.contains(name)) & (dataf['date'] == date_t), :]

# 后面市会筛选，默认每次省的数据为全量数据，不全视为删除
        df1 = df1.loc[(df1['updateTime'] == df1['updateTime'].max()), :]  # 筛出省的最后数据 避免之前时间的市数据干扰，产生孤立值

        df_t = df1['cityName']
        df_city = df_t.drop_duplicates()  # 去重 这个返回Series对象
        province_confirmedCount = df1['province_confirmedCount'].max()
        province_curedCount = df1['province_curedCount'].max()
        province_deadCount = df1['province_deadCount'].max()

        for city in df_city:
            if pandas.isnull(city):
                continue            
            df2 = df1.loc[(df1['cityName'].str.contains(city)), :]  # df2筛选出某个市的数据

            # 使用当天最后时间的数据，注释这行，则使用当天最大值提取数据
            df2 = df2.loc[(df2['updateTime'] == df2['updateTime'].max()), :]

            new = pandas.DataFrame({'省': name,
                                    '省确诊': province_confirmedCount,
                                    '省治愈': province_curedCount,
                                    '省死亡': province_deadCount,
                                    '市': city,
                                    '确诊': df2['city_confirmedCount'].max(),
                                    '治愈': df2['city_curedCount'].max(),
                                    '死亡': df2['city_deadCount'].max(),
                                    '日期': date_t},
                                   pandas.Index(range(1)))
            #            print(new.head())
#            df = df.append(new)
            NewList.append(new)
df = df.append(NewList)

# 补齐一个省的空数据

for date_t in df_date:
    #    print(date_t.strftime('%Y-%m-%d') + name)  # 输出处理进度
    if date_t == df_date.max():  # 最后一天不处理
        continue
    date_add = date_t + timedelta(days=1)
    for name in df_province:
        df1 = df.loc[(df['省'].str.contains(name)) & (df['日期'] == date_t), :]
        if df1.shape[0] > 0:
            df2 = df.loc[
                  (df['省'].str.contains(name)) & (df['日期'] == date_add),
                  :]
            if df2.shape[0] == 0:  # 后面一天省数据为空 把当前数据填到后一天
                print('追加 ' + date_add.strftime('%Y-%m-%d') + name)  # 输出处理进度

                for index, data in df1.iterrows():  # 改变值 使用索引
                    df1.loc[index, '日期'] = date_add
                df = df.append(df1)

# print(df)

df.to_csv(output_file, encoding="utf_8_sig", index=False)  # 为保证excel打开兼容，输出为UTF8带签名格式
