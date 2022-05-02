"""
@ProjectName: 计算股票收益率
@FileName: cal_stocks_profit.py
@Author: xiao-yi.yu
@Date: 2020/09/15
"""
import openpyxl
from stocks.stock_info import stock_info
import logging

money_unit = '元'
sheet_title = ["证券代码", "证券名称", "成交日期", "买入价格", "买入股数", "买入金额", "买入手续费", "买入印花税", "买入其他杂费"
               "卖出价格", "卖出股数", "卖出金额", "卖出手续费", "卖出印花税", "卖出其他杂费", "交易市场", "交易成本", "净利润",
               "净利润率"]
file_name = "D:\\yuxiaoyi\\2022-03-14\\A股历史成交明细.xlsx"


def get_stock_info_dict(stock_sheet):
    # 股票信息字典
    stock_info_dict = {}
    # 股票列表
    stock_list = []
    # 市场list
    market_list = []
    profit = 0
    profit_rate = 0.0

    for row in range(2, stock_sheet.max_row + 1):
        # 交易日期
        deal_date = stock_sheet['A' + str(row)].value
        # 股票代码
        stock_code = stock_sheet['C' + str(row)].value
        # 股票名
        stock_name = stock_sheet['D' + str(row)].value
        # 股票操作
        operation = stock_sheet['E' + str(row)].value
        # 成交量
        deal_count = stock_sheet['F' + str(row)].value
        # 成交价
        deal_price = stock_sheet['G' + str(row)].value
        # 成交金额
        deal_amount = stock_sheet['H' + str(row)].value
        # 手续费
        handling_charge = stock_sheet['K' + str(row)].value
        # 印花税
        stamp_duty = stock_sheet['L' + str(row)].value
        # 其他杂费
        others = stock_sheet['M' + str(row)].value
        # 市场区分
        market_region = stock_sheet['N' + str(row)].value

        if market_region not in market_list:
            market_list.append(market_region)

        info = stock_info(deal_date, stock_code, stock_name, float(deal_price), int(deal_count), float(deal_amount),
                          operation, float(handling_charge), float(stamp_duty), float(others), market_region)
        # 买入成本
        if operation == '卖出':
            return
            # result, rate = cal_profit(cal_profit_sheet, info, stock_list)
            # profit = profit + result
            # profit_rate = profit_rate + rate
        else:
            # 买入成本
            info.cost = float(deal_amount) + float(handling_charge) + float(stamp_duty) + float(others)
            stock_list.append(info)

    return stock_info_dict


def cal_stocks_profit():
    """
        计算股票收益
    """
    stock_wb = openpyxl.load_workbook(file_name)
    stock_sheet = stock_wb['stock_info']
    # 创建计算利润sheet
    # cal_profit_sheet = stock_wb.create_sheet("cal_profit")
    # 保存工作簿
    # stock_wb.save(file_name)
    # 设置[计算利润]sheet的第一行数据
    # set_title(cal_profit_sheet)

    logging.debug('''----------- cal profit start -----------''')
    stock_info_dict = {}
    stock_info_dict = get_stock_info_dict(stock_sheet)

    logging.debug('''----------- cal profit end -------------''')


def cal_profit(sheet, info, stock_list):
    """
        计算股票收益
    """
    profit = 0.0
    profit_rate = 0.0

    # 抛售股份代码
    stock_code = info.stock_code
    # 抛售股份的成交金额
    amount = info.deal_amount
    # 抛售股份数量
    sell_count = info.deal_count
    # 获得抛售股份的成本
    cost = get_cost(stock_code, stock_list, sell_count)
    if cost > 0:
        cost = cost + info.handling_charge + info.stamp_duty + info.others
        profit = amount - cost
        profit_rate = round(profit / cost, 3)

        logging.debug('''
                {0}抛售股票信息如下:
                股票代码={1},
                股票名={2},
                成交价={3},
                成交量={4}股,
                成交金额={5}，
                买入成本={6},
                卖出手续费={7}，
                卖出印花税={8}，
                卖出其他杂费={9}
                净利润={10},
                净利润率={11}%
                '''.format(info.deal_date, stock_code, info.stock_name, str(round(info.deal_price, 2)) + money_unit,
                           info.deal_count,str(round(info.deal_amount, 2)) + money_unit,
                           str(round(cost, 2)) + money_unit,
                           str(round(info.handling_charge, 2)) + money_unit,
                           str(round(info.stamp_duty, 2)) + money_unit,
                           str(round(info.others, 2)) + money_unit, str(round(profit, 2)) + money_unit,
                           round(profit_rate, 2) * 100))
    else:
        logging.debug('''
        由于没有找到买入记录，
        因此只显示{0}抛售股票信息如下:
                股票代码={1},
                股票名={2},
                成交价={3},
                成交量={4}股,
                成交金额={5}，
                卖出手续费={6}，
                卖出印花税={7}，
                卖出其他杂费={8}
                '''.format(info.deal_date, stock_code, info.stock_name, str(round(info.deal_price, 2)) + money_unit,
                           info.deal_count, str(round(info.deal_amount, 2)) + money_unit,
                           str(round(info.handling_charge, 2)) + money_unit,
                           str(round(info.stamp_duty, 2)) + money_unit, str(round(info.others, 2)) + money_unit))
    return profit, profit_rate


def get_cost(stock_code, stock_list, sell_count):
    """
        计算抛售股票的实际成本
    """
    i = 0
    # 买入股份的总成本金额
    cost = 0.0
    # 买入股份的总股数
    count = 0
    # 买入股份的总手续费
    handling_charge = 0.0
    # 买入股份的总印花税
    stamp_duty = 0.0
    # 买入股份的总的其他杂费
    others = 0.0

    for i in range(len(stock_list)):
        item = stock_list[i]
        if stock_code == item.stock_code:
            cost = cost + item.cost
            count = count + item.deal_count
            handling_charge = handling_charge + item.handling_charge
            stamp_duty = stamp_duty + item.stamp_duty
            others = others + item.others

            logging.debug('''
                        {0}买入股票信息如下:
                        股票代码={1},
                        股票名={2},
                        成交价={3},
                        成交量={4}股,
                        成交金额={5}，
                        买入成本={6},
                        买入手续费={7},
                        买入印花税={8}，
                        买入其他杂费={9}
                        '''.format(item.deal_date, stock_code, item.stock_name,
                                   str(round(item.deal_price, 2)) + money_unit,
                                   item.deal_count, str(round(item.deal_amount, 2)) + money_unit,
                                   str(round(item.cost, 2)) + money_unit,
                                   str(round(handling_charge, 2)) + money_unit, str(round(stamp_duty, 2)) + money_unit,
                                   str(round(others, 2)) + money_unit))

    # 判定买入记录是否找到
    if count > 0 and cost > 0:
        # 判定是否有送股
        if count >= sell_count:
            price = cost / count

            handling_charge = handling_charge / count
            stamp_duty = stamp_duty / count
            others = others / count

            return price * sell_count + handling_charge * sell_count + \
                   stamp_duty * sell_count + others * sell_count
        else:
            # 因为送股，股均价就被摊薄
            price = cost / sell_count
            logging.debug('''
                        买入股票综合信息如下:
                        股票代码={},
                        股票名={},
                        平均成交价={},
                        总成交量={}股,
                        总成交金额={}，
                        总买入成本={},
                        总买入手续费={},
                        总买入印花税={}，
                        总买入其他杂费={}
                        '''.format(stock_code, item.stock_name, str(round(price, 2)) + money_unit,
                                   sell_count, str(round(cost - handling_charge - stamp_duty - others, 2)) + money_unit,
                                   str(round(cost, 2)) + money_unit, str(round(handling_charge, 2)) + money_unit,
                                   str(round(stamp_duty, 2)) + money_unit, str(round(others, 2)) + money_unit))
            return cost
    else:
        logging.debug('''
                    股票代码={0},
                    未找到买入记录。
                    将不计算净利润与净利润率。
                    '''.format(stock_code))
        return -1


def set_title(sheet):
    for col in range(len(sheet_title)):
        sheet.cell(row=1, column=col, value=sheet_title[col])


def main():
    """
        主函数
    """
    cal_stocks_profit()


if __name__ == '__main__':
    main()
