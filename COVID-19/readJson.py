"""
@ProjectName: Covid-2019
@FileName: readJson.py
@Author: xiao-yi.yu
@Date: 2020/04/28
"""
import json
import time
from service.json_info import covid_info
import logging


def write_csv_title(file, file_name):
    """
        写入新冠疫情csv文件的第一行数据
    """
    line = 'name,type,value,date'
    logging.debug(file_name + ' csv title:' + line)
    file.write(line + '\n')
    file.flush()


def time_to_date(time_num):
    """
        将time时间变换为“2022-03-08”这种形式
    """
    time_temp = float(time_num / 1000)
    current_date = time.localtime(time_temp)
    date_ymd = time.strftime("%Y-%m-%d", current_date)
    return date_ymd


def clean_same_item(list):
    """
        除去相同项，取出最大项
    """
    # 最终形成的list
    new_list = []
    # 相同项的累计确诊数list
    confirmed_count_list = []
    # 相同项的治愈病例数list
    cured_count_list = []
    # 相同项的死亡病例数list
    dead_count_list = []
    # 相同项的死亡率list
    dead_rate_list = []

    max_len = len(list)
    i = 0
    j = 0
    # 遍历整个list
    while i < max_len:
        item = list[i]
        # 先保存第i项的数据
        if item.confirmed_count and int(item.confirmed_count) > 0:
            # 判断item_i中有确诊人数
            confirmed_count_list.append(item.confirmed_count)
        if item.cured_count and int(item.cured_count) > 0:
            # 判断item_i中有治愈人数
            cured_count_list.append(item.cured_count)
        if item.dead_count and int(item.dead_count) > 0:
            # 判断item_i中有死亡人数
            dead_count_list.append(item.dead_count)
        if item.dead_rate and float(item.dead_rate) > 0:
            # 判断item_i中有死亡率
            dead_rate_list.append(item.dead_rate)
        j = i + 1
        # 与下一个item进行比较
        while j < max_len:
            j_item = list[j]
            # 同一项目的判定
            if item.name == j_item.name and item.update_date == j_item.update_date:
                if j_item.confirmed_count and int(j_item.confirmed_count) > 0:
                    # # 判断item_j中有确诊人数
                    confirmed_count_list.append(j_item.confirmed_count)
                if j_item.cured_count and int(j_item.cured_count) > 0:
                    # 判断item_j中有治愈人数
                    cured_count_list.append(j_item.cured_count)
                if j_item.dead_count and int(j_item.dead_count) > 0:
                    # 判断item_j中有死亡人数
                    dead_count_list.append(j_item.dead_count)
                if j_item.dead_rate and float(j_item.dead_rate) > 0:
                    # 判断item_j中有死亡率
                    dead_rate_list.append(j_item.dead_rate)
                list.remove(j_item)
                max_len = max_len - 1
            else:
                if item.update_date < j_item.update_date:
                    # 如果是第二天数据就跳出二层循环，一层循环继续
                    break
                j += 1
        # 设定list中的最大值
        if len(confirmed_count_list) > 0:
            item.confirmed_count = max(confirmed_count_list)
        if len(cured_count_list) > 0:
            item.cured_count = max(cured_count_list)
        if len(dead_count_list) > 0:
            item.dead_count = max(dead_count_list)
        if len(dead_rate_list) > 0:
            item.dead_rate = max(dead_rate_list)
        new_list.append(item)
        i += 1
        logging.debug('''new_list item
name={}, 
confirmed_count={}, 
cured_count={}, 
dead_count={}, 
dead_rate={},  
update_date={}'''.format(item.name, item.confirmed_count, item.cured_count, item.dead_count, item.dead_rate,
                         item.update_date))
        confirmed_count_list.clear()
        cured_count_list.clear()
        dead_count_list.clear()
        dead_rate_list.clear()

    return new_list


def set_default_count(count):
    """
        设定默认返回值
    """
    if count:
        return count
    else:
        return 0


def read_json_file():
    """
        读取json文件(DXYArea.json)
    """
    json_filename = 'D:\\yuxiaoyi\\2022-03-09\\DXYArea.json'
    # 新冠疫情确诊总人数
    csv_confirmed_count = 'D:\\DXY-COVID-19-Data-master\\csv\\2022-03-09\\confirmedCount.csv'
    # 新冠疫情治愈总人数
    csv_cured_count = 'D:\\DXY-COVID-19-Data-master\\csv\\2022-03-09\\cured_count.csv'
    # 新冠疫情死亡总人数
    csv_dead_count = 'D:\\DXY-COVID-19-Data-master\\csv\\2022-03-09\\dead_count.csv'
    # 新冠疫情死亡率
    csv_dead_rate = 'D:\\DXY-COVID-19-Data-master\\csv\\2022-03-09\\dead_rate.csv'
    # 新冠疫情确诊人数文件
    confirmed_count_file = open(csv_confirmed_count, 'w', encoding='utf-8')
    # 新冠疫情治愈人数文件
    cured_count_file = open(csv_cured_count, 'w', encoding='utf-8')
    # 新冠疫情死亡人数文件
    dead_count_file = open(csv_dead_count, 'w', encoding='utf-8')
    # 新冠疫情死亡率文件
    dead_rate_file = open(csv_dead_rate, 'w', encoding='utf-8')
    # 写入新冠疫情确诊人数文件的第一行数据
    write_csv_title(confirmed_count_file, 'csv_confirmed_count_file')
    # 写入新冠疫情治愈人数文件的第一行数据
    write_csv_title(cured_count_file, 'csv_cured_count_file')
    # 写入新冠疫情死亡人数文件的第一行数据
    write_csv_title(dead_count_file, 'csv_dead_count_file')
    # 写入新冠疫情死亡率文件的第一行数据
    write_csv_title(dead_rate_file, 'csv_dead_rate_file')

    info_list = []
    with open(json_filename, 'r', encoding='utf-8') as load_f:
        # 载入json文件全部内容
        json_info = json.loads(load_f.read())
        for item_info in json_info:
            # 洲名
            continent_name = ''
            # 省名
            province_name = ''
            # 国家名
            country_name = ''
            # 确诊人数
            confirmed_count = 0
            # 治愈人数
            cured_count = 0
            # 死亡人数
            dead_count = 0
            # 死亡率
            dead_rate = 0.0
            # [欧洲-葡萄牙]的格式变换
            # [中国-上海]的格式变换
            name = ''
            # 更新日期
            update_date = ''

            if 'cities' not in item_info:
                # 国外
                # 洲名
                if 'continentName' in item_info:
                    continent_name = item_info['continentName']
                else:
                    continent_name = item_info['countryName']
                # 国家名
                province_name = item_info['provinceName']
                # 累计确诊数
                confirmed_count = set_default_count(item_info['confirmedCount'])
                # 治愈病例数
                cured_count = set_default_count(item_info['curedCount'])
                # 死亡病例数
                dead_count = set_default_count(item_info['deadCount'])
                # 死亡率
                if 'deadRate' in item_info:
                    dead_rate = float(set_default_count(item_info['deadRate']))
                # [欧洲-葡萄牙]的格式变换
                name = str(continent_name) + "-" + str(province_name)
            else:
                # 国内
                # 中国
                country_name = item_info['countryName']
                # 城市名
                province_name = item_info['provinceName']
                # 累计确诊数
                confirmed_count = set_default_count(item_info['confirmedCount'])
                # 治愈病例数
                cured_count = set_default_count(item_info['curedCount'])
                # 死亡病例数
                dead_count = set_default_count(item_info['deadCount'])
                # 国内没有这个数据
                if confirmed_count and dead_count:
                    dead_rate = dead_count/confirmed_count * 100.00
                # [中国-上海]的格式变换
                name = str(country_name) + "-" + str(province_name)
            # 更新时间
            update_time = item_info['updateTime']
            # 转换成yyyy-mm-dd格式
            update_date = time_to_date(update_time)

            info = covid_info(name, confirmed_count, cured_count, dead_count, dead_rate, update_date)
            info_list.append(info)
            logging.debug('''
name={}, 
confirmed_count={}, 
cured_count={}, 
dead_count={}, 
dead_rate={}, 
update_date={} 
update_time={}'''.format(name, confirmed_count, cured_count, dead_count, dead_rate, update_date, update_time))
    # 列表反转
    info_list.reverse()

    logging.debug('info_list len =%s' % (len(info_list)))

    new_info_list = clean_same_item(info_list)

    logging.debug('new_info_list len =%s' % (len(new_info_list)))

    for i in range(len(new_info_list)):
        info = new_info_list[i]
        # 累计确诊数csv文件出力
        if info.confirmed_count and int(info.confirmed_count) > 0:
            info.write_csv_confirmed_count_file(confirmed_count_file)
        # 治愈病例数csv文件出力
        if info.cured_count and int(info.cured_count) > 0:
            info.write_csv_cured_count_file(cured_count_file)
        # 死亡病例数csv文件出力
        if info.dead_count and int(info.dead_count) > 0:
            info.write_csv_dead_count_file(dead_count_file)
        # 死亡率csv文件出力
        if info.dead_rate and float(info.dead_rate) > 0.0:
            info.write_csv_dead_rate_file(dead_rate_file)
    confirmed_count_file.close()
    cured_count_file.close()
    dead_count_file.close()
    dead_rate_file.close()


def main():
    """
        主函数
    """
    # 读取json文件(DXYArea.json)
    read_json_file()


if __name__ == '__main__':
    main()
