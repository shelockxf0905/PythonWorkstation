"""
    作者：xiao-yi.yu
    日期：2020/03/29
    功能：作成从Bilibili网站上下载视频list
    版本：1.0
"""

URL = 'https://www.bilibili.com/video/BV1hx411e7KP'
fileName = '【木鱼微剧场】一口气看完《三国演义》（全集）.txt'
total_times = 11


def main():
    """
        主函数
    """
    fo = open(fileName, "w", encoding='utf-8')
    for i in range(total_times):
        url = URL + '?p={}\n'.format(i + 1)
        fo.write(url)

    print('记录全部处理完毕。')


if __name__ == '__main__':
    main()
