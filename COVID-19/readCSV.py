"""
@ProjectName: Covid-2019
@FileName: readJson.py
@Author: xiao-yi.yu
@Date: 2022/03/09
"""
import csv
from service.json_info import covid_info
import logging

Regions = ["中国", "亚洲", "欧洲", "北美洲", "南美洲", "非洲", "大洋洲"]


logging.basicConfig(filename='read_csv_for_flourish.log',
                    format='%(asctime)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)


def write_csv_title(file, date_list):
    line = 'Country Name, Region, Image URL'
    for date in date_list:
        line = line + "," + date
    file.write(line + '\n')
    file.flush()


def write_csv_data(file, country, date_list, info_list):
    line = country
    country_list = country.split("-")
    if len(country_list) > 1:
        if country_list[0] == "中国":
            line = line + ",亚洲, "
        else:
            line = country_list[1] + "," + country_list[0] + ", "
    else:
        logging.error("海外国家名称异常。应该是[亚洲-新加坡]这样的形式的。但实际是{0}".format(country))
        return

    line = line + get_flourish_data(country, date_list, info_list)
    file.write(line + '\n')
    file.flush()


def get_flourish_data(country, date_list, info_list):
    i = 0
    line = ""
    pre_count = "0"
    for date in date_list:
        i = 0
        for info in info_list:
            if date > info.update_date:
                continue
            if date < info.update_date:
                if i == 0:
                    line += "," + pre_count
                break
            if country == info.name and date == info.update_date:
                count = info.confirmed_count
                pre_count = count
                line += "," + count
                i = 1

    return line


def read_csv_file():
    csv_file = 'D:\\DXY-COVID-19-Data-master\\csv\\2022-03-09\\confirmedCount.csv'

    csv_flourish_confirmed_count = 'D:\\DXY-COVID-19-Data-master\\csv\\2022-03-09\\flourish_confirmedCount.csv'

    confirmed_count_file = open(csv_flourish_confirmed_count, 'w', encoding='utf-8')

    with open(csv_file, "r", encoding="utf-8") as f1:
        f_csv1 = csv.reader(f1)
        column1 = [row[0] for row in f_csv1]
        country_name = sorted(set(column1), key=column1.index)
        new_country_list = []
        for name in country_name:
            country_list = name.split("-")
            region = country_list[0]
            if region in Regions:
                # [亚洲-新加坡]作为国家名称
                # [中国-江苏省]作为国家名称
                new_country_list.append(name)
        logging.debug(new_country_list)

    with open(csv_file, "r", encoding="utf-8") as f2:
        f_csv2 = csv.reader(f2)
        column3 = [row[3] for row in f_csv2]
        date_list = sorted(set(column3), key=column3.index)
        date_list.pop(0)
        logging.debug(date_list)

    write_csv_title(confirmed_count_file, date_list)

    info_list = []
    with open(csv_file, "r", encoding="utf-8") as f3:
        f_csv3 = csv.reader(f3)
        i = 0
        for row in f_csv3:
            if i > 0:
                info = covid_info(row[0], row[2], 0, 0, 0, row[3])
                info_list.append(info)
            else:
                i += 1

    for country in new_country_list:
        # 将疫情数据写入csv文件
        write_csv_data(confirmed_count_file, country, date_list, info_list)

    confirmed_count_file.close()


def main():
    """
        主函数
    """
    read_csv_file()


if __name__ == '__main__':
    main()
