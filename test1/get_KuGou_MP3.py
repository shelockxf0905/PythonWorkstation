"""
    作者：xiao-yi.yu
    日期：2023/11/14
    功能：获取kugou音乐
    版本：1.0
"""
import requests
import json


headers = {
    'User - Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}


def main():
    """
        主函数
    """
    url_list = 'https://searchrecommend.kugou.com/get/complex?callback=jQuery19106011142930865625_1700031494948&word=%E8%AE%B8%E5%B7%8D&_=1700031494950'

    list_resp = requests.get(url_list, headers=headers)
    print("")
    print(list_resp.text[42:-3])
    print("")
    song_list = json.loads(list_resp.text[42:-3])['data']['song']
    print(song_list)
    for i, enum in enumerate(song_list):
        print(f'{i +1}===={enum.get("singername")}===={enum.get("songname")}===={enum.get("hash")}')

    # url = "https://webfs.hw.kugou.com/202311141451/e3a5aaab4b7ebf87267ea213a671c72e/v2/19e030ab78dc0ea613ee5b71b250abd3/part/0/960169/G324/M0B/A4/57/clip_JJUEAGTTXSCAbZn7AEqqboHJhh0589.mp3"

    # res = requests.get(url, headers=headers)
    # with open('kugou_1.mp3', 'wb') as f:
    #     f.write(res.content)


if __name__ == '__main__':
    main()
