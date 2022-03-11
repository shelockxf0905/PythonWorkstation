"""
    作者：xiao-yi.yu
    日期：2020/04/25
    功能：自动生成YouTube目录
    版本：1.0
"""
import os

youtubePath = "D:\\YouTube\\"


def main():
    """
        主函数
    """
    path1 = "57爆新聞"
    makedir(path1)

    path2 = "stone记"
    makedir(path2)

    path3 = "sun riches"
    makedir(path3)

    path4 = "Wen Zhao Official文昭談古論今"
    makedir(path4)

    path5 = "AV"
    makedir(path5)

    # path6 = "年代向錢看"
    # makedir(path6)

    path7 = "世界历史"
    makedir(path7)

    path8 = "老高與小茉"
    makedir(path8)

    path9 = "曉涵哥來了"
    makedir(path9)

    path10 = "關鍵時刻"
    makedir(path10)

    path11 = "经济金融"
    makedir(path11)

    path12 = "财经冷眼"
    makedir(path12)

    path13 = "seeker大师兄"
    makedir(path13)

    path14 = "电脑硬件"
    makedir(path14)

    path15 = "科技传奇"
    makedir(path15)

    # path16 = "火影"
    # makedir(path16)

    path17 = "看电影"
    makedir(path17)

    path18 = "社会百态"
    makedir(path18)

    path19 = "李永乐老师"
    makedir(path19)

    path20 = "军事动态"
    makedir(path20)

    path21 = "妈咪说MommyTalk"
    makedir(path21)

    path22 = "政治风云"
    makedir(path22)

    path23 = "看动漫"
    makedir(path23)

    path24 = "听音乐"
    makedir(path24)

    # path25 = "袁腾飞"
    # makedir(path25)

    # path26 = "江峰漫談"
    # makedir(path26)

    path27 = "犯罪百科"
    makedir(path27)

    path28 = "中環孫老師"
    makedir(path28)

    path29 = "巫师"
    makedir(path29)

    path30 = "不良博士"
    makedir(path30)

    path31 = "凤凰秀"
    makedir(path31)


def makedir(path):
    if not os.path.exists(youtubePath + path):
        os.makedirs(youtubePath + path, True)
        print("{}目录创建完毕。".format(path))
    else:
        print("{}目录已经存在了。".format(path))


if __name__ == '__main__':
    main()
