"""
@ProjectName: Covid-2019
@FileName: stock_info.py
@Author: xiao-yi.yu
@Date: 2020/09/14
"""
import logging

logging.basicConfig(filename='stocks.log',
                    format='%(asctime)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)


class stock_info:
    # 交易日期
    deal_date = ''
    # 股票代码
    stock_code = ''
    # 股票名
    stock_name = ''
    # 成交价
    deal_price = ''
    # 成交量
    deal_count = ''


    
    # 成交金额
    deal_amount = ''
    # 股票操作
    operation = ''
    # 手续费
    handling_charge = ''
    # 印花税
    stamp_duty = ''
    # 买入成本
    cost = ''
    # 其他杂费
    others = ''
    # 交易市场
    market_region = ''

    def __init__(self, deal_date, stock_code, stock_name, deal_price, deal_count, deal_amount, operation,
                 handling_charge, stamp_duty, others, market_region):
        self.deal_date = deal_date
        self.stock_code = stock_code
        self.stock_name = stock_name
        self.deal_price = deal_price
        self.deal_count = deal_count
        self.deal_amount = deal_amount
        self.operation = operation
        self.handling_charge = handling_charge
        self.stamp_duty = stamp_duty
        self.others = others
        self.market_region = market_region
