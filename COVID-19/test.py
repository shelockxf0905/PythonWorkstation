# from pyecharts.charts import Bar
# from pyecharts import options as opts
# import openpyxl
import os
# import re
# import sys


# 示例数据
cate = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
data1 = [123, 153, 89, 107, 98, 23]
data2 = [56, 77, 93, 68, 45, 67]
file_name = "D:\\yuxiaoyi\\2022-05-04\\A股历史成交明细.xlsx"
# 设定文件路径
file_path = 'D:\\YouTube\\政治风云'


def check_filename_len():
    # 对目录下的文件进行遍历
    for file in os.listdir(file_path):
        # 判断文件名是否以'y2mate.com - '开头
        if file.startswith('y2mate.com - '):
            # 把'y2mate.com - '除去
            new_name = file.replace("y2mate.com - ", "").strip()
            # 重命名
            os.rename(os.path.join(file_path, file), os.path.join(file_path, new_name))

        if file.startswith('yt5s.com-'):
            # 把'yt5s.com-'除去
            new_name = file.replace("yt5s.com-", "").strip()
            # 重命名
            os.rename(os.path.join(file_path, file), os.path.join(file_path, new_name))

        if file.startswith(' '):
            # 把空格除去
            new_name = file.strip()
            # 重命名
            os.rename(os.path.join(file_path, file), os.path.join(file_path, new_name))

    # 对目录下的文件进行遍历
    for file in os.listdir(file_path):
        # 判断文件名是否过长
        if len(file.title()) > 94:
            print('重命名元文件名=%s' % file)
            # 查找'单口相声嘚啵嘚'的字符串
            index_s = file.find('单口相声嘚啵嘚')
            if index_s > 0:
                # 有'单口相声嘚啵嘚'关键字
                # 截取60长度的字符串
                new_name = file[0:60]
                # 查找'（'的字符串
                index_topic = file.find('（')
                if index_topic > 0:
                    # 有topic
                    topic = file[index_topic:]
                else:
                    # 无topic
                    topic = file[index_s:]
                new_name += topic
                print('重命名文件名=%s' % new_name)
            else:
                # 截取90长度的字符串 + '.mp4'
                new_name = file[0:90] + '.mp4'
                print('重命名文件名=%s' % new_name)

            # 重命名
            os.rename(os.path.join(file_path, file), os.path.join(file_path, new_name))


def file_rename():
    # 对目录下的文件进行遍历
    for file in os.listdir(file_path):
        # 判断是否是文件（查找以.pdf结尾的文件）
        if file.endswith(".pdf"):
            print(file)
            # # 设置新文件名
            # new_name = file.replace("QL", "权利")  # 这一句的效果是将QL替换为权利
            new_name = file.replace(".pdf", ".mp4")
            # 重命名
            os.rename(os.path.join(file_path, file), os.path.join(file_path, new_name))


def main():
    """
        主函数
    """
    # bar = (Bar()
    #        .add_xaxis(cate)
    #        .add_yaxis('电商渠道', data1)
    #        .add_yaxis('门店', data2)
    #        .set_global_opts(title_opts=opts.TitleOpts(title="XY轴翻转-基本示例", subtitle="我是副标题"))
    #        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    #        .reversal_axis()
    #       )
    #
    # bar.render_notebook()
    # path = input('请输入文件路径(结尾加上/)：')
    #
    # # 获取该目录下所有文件，存入列表中
    # file_list = os.listdir(path)
    #
    # n = 0
    # for i in fileist:
    #     # 设置旧文件名（就是路径+文件名）
    #     old_name = path + os.sep + file_list[n]  # os.sep添加系统分隔符
    #
    #     # 设置新文件名
    #     new_name = path + os.sep + 'a' + str(n + 1) + '.JPG'
    #
    #     os.rename(old_name, new_name)  # 用os模块中的rename方法对文件改名
    #     print(old_name, '======>', new_name)
    #
    #     n += 1

    # folder_path = "/Users/linzehua/Desktop/Python代码练习/08/09"
    # file_list = os.listdir(folder_path)
    # # 切换到当前文件夹路径下
    # os.chdir(folder_path)
    # for old_name in file_list:
    #     new_name = "[ZZ出品]" + old_name
    #     os.rename(old_name, new_name)
    #     pass
    print("\n File rename is Start.")

    # file_rename()
    check_filename_len()
    # 结束
    print("File rename is End.")

    # Python根据条件修改目录里的文件名:将不想要的删去或者替换掉

    # 设定文件路径

    # path = 'G:\\影视02\\足球小将初中篇[辽艺国语配音]\\01_足球小将小学篇'
    #
    # def rename(path):
    #     # 对目录下的文件进行遍历
    #
    #     for file in os.listdir(path):
    #
    #         # 判断是否是文件（查找以QL开头以.rmvb结尾的文件）
    #         if (file.startswith("[MINI资源组][足球小将小学篇]") and file.endswith(".mkv")):
    #             print(file)
    #             # 设置新文件名
    #
    #             # newName=file.replace("[MINI资源组]","")#这一句的效果是直接删除[MINI资源组]
    #             newName = file.replace("[MINI资源组][足球小将小学篇]", "足球小将小学篇")  # 重命名
    #             # 重命名
    #
    #             os.rename(os.path.join(path, file), os.path.join(path, newName))
    #
    # rename(path)
    # # 结束
    #
    # print("End")
    #
    # file_path = 'G:\\影视\\04_电视剧\\顶级生活\\'
    #
    # def rename(file_path):
    #     # 对目录下的文件进行遍历
    #
    #     for file in os.listdir(file_path):
    #
    #         # 判断是否是文件
    #
    #         if (file.endswith((".mp4", ".avi", ".rmvb"))):
    #             print(file)
    #             # 设置新文件名
    #
    #             if "第一季" in file:
    #                 new_name = file.replace("第一季", "第01季")  # 这一句的效果是将第一季替换为第01季
    #                 os.rename(os.path.join(path, file), os.path.join(path, new_name))
    #             # 重命名
    #
    #             if "第1季" in file:
    #                 new_name = file.replace("第1季", "第01季")  # 这一句的效果是将第1季替换为第01季
    #                 os.rename(os.path.join(path, file), os.path.join(path, new_name))
    #             # 重命名
    #
    #             if "S01E" in file:
    #                 new_name = file.replace("S01E", "第01季-")  # 这一句的效果是将S01E替换为第01季
    #                 os.rename(os.path.join(path, file), os.path.join(path, new_name))
    #             # 重命名
    #
    #             if "第二季" in file:
    #                 new_name = file.replace("第二季", "第02季")  # 这一句的效果是将第二季替换为第02季
    #                 os.rename(os.path.join(path, file), os.path.join(path, new_name))
    #             # 重命名
    #
    #             if "S02E" in file:
    #                 new_name = file.replace("S02E", "第02季-")  # 这一句的效果是将S02E替换为第02季
    #                 os.rename(os.path.join(path, file), os.path.join(path, new_name))
    #             # 重命名
    #
    #             if "第三季" in file:
    #                 new_name = file.replace("第三季", "第03季")  # 这一句的效果是将第三季替换为第03季
    #                 os.rename(os.path.join(path, file), os.path.join(path, new_name))
    #             # 重命名
    #
    #             if "S03E" in file:
    #                 new_name = file.replace("S03E", "第03季-")  # 这一句的效果是将S03E替换为第03季
    #                 os.rename(os.path.join(path, file), os.path.join(path, new_name))
    #             # 重命名
    #
    #             if "第四季" in file:
    #                 new_name = file.replace("第四季", "第04季")  # 这一句的效果是将第四季替换为第04季
    #                 os.rename(os.path.join(path, file), os.path.join(path, new_name))
    #             # 重命名
    #
    #             if "第五季" in file:
    #                 new_name = file.replace("第五季", "第05季")  # 这一句的效果是将第五季替换为第05季
    #                 os.rename(os.path.join(path, file), os.path.join(path, new_name))
    #             # 重命名
    #
    #             if "第六季" in file:
    #                 new_name = file.replace("第六季", "第06季")  # 这一句的效果是将第六季替换为第06季
    #                 os.rename(os.path.join(path, file), os.path.join(path, new_name))
    #             # 重命名
    #
    #             if "第七季" in file:
    #                 new_name = file.replace("第七季", "第07季")  # 这一句的效果是将第七季替换为第07季
    #                 os.rename(os.path.join(path, file), os.path.join(path, new_name))
    #             # 重命名
    #
    #             if "第八季" in file:
    #                 new_name = file.replace("第八季", "第08季")  # 这一句的效果是将第八季替换为第08季
    #                 os.rename(os.path.join(path, file), os.path.join(path, new_name))
    #
    # # 重命名
    #
    # rename(path)
    # # 结束
    #
    # print("End")
    #
    # # 批量修改文件名
    # # 批量修改图片文件名
    #
    #
    # path = 'F:\Temp\ZZ'
    # fileList = os.listdir(path)  # 待修改文件夹
    # print("修改前：" + str(fileList))  # 输出文件夹中包含的文件
    #
    # currentpath = os.getcwd()  # 得到进程当前工作目录
    # os.chdir(path)  # 将当前工作目录修改为待修改文件夹的位置
    # n = 1  # 名称变量
    # for fileName in fileList:  # 遍历文件夹中所有文件
    #     pat = ".+\.(jpg|png|jpeg)"  # 匹配文件名正则表达式
    #     pattern = re.findall(pat, fileName)  # 进行匹配
    #     os.rename(fileName, (str(n) + '.' + pattern[0]))  # 文件重新命名
    #     n += 1  # 改变编号，继续下一项
    #
    # os.chdir(currentpath)  # 改回程序运行前的工作目录
    # sys.stdin.flush()  # 刷新
    # print("修改后：" + str(os.listdir(path)))  # 输出修改后文件夹中包含的文件

    # stock_wb = openpyxl.load_workbook(file_name)
    # stock_sheet = stock_wb['stock_info']
    # print([[c.value for c in row] for row in stock_sheet['A2:M105']])
    #
    # print([[col.value for col in columns][1:] for columns in stock_sheet['A:K']])
    #
    # print(list(zip(*list(stock_sheet.values)[1:])))

    # sh = stock_wb.worksheets[0]
    # for row in sh.rows:
    #     print([c.value for c in row])
    #
    # for col in sh.columns:
    #     print([c.value for c in col])
    #
    # print(sh.min_row, sh.min_column, sh.max_row, sh.max_column)

    # for row in sh.iter_rows(min_row=2, min_col=2, max_row=sh.max_row, max_col=2):
    #     print([c.value for c in row])

    # for row in list(sh.rows)[1:]:
    #     line = [c.value for c in row]
    #     print("[%s-%s]:%s" % (line[1], line[2], line[3:]))

    # for col in list(sh.columns)[1:]:
    #     line = [c.value for c in col][1:]
    #     print(line)
    #
    # line = [[c.value for c in row] for row in sh.iter_rows(min_row=2, min_col=1, max_row=sh.max_row,
    #                                                        max_col=sh.max_column)]
    # print(line)

    # line = [c.value for c in sh['B']][1:]
    # print(line)

    # total = [sum([c.value for c in row]) for row in sh.iter_rows(min_row=2, min_col=7, max_row=sh.max_row,
    # max_col=10)]
    # print(total)
    # name = [c.value for c in sh['C'][1:]]
    # print(name)
    # print(list(zip(name, total)))
    # max_data = [max([c.value for c in row]) for row in sh.iter_cols(min_row=2, min_col=7, max_row=sh.max_row,
    #                                                                 max_col=10)]
    # print(max_data)
    # name = [c.value for c in sh[1]][6:10]
    # print(name)
    # print(list(zip(name, max_data)))
    # for row in list(sh.rows)[1:]:
    #     line = [v.value for v in row]
    #     print(line[2], sum(line[6:9]))

    # for col in list(sh.columns):
    #     column_data = [v.value for v in col]
    #
    # print(column_data)

    # 工作表['A1'] =
    # 工作表.cell(2, 3, 'Gandum is comming.')

    # wb = openpyxl.Workbook()
    # ws = wb.active
    # ws.title = "十九乘法口诀表"
    # for x in range(1, 20):
    #     for y in range(1, x + 1):
    #         print(y, '*', x, '=', y*x, end='\t')
    #         ws.cell(x, y, '%d × %d = %d' % (y, x, y*x))
    #     print('')
    # wb.save('十九乘法表.xlsx')

    # for r in [['%d × %d = %d' % (y, x, x * y) for y in range(1, x + 1)] for x in range(1, 20)]:
    #     ws.append(r)
    # wb.save('十九乘法表.xlsx')


if __name__ == '__main__':
    main()
