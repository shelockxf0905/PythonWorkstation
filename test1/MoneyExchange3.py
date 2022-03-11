"""
    作者：xiao-yi.yu
    功能：汇率兑换
    版本：5.0
    日期：2019/09/21
    2.0 新增功能：根据输入判断是人民币还是美元，进行相应的转换计算
    3.0 增加功能：程序可以一直运行，直到用户选择退出
    4.0 增加功能：将汇率兑换功能封装到函数中
    5.0 增加功能：(1) 使程序结构化 (2) 简单函数的定义 lambda
"""


def convert_currency(inmoney, exchangerate):
    """
        汇率兑换函数
    """
    return inmoney * exchangerate

# 汇率
USD_VS_RMB = 7.15

"""
    主函数
"""
def main():
    # 带单位的货币输入
    currency_str_value = input('请输入带单位的人民币(CNY)或者美元(USD)的兑换金额(退出程序请输入Q/q)：')

    i = 0

    while currency_str_value != 'Q' and currency_str_value != 'q':
        i = i + 1
        print('这是第', i, '次兑换。')
        # 获取货币单位
        unit = currency_str_value[-3:]

        if unit == 'CNY' or unit == 'cny' or unit == 'RMB' or unit == 'rmb':
            # 输入的是人民币
            exchange_rate = 1 / USD_VS_RMB
            title = '美元(USD)金额是：'
        elif unit == 'USD' or unit == 'usd':
            exchange_rate = USD_VS_RMB
            title = '人民币(CNY)金额是：'
        else:
            exchange_rate = -1

        if exchange_rate != -1:
            # 将字符串转换为数字
            in_money = eval(currency_str_value[:-3])

            # 使用lambda定义函数
            convert_currency2 = lambda money: money * exchange_rate

            # 调用lambda函数
            # 汇率计算
            out_money = convert_currency2(in_money)
            # 输出结果
            print(title + str(out_money))
        else:
            # 其他情况
            print('目前版本只支持兑换人民币(CNY)或者美元(USD)!')
        print('************************************************')
        # 带单位的货币输入
        currency_str_value = input('请输入带单位的人民币(CNY)或者美元(USD)的兑换金额(退出程序请输入Q/q)：')

    print('人民币(CNY)或者美元(USD)的兑换程序已退出!')


if __name__ == '__main__':
    main()
