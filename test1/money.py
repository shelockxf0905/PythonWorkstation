import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY, date2num


# 设置字体为Microsoft YaHei显示中文
plt.rcParams['font.family'] = 'Microsoft YaHei'
# 更新字体格式
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['font.size'] = 9
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
        主函数
    """
    stocks = pd.read_table('data.txt', usecols=range(15), parse_dates=[0], index_col=0)
    stocks = stocks[::-1]

    # print(stocks.info)
    # print("old columns is " + stocks.columns)

    stocks.rename(columns={'    open': 'open'}, inplace=True)
    # print("new columns is " + stocks.columns)

    stocks['close'].plot(grid=True, label='收盘价')
    plt.legend()
    plt.show()



if __name__ == '__main__':
    main()