"""
@ProjectName: 爬取链家房屋信息
https://sh.lianjia.com/ershoufang/pg{0}/
@FileName: GetLianjia.py
@Author: xiao-yi.yu
@Date: 2023/03/14
"""
import requests
import parsel
import csv
import time
import random

count = 0
for page in range(1, 100+1):
    print('=======================正在爬取第{0}页的数据======================================'.format(page))
    choice = random.randint(0, 5)
    # url1 = 'https://sh.fang.lianjia.com/loupan/'
    url2 = 'https://sh.lianjia.com/ershoufang/pg{0}/'.format(str(page))

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/86.0.4240.198 Safari/537.36'}
    res = requests.get(url2, headers)
    html_data = res.text
    selector = parsel.Selector(html_data)
    lst = selector.css('.clear.LOGCLICKDATA')  # 30个li
    for li in lst:
        title = li.css('.title a::text').get()  # 标题
        positionInfo_list = li.css('.positionInfo a::text').getall()  # 地址信息
        positionInfo = ','.join(positionInfo_list)
        houseInfo = li.css('.houseInfo::text').get()  # 房屋信息
        followInfo = li.css('.followInfo::text').get()  # 关注人数与发布时间
        tags = li.css('.tag span::text').getall()  # 房屋标签
        tags = ','.join(tags)
        totalPrice = li.css('.totalPrice.totalPrice2 span::text').get() + '万元'  # 房屋总价
        unitPrice = li.css('.unitPrice span::text').get()  # 房屋单价
        title_url = li.css('.title a::attr(href)').get()  # 标题url

        count += 1
        print('链家_上海_二手房数据{0}:{1},地址信息={2}, 房屋信息={3}, 关注人数与发布时间={4}, 房屋总价={5}, 房屋单价={6}'.
              format(count, title, positionInfo, houseInfo, followInfo, totalPrice, unitPrice))

        with open('lianjia_shanghai_ershoufang.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow((title, positionInfo, houseInfo, followInfo, tags, totalPrice, unitPrice, title_url))

        time.sleep(choice)
