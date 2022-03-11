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
    """
        写入csv的第一行数据
        如以下的形式
        Country Name, Region, Image URL,2020-01-22,2020-01-23,2020-01-24,2020-01-25,2020-01-26...
    """
    line = 'Country Name, Region, Image URL'
    for date in date_list:
        line = line + "," + date
    file.write(line + '\n')
    file.flush()


def write_csv_data(file, country, date_list, info_list, count_type):
    """
        写入csv数据
        如以下的形式
        中国-湖南省,亚洲, ,
    """
    line = country
    country_list = country.split("-")
    if len(country_list) > 1:
        if country_list[0] == "中国":
            # 判断是中国,洲名自动补全
            line = line + ",亚洲, "
        else:
            # 判断是国外,[英国,欧洲,]的形式
            line = country_list[1] + "," + country_list[0] + ", "
    else:
        logging.error("海外国家名称异常。应该是[亚洲-新加坡]这样的形式的。但实际是{0}".format(country))
        return
    # 组成疫情的详细数据
    line = line + get_flourish_data(country, date_list, info_list, count_type)
    file.write(line + '\n')
    file.flush()


def get_flourish_data(country, date_list, info_list, count_type):
    """
        写入疫情每日的详细数据
        20200122-至今
    """
    i = 0
    line = ""
    # 前一次数据
    pre_count = "0"

    for date in date_list:
        i = 0
        for info in info_list:
            if date > info.update_date:
                # 遍历元数据list,之前的数据全部过滤
                continue
            if date < info.update_date:
                # 遍历元数据list,之后的数据直接跳出循环,执行下一个日期
                if i == 0:
                    # 如果遍历元数据list,没有相应的数据,就用前一个数据填补
                    line += "," + pre_count
                break
            if country == info.name and date == info.update_date:
                # 国家名与更新日期相同,才赋予数据
                # 中国-湖南省 == 中国-湖南省
                # 非洲-尼日利亚 == 非洲-尼日利亚
                # 拼接一行长疫情详细数据
                if count_type == 0:
                    # 确诊人数
                    count = info.confirmed_count
                elif count_type == 1:
                    # 治愈人数
                    count = info.cured_count
                elif count_type == 2:
                    # 死亡人数
                    count = info.dead_count
                elif count_type == 3:
                    # 死亡率
                    count = info.dead_rate
                pre_count = count
                line += "," + count
                i = 1

    return line


def read_csv_file():
    """
        读入新冠疫情csv元数据(20200122开始)
        1.确诊人数
        2.治愈人数
        3.死亡人数
        4.死亡率
    """
    # 确诊人数
    csv_file = 'D:\\DXY-COVID-19-Data-master\\csv\\2022-03-09\\confirmed_count.csv'
    # 治愈人数
    csv_file2 = 'D:\\DXY-COVID-19-Data-master\\csv\\2022-03-09\\cured_count.csv'
    # 死亡人数
    csv_file3 = 'D:\\DXY-COVID-19-Data-master\\csv\\2022-03-09\\dead_count.csv'
    # 死亡率
    csv_file4 = 'D:\\DXY-COVID-19-Data-master\\csv\\2022-03-09\\dead_rate.csv'

    csv_flourish_confirmed_count = 'D:\\DXY-COVID-19-Data-master\\csv\\2022-03-09\\flourish_confirmedCount.csv'
    csv_flourish_cured_count = 'D:\\DXY-COVID-19-Data-master\\csv\\2022-03-09\\flourish_curedCount.csv'
    csv_flourish_dead_count = 'D:\\DXY-COVID-19-Data-master\\csv\\2022-03-09\\flourish_deadCount.csv'
    csv_flourish_dead_rate = 'D:\\DXY-COVID-19-Data-master\\csv\\2022-03-09\\flourish_deadRate.csv'

    # 确诊人数文件
    confirmed_count_file = open(csv_flourish_confirmed_count, 'w', encoding='utf-8')
    # 治愈人数文件
    cured_count_file = open(csv_flourish_cured_count, 'w', encoding='utf-8')
    # 死亡人数文件
    dead_count_file = open(csv_flourish_dead_count, 'w', encoding='utf-8')
    # 死亡率文件
    dead_rate_file = open(csv_flourish_dead_rate, 'w', encoding='utf-8')

    # 获取所有国家与地球名称
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

    logging.debug("获取全部国家地区名称完了.")

    # 获取所有日期,从20200122开始
    with open(csv_file, "r", encoding="utf-8") as f2:
        f_csv2 = csv.reader(f2)
        column3 = [row[3] for row in f_csv2]
        date_list = sorted(set(column3), key=column3.index)
        date_list.pop(0)
        logging.debug(date_list)

    logging.debug("获取全部日期完了.")

    # 写入确诊人数文件第一行数据
    write_csv_title(confirmed_count_file, date_list)
    # 写入治愈人数文件第一行数据
    write_csv_title(cured_count_file, date_list)
    # 写入死亡人数文件第一行数据
    write_csv_title(dead_count_file, date_list)
    # 写入死亡率文件第一行数据
    write_csv_title(dead_rate_file, date_list)

    logging.debug("第一行数据全部写入完了.")

    info_list = []
    # 读取确诊人数文件
    confirmed_reader = csv.reader(open(csv_file, 'r', encoding="utf-8"))
    # 读取治愈人数文件
    cured_reader = csv.reader(open(csv_file2, 'r', encoding="utf-8"))
    # 读取死亡人数文件
    dead_reader = csv.reader(open(csv_file3, 'r', encoding="utf-8"))
    # 读取死亡率文件
    rate_reader = csv.reader(open(csv_file4, 'r', encoding="utf-8"))

    i = 0
    for (row, cured, dead, rate) in zip(confirmed_reader, cured_reader, dead_reader, rate_reader):
        if i > 0:
            info = covid_info(row[0], row[2], cured[2], dead[2], rate[2], row[3])
            info_list.append(info)
        else:
            i += 1

    logging.debug("元数据info_list全部组建完毕.")

    for country in new_country_list:
        # 将疫情确诊详细数据写入csv文件
        write_csv_data(confirmed_count_file, country, date_list, info_list, 0)
        # 将疫情治愈详细数据写入csv文件
        write_csv_data(cured_count_file, country, date_list, info_list, 1)
        # 将疫情死亡详细数据写入csv文件
        write_csv_data(dead_count_file, country, date_list, info_list, 2)
        # 将疫情死亡率详细数据写入csv文件
        write_csv_data(dead_rate_file, country, date_list, info_list, 3)

    logging.debug("疫情确诊详细数据写入完毕.")
    logging.debug("疫情治愈详细数据写入完毕.")
    logging.debug("疫情死亡详细数据写入完毕.")
    logging.debug("疫情死亡率详细数据写入完毕.")

    # 关闭文件
    confirmed_count_file.close()
    cured_count_file.close()
    dead_count_file.close()
    dead_rate_file.close()

    logging.debug("所有csv文件全部关闭.")
    logging.debug("处理全部结束.")


def main():
    """
        主函数
    """
    logging.debug("读取csv文件开始")
    read_csv_file()


if __name__ == '__main__':
    main()
