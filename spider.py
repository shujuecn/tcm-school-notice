#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
"""
@Brief  : 查询中医药相关院校的考研调剂通知
@Time   : 2023/03/03 11:26:13
@Author : https://github.com/shujuecn
"""

import requests
from lxml import etree
import urllib.parse
from setting import NoticeType, SchoolInfo


class NoticeScraper(object):
    def __init__(self):

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50",
        }
        self.type = None
        self.charset = None
        self.notice_url = None
        self.title_path = None
        self.herf_path = None
        self.time_path = None

    def crawl_notice(self, type, charset):
        """
        在指定的网页中爬取通知信息
        :param type: 要在标题中匹配的关键词
        :return: 匹配成功的通知列表
        """

        try:
            response = requests.get(self.notice_url, headers=self.headers)
            if response.status_code == 200:
                response.encoding = charset
                html = etree.HTML(response.text)
            else:
                print("response.status_code: ", response.status_code)
                return None
        except Exception as e:
            print(e)
            return None

        if html is not None:
            title = html.xpath(self.title_path)
            # 有的官网未提供时间与链接，相应值为None，需要手动补充一个空列表
            herf = html.xpath(self.herf_path) if self.herf_path else [""] * len(title)
            time = html.xpath(self.time_path) if self.time_path else [""] * len(title)

        result = []
        for i in range(len(title)):

            if type in title[i]:

                if not herf[i]:
                    herf[i] = None
                elif "http" not in herf[i]:
                    herf[i] = urllib.parse.urljoin(self.notice_url, herf[i])

                if not time[i]:
                    time[i] = None
                elif "2023" not in time[i]:
                    continue

                res = {"title": title[i], "herf": herf[i], "time": time[i]}
                result.append(res)

            else:
                continue

        return result

    def print_notice(self, result, type):
        """
        在控制台中打印匹配成功的通知信息
        :param result: 通知列表
        :param type: 要在标题中匹配的关键词
        :return: None
        """

        if result:
            for r in result:
                title = r["title"]
                herf = r["herf"]
                time = r["time"]

                title = title.replace(type, "\033[1;31m" + type + "\033[1;34m")
                print(f"标题: \033[1;34m{title}\033[0m")
                print(f"链接: {herf}")
                print(f"时间: {time}")
        else:
            print("暂无通知")

    def run(self, type):
        """
        主函数
        :param type: 要在标题中匹配的关键词
        :return: None
        """

        for school, urls in SchoolInfo.items():

            print("*" * 80, "\n")
            print(f"正在查询\033[1;31m{school}\033[0m的【{type}】通知...\n")

            for url in urls:
                # 如果有charset字段，则使用charset字段的值，否则使用utf-8
                self.charset = url.get("charset", "utf-8")

                self.notice_url = url["url"]
                self.title_path = url["title"]
                self.herf_path = url["href"]
                self.time_path = url["time"]

                try:
                    result = self.crawl_notice(type, self.charset)
                except Exception as e:
                    print(e)
                    result = None

                self.print_notice(result, type)

            print()
        print("*" * 80)


if __name__ == "__main__":
    scraper = NoticeScraper()
    scraper.run(type=NoticeType)
