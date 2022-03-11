"""
    作者：xiao-yi.yu
    版本：1.0
    日期：2019/09/26
    功能：输入某年某月某日，判断这一天是这一年的第几天？
"""
from datetime import datetime

def is_leap_year(year):
    """
        判断year是否为闰年
        是，返回True
        否，返回False
    """
    is_leap = False

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True

    return is_leap

def main():
    """
        主函数
    """
    input_date_str = input('请输入日期(yyyy/mm/dd)：')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')
    print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day

    # # 计算之前月份天数的总和以及当前月份天数
    # days_in_month_tup = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    # # print(days_in_month_tup[: month - 1])
    # days = sum(days_in_month_tup[: month - 1]) + day
    #
    # # 判断闰年
    # if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    #     if month > 2:
    #         days += 1

    # print('这是第{}天。'.format(days))

    # 计算之前月份天数的总和以及当前月份天数
    # days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # if is_leap_year(year):
    #     days_in_month_list[1] = 29
    # days = sum(days_in_month_list[: month - 1]) + day
    #
    # print('这是{}年的第{}天。'.format(year, days))

    # 包含30天 月份集合
    # _30_days_month_set = {4, 6, 9, 11}
    # _31_days_month_set = {1, 3, 5, 7, 8, 10, 12}
    #
    # # 初始化值
    # days = 0
    # days += day
    #
    # for i in range(1, month):
    #     if i in _30_days_month_set:
    #         days += 30
    #     elif i in _31_days_month_set:
    #         days += 31
    #     else:
    #         days += 28
    #
    # if is_leap_year(year) and month > 2:
    #     days += 1
    #
    # print('这是{}年的第{}天。'.format(year, days))

    # 月份-天数 字典
    month_day_dict = {1: 31,
                      2: 28,
                      3: 31,
                      4: 30,
                      5: 31,
                      6: 30,
                      7: 31,
                      8: 31,
                      9: 30,
                      10: 31,
                      11: 30,
                      12: 31}

    day_month_dict = {30: {4, 6, 9, 11},
                      31: {1, 3, 5, 7, 8, 10, 12}}

    # 初始化值
    days = 0
    days += day

    for i in range(1, month):
        days += month_day_dict[i]

    if is_leap_year(year) and month > 2:
        days += 1

    print('这是{}年的第{}天。'.format(year, days))

if __name__ == '__main__':
    main()
