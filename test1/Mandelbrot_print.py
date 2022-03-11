"""
    作者：xiao-yi.yu
    日期：2019/10/21
    功能：输出mandelbrot图像
    版本：1.0
"""


from collections import Counter


# 重复元素判定
def all_unique(lst):
    return len(lst) == len(set(lst))


# 字符元素组成判定
def anagram(first, second):
    return Counter(first) == Counter(second)


def main():
    """
        主函数
    """
    x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
    y = [1, 2, 3, 4, 5]
    print("是否存在重复元素:" + str(all_unique(x)))
    print("是否存在重复元素:" + str(all_unique(y)))


if __name__ == '__main__':
    main()