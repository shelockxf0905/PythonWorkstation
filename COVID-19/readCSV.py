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


def get_country_list(csv_file):
    """
        获取所有国家与地球名称
    """
    with open(csv_file, "r", encoding="utf-8") as f1:
        f_csv1 = csv.reader(f1)
        column1 = [row[0] for row in f_csv1]
        country_name_list = sorted(set(column1), key=column1.index)
        new_country_list = []
        for name in country_name_list:
            country_list = name.split("-")
            region = country_list[0]
            if region in Regions:
                # [亚洲-新加坡]作为国家名称
                # [中国-江苏省]作为国家名称
                new_country_list.append(name)
        logging.debug(new_country_list)

    logging.debug("获取全部国家地区名称完了.一共{0}个国家.".format(len(new_country_list)))

    return new_country_list


def get_info_dict(csv_file, date_list, count_type):
    """
        获取元数据字典
    """
    # 元数据字典
    info_dict = {}
    # 同一日期的所有国家元疫情数据
    info_list = []
    # 所有日期的所有国家元疫情数据
    data_list = []

    for date in date_list:
        info_list = get_info_list_by_date(csv_file, date, count_type)
        data_list.append(info_list)
        logging.debug("{0}的数据全部取得完了.一共{1}条数据.".format(date, len(info_list)))

    # 元数据字典做成
    for date, data in zip(date_list, data_list):
        # 以日期为key,以同一日期的疫情数据为value
        info_dict[date] = data

    return info_dict


def get_info_list_by_date(csv_file, date, count_type):
    """
        读取csv元文件
        1.confirmed_count.csv(确诊人数文件)
        2.cured_count.csv(治愈人数文件)
        3.dead_count.csv(死亡人数文件)
        4.dead_rate.csv(死亡率文件)
    """
    info_list = []
    i = 0

    # 读取确诊人数文件
    with open(csv_file, 'r', encoding="utf-8") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            if i > 0:
                # 跳过第一行数据
                if row[3] > date:
                    # 遍历元数据list,之后的数据直接跳出循环,执行下一个日期
                    break
                if row[3] < date:
                    # 遍历元数据list,之前的数据全部过滤
                    continue
                if row[3] == date:
                    # 同一日期的数据做成
                    if count_type == 0:
                        # 确诊人数
                        info = covid_info(row[0], row[2], '0', '0', '0', row[3])
                    elif count_type == 1:
                        # 治愈人数
                        info = covid_info(row[0], '0', row[2], '0', '0', row[3])
                    elif count_type == 2:
                        # 死亡人数
                        info = covid_info(row[0], '0', '0', row[2], '0', row[3])
                    else:
                        # 死亡率
                        info = covid_info(row[0], '0', '0', '0', row[2], row[3])
                    info_list.append(info)
            else:
                i += 1

    return info_list


def get_date_list(csv_file):
    # 获取所有日期,从20200122开始
    with open(csv_file, "r", encoding="utf-8") as f2:
        f_csv2 = csv.reader(f2)
        column3 = [row[3] for row in f_csv2]
        date_list = sorted(set(column3), key=column3.index)
        date_list.pop(0)
        logging.debug(date_list)

    logging.debug("获取全部日期完了.从20200122至今一共{0}天.".format(len(date_list)))

    return date_list


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


def write_csv_data(file, country, date_list, info_dict, count_type):
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
    line = line + get_flourish_data(country, date_list, info_dict, count_type)
    file.write(line + '\n')
    file.flush()


def get_flourish_data(country, date_list, info_dict, count_type):
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
        # 同一日期
        info_list = info_dict[date]
        for info in info_list:
            if country == info.name:
                # 同一国家
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

        if i == 0:
            line += "," + pre_count

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

    # 确诊国家列表
    confirmed_country_list = get_country_list(csv_file)
    # 治愈国家列表
    cured_country_list = get_country_list(csv_file2)
    # 死亡人数国家列表
    dead_country_list = get_country_list(csv_file3)
    # 死亡率国家列表
    rate_country_list = get_country_list(csv_file4)
    # 汇总所有国家地区列表
    all_country_list = confirmed_country_list + cured_country_list + dead_country_list + rate_country_list
    # 汇总所有去重国家地区列表
    all_country_list = sorted(set(all_country_list), key=all_country_list.index)
    logging.debug(all_country_list)
    logging.debug("汇总全部国家地区名称完了.一共{0}个国家或地区.".format(len(all_country_list)))

    # 确诊人数日期列表
    confirmed_date_list = get_date_list(csv_file)
    # 治愈人数日期列表
    cured_date_list = get_date_list(csv_file2)
    # 死亡人数日期列表
    dead_date_list = get_date_list(csv_file3)
    # 死亡率日期列表
    rate_date_list = get_date_list(csv_file4)
    # 汇总所有日期列表
    all_date_list = confirmed_date_list + cured_date_list + dead_date_list + rate_date_list
    # 汇总所有去重日期列表
    all_date_list = sorted(set(all_date_list), key=all_date_list.index)
    logging.debug(all_date_list)
    logging.debug("汇总全部日期完了.从20200122至今一共{0}天.".format(len(all_date_list)))

    # 写入确诊人数文件第一行数据
    write_csv_title(confirmed_count_file, all_date_list)
    # 写入治愈人数文件第一行数据
    write_csv_title(cured_count_file, all_date_list)
    # 写入死亡人数文件第一行数据
    write_csv_title(dead_count_file, all_date_list)
    # 写入死亡率文件第一行数据
    write_csv_title(dead_rate_file, all_date_list)

    logging.debug("第一行数据全部写入完了.")

    confirmed_info_dict = {}
    cured_info_dict = {}
    dead_info_dict = {}
    rate_info_dict = {}

    confirmed_info_dict = get_info_dict(csv_file, all_date_list, 0)
    logging.debug("确诊人数的元数据confirmed_info_dict全部取得完毕.一共有{0}条数据".format(len(confirmed_info_dict)))
    cured_info_dict = get_info_dict(csv_file2, all_date_list, 1)
    logging.debug("治愈人数的元数据cured_info_dict全部取得完毕.一共有{0}条数据".format(len(cured_info_dict)))
    dead_info_dict = get_info_dict(csv_file3, all_date_list, 2)
    logging.debug("死亡人数的元数据dead_info_dict全部取得完毕.一共有{0}条数据".format(len(dead_info_dict)))
    rate_info_dict = get_info_dict(csv_file4, all_date_list, 3)
    logging.debug("死亡率的元数据rate_info_dict全部取得完毕.一共有{0}条数据".format(len(rate_info_dict)))

    for country in all_country_list:
        # 将疫情确诊详细数据写入csv文件
        write_csv_data(confirmed_count_file, country, all_date_list, confirmed_info_dict, 0)
        # 将疫情治愈详细数据写入csv文件
        write_csv_data(cured_count_file, country, all_date_list, cured_info_dict, 1)
        # 将疫情死亡详细数据写入csv文件
        write_csv_data(dead_count_file, country, all_date_list, dead_info_dict, 2)
        # 将疫情死亡率详细数据写入csv文件
        write_csv_data(dead_rate_file, country, all_date_list, rate_info_dict, 3)

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
