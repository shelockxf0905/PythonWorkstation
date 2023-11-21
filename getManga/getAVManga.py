"""
@ProjectName: 爬取羞羞漫画网<<火影忍者同人漫画大全（本子）>>的漫画图片
@FileName: getAVManga.py
@Author: xiao-yi.yu
@Date: 2023/02/14
"""
import requests
import parsel
import os


def get_av_manga_jpg_file():
    # 1.对漫画目录页面发送请求
    url = 'http://mhw.xxmh7.biz/13684ddd-a0d7-41bc-be8d-00cb58a39a8b'  # 确定请求url地址
    response = requests.get(url=url)

    # 2.获取html字符串数据
    print(response.text)

    # 3.提取章节名字与ID
    selector = parsel.Selector(response.text)  # 转成可解析的对象
    lis = selector.css('.chapter__list-box li')
    for li in list(reversed(lis))[1:]:
        # 章节id
        chaper_id = li.css('a::attr(data-chapterid)').get()
        # 章节名
        chaper_title = li.css("a::text").getall()[-1].strip()
        print(chaper_id, chaper_title)
        # 以章节名为文件夹名
        folder_name = f'{chaper_title}\\'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        # 组建requests的url
        link = 'https://comic.mkzcdn.com/chapter/content/v1/'
        # 组建requests的param
        data = {'chapter_id': chaper_id,
                'comic_id': '215720',
                'format': '1',
                'quality': '1',
                'type': '1'}

        # 获得response的内容
        json_data = requests.get(url=link, params=data).json()['data']['page']
        print(json_data)
        page = 1
        for index in json_data:
            # 获得image的url
            img_url = index['image']
            print(img_url)
            image_contents = requests.get(url=img_url).content
            with open(folder_name + str(page) + '.jpg', mode='wb') as f:
                f.write(image_contents)
                page += 1
        break


def main():
    """
        主函数
    """
    # 获取漫画jpg文件内容
    get_av_manga_jpg_file()


if __name__ == '__main__':
    main()



