"""
@ProjectName: Covid-2019
@FileName: crawler.py
@Author: xiao-yi.yu
@Date: 2020/04/04
"""
from bs4 import BeautifulSoup
from service.db import DB
from service.userAgent import user_agent_list
from service.nameMap import country_type_map, city_name_map, country_name_map, continent_name_map
import re
import json
import time
import random
import logging
import requests


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)


class Crawler:
    def __init__(self):
        self.session = requests.session()
        self.db = DB()
        self.crawl_timestamp = int()

    def run(self):
        while True:
            self.crawler()
            time.sleep(60)

    def crawler(self):
        while True:
            self.session.headers.update(
                {
                    'user-agent': random.choice(user_agent_list)
                }
            )
            self.crawl_timestamp = int(time.time() * 1000)
            try:
                r = self.session.get(url='https://ncov.dxy.cn/ncovh5/view/pneumonia')
            except requests.exceptions.ChunkedEncodingError:
                continue
            # soup = BeautifulSoup(r.content, 'lxml')
            soup = BeautifulSoup(r.content, 'html.parser')

            overall_information = re.search(r'(\{"id".*\})\}', str(soup.find('script', attrs={'id': 'getStatisticsService'})))
            if overall_information:
                self.overall_parser(overall_information=overall_information)

            area_information = re.search(r'\[(.*)\]', str(soup.find('script', attrs={'id': 'getAreaStat'})))
            if area_information:

                self.area_parser(area_information=area_information)

            abroad_information = re.search(r'\[(.*)\]', str(soup.find('script', attrs={'id': 'getListByCountryTypeService2true'})))
            if abroad_information:
                self.abroad_parser(abroad_information=abroad_information)

            news_chinese = re.search(r'\[(.*?)\]', str(soup.find('script', attrs={'id': 'getTimelineService1'})))
            if news_chinese:
                self.news_parser(news=news_chinese)

            news_english = re.search(r'\[(.*?)\]', str(soup.find('script', attrs={'id': 'getTimelineService2'})))
            if news_english:
                self.news_parser(news=news_english)

            rumors = re.search(r'\[(.*?)\]', str(soup.find('script', attrs={'id': 'getIndexRumorList'})))
            if rumors:
                self.rumor_parser(rumors=rumors)

            if not overall_information or \
                    not area_information or \
                    not abroad_information or \
                    not news_chinese or \
                    not news_english or \
                    not rumors:
                time.sleep(3)
                continue

            break

        logger.info('Successfully crawled.')

    def overall_parser(self, overall_information):
        overall_information = json.loads(overall_information.group(1))
        overall_information.pop('id')
        overall_information.pop('createTime')
        overall_information.pop('modifyTime')
        overall_information.pop('imgUrl')
        overall_information.pop('deleted')
        overall_information['countRemark'] = overall_information['countRemark'].replace(' ??????', '?????????').replace(' ??????', '?????????').replace(' ??????', '?????????').replace(' ', '')

        if not self.db.find_one(collection='DXYOverall', data=overall_information):
            overall_information['updateTime'] = self.crawl_timestamp

            self.db.insert(collection='DXYOverall', data=overall_information)

    def province_parser(self, province_information):
        provinces = json.loads(province_information.group(0))
        for province in provinces:
            province.pop('id')
            province.pop('tags')
            province.pop('sort')
            province['comment'] = province['comment'].replace(' ', '')

            if self.db.find_one(collection='DXYProvince', data=province):
                continue

            province['provinceEnglishName'] = city_name_map[province['provinceShortName']]['engName']
            province['crawlTime'] = self.crawl_timestamp
            province['country'] = country_type_map.get(province['countryType'])

            self.db.insert(collection='DXYProvince', data=province)

    def area_parser(self, area_information):
        area_information = json.loads(area_information.group(0))
        for area in area_information:
            area['comment'] = area['comment'].replace(' ', '')

            # Because the cities are given other attributes,
            # this part should not be used when checking the identical document.
            cities_backup = area.pop('cities')

            if self.db.find_one(collection='DXYArea', data=area):
                continue

            # If this document is not in current database, insert this attribute back to the document.
            area['cities'] = cities_backup

            area['countryName'] = '??????'
            area['countryEnglishName'] = 'China'
            area['continentName'] = '??????'
            area['continentEnglishName'] = 'Asia'
            area['provinceEnglishName'] = city_name_map[area['provinceShortName']]['engName']

            for city in area['cities']:
                if city['cityName'] != '???????????????':
                    try:
                        city['cityEnglishName'] = city_name_map[area['provinceShortName']]['cities'][city['cityName']]
                    except KeyError:
                        print(area['provinceShortName'], city['cityName'])
                        pass
                else:
                    city['cityEnglishName'] = 'Area not defined'

            area['updateTime'] = self.crawl_timestamp

            self.db.insert(collection='DXYArea', data=area)

    def abroad_parser(self, abroad_information):
        countries = json.loads(abroad_information.group(0))
        for country in countries:
            try:
                country.pop('id')
                country.pop('tags')
                country.pop('sort')
                # Ding Xiang Yuan have a large number of duplicates,
                # values are all the same, but the modifyTime are different.
                # I suppose the modifyTime is modification time for all documents, other than for only this document.
                # So this field will be popped out.
                country.pop('modifyTime')
                # createTime is also different even if the values are same.
                # Originally, the createTime represent the first diagnosis of the virus in this area,
                # but it seems different for abroad information.
                country.pop('createTime')
                country['comment'] = country['comment'].replace(' ', '')
            except KeyError:
                pass
            country.pop('countryType')
            country.pop('provinceId')
            country.pop('cityName')
            # The original provinceShortName are blank string
            country.pop('provinceShortName')
            # Rename the key continents to continentName
            country['continentName'] = country.pop('continents')

            if self.db.find_one(collection='DXYArea', data=country):
                continue

            country['countryName'] = country.get('provinceName')
            country['provinceShortName'] = country.get('provinceName')
            country['continentEnglishName'] = continent_name_map.get(country['continentName'])
            country['countryEnglishName'] = country_name_map.get(country['countryName'])
            country['provinceEnglishName'] = country_name_map.get(country['countryName'])

            country['updateTime'] = self.crawl_timestamp

            self.db.insert(collection='DXYArea', data=country)

    def news_parser(self, news):
        news = json.loads(news.group(0))
        for _news in news:
            _news.pop('pubDateStr')
            if self.db.find_one(collection='DXYNews', data=_news):
                continue
            _news['crawlTime'] = self.crawl_timestamp

            self.db.insert(collection='DXYNews', data=_news)

    def rumor_parser(self, rumors):
        rumors = json.loads(rumors.group(0))
        for rumor in rumors:
            rumor.pop('score')
            rumor['body'] = rumor['body'].replace(' ', '')
            if self.db.find_one(collection='DXYRumors', data=rumor):
                continue
            rumor['crawlTime'] = self.crawl_timestamp

            self.db.insert(collection='DXYRumors', data=rumor)


if __name__ == '__main__':
    crawler = Crawler()
    crawler.run()
