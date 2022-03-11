"""
    作者：xiao-yi.yu
    日期：2019/10/11
    功能：AQI计算
    版本：1.0
"""
import csv
import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

# 设置字体为Microsoft YaHei显示中文
plt.rcParams['font.family'] = 'Microsoft YaHei'
# 更新字体格式
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['font.size'] = 9
plt.rcParams['axes.unicode_minus'] = False


def get_city_aqi(city_pinyin):
    """
        获取城市的AQI
    """
    url = 'http://www.86kongqi.com/city/' + city_pinyin + '.html'
    r = requests.get(url, timeout=30)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')

    div_list = soup.find_all('div', {'class': 'weilai'})

    td_aqi = []
    city_aqi = []

    if len(div_list) > 0:
        div_content = div_list[0]
        td_list = div_content.find_all('td')
        if td_list is not None and len(td_list) > 0:
            for td in td_list:
                td_val = td.text.strip()
                if td_val.isnumeric() and td_val != '四零三':
                    td_val_int = eval(td_val)
                    td_aqi.append(td_val_int)

            aqi = math.floor(np.mean(td_aqi))
            city_aqi.append(aqi)
    return city_aqi


def get_all_cities():
    """


        获取所有城市
    """
    url = 'http://www.86kongqi.com/'
    city_list = []

    r = requests.get(url, timeout=30)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text[5:], 'html.parser')

    city_div_list = soup.find_all('div', {'class': 'aqi-site'})
    if len(city_div_list) < 2:
        print('获取所有城市异常!(没有找到任何城市)')
        return None
    city_div = city_div_list[1]
    city_link_list = city_div.find_all('a')

    for city_link in city_link_list:
        city_name = city_link.text
        city_str = city_link['href']
        index = city_str.find('.html')
        if index < 2:
            print('获取所有城市异常!(.html没有找到)')
            return None
        city_pinyin = city_str[5:index]
        if (city_name, city_pinyin) not in city_list:
            city_list.append((city_name, city_pinyin))
    return city_list


def main():
    """
        主函数
    """
    city_list = get_all_cities()
    if city_list is None:
        return
    header = ['City', 'PINYIN', 'AQI']

    with open('aqi_china_cities.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        count = len(city_list)
        for i, city in enumerate(city_list):
            if (i + 1) % 10 == 0:
                print('已处理{}条记录。(共{}条记录)'.format(i + 1, count))

            city_name = city[0]
            city_pinyin = city[1]
            city_aqi = get_city_aqi(city_pinyin)
            if city_aqi is not None and len(city_aqi) > 0 and city_aqi[0] > 0:
                row = [city_name] + [city_pinyin] + city_aqi
                writer.writerow(row)
            else:
                print('中国{0}-{1}的AQI值取得失败!'.format(city_name, city_pinyin))

    print('记录全部处理完毕。一共处理{}条记录。'.format(count))

    aqi_data = pd.read_csv('aqi_china_cities.csv')
    print('基本信息：')
    print(aqi_data.info())

    print('数据预览：')
    print(aqi_data.head())

    clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]

    # 基本统计
    print('AQI最大值:', clean_aqi_data['AQI'].max())
    print('AQI最小值：', clean_aqi_data['AQI'].min())
    print('AQI均值：', clean_aqi_data['AQI'].mean())

    # top50
    top50_cities = clean_aqi_data.sort_values(by=['AQI']).head(50)
    top50_cities.plot(kind='bar', x='City', y='AQI', title='空气质量最好的50个城市',
                      figsize=(20, 10))
    plt.savefig('top50_aqi_bar.png')
    plt.show()


if __name__ == '__main__':
    main()
