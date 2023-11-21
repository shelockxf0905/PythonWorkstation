"""
@ProjectName: 爬取文章
@FileName: getArticleContents.py
@Author: xiao-yi.yu
@Date: 2023/02/15
"""
import re

import requests
import parsel
import os

# 定义html文件夹的名字
html_folder = 'html\\'

html_str = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>{title}</title>
    </head>
    <body>
    {article}
    </body>
</html>
"""


def get_article_contents():
    # 判断文件夹是否存在
    if not os.path.exists(html_folder):
        # 如果不存在,就创建文件夹
        os.makedirs(html_folder)

    # 文章列表的url地址
    url = 'https://www.chinawenwang.com/zlist-66-1.html'
    # 请求头[字典形式]User - Agent:浏览器的基本信息
    headers = {
        'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/86.0.4240.198 Safari/537.36'
    }
    # 发送请求
    response = requests.get(url=url, headers=headers)
    # print(response.text)
    # 解析数据 用re正则表达式提取文章url地址 匹配任意字符 除了(\n)
    href = re.findall('<h2><a href="(.*?)" class="juhe-page-left-div-link">', response.text)
    for link in href:
        article_response = requests.get(url=link, headers=headers)
        print(article_response.text)
        selector = parsel.Selector(article_response.text)
        title = selector.css('.content-page-header-div h1::text').get()
        contents = selector.css('.content-page-main-content-div').get()
        print(title)
        print(contents)
        article = html_str.format(title=title, article=contents)
        print(article)
        html_path = html_folder + title + '.html'
        print(html_path)
        with open(html_path, mode='w', encoding='utf-8') as f:
            f.write(article)


def main():
    """
        主函数
    """
    # 获取漫画jpg文件内容
    get_article_contents()


if __name__ == '__main__':
    main()
