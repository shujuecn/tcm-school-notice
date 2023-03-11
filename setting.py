#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-

# 要查询的字段
keywords_list = ["硕士", "复试"]

# 学校信息列表
school_info = {
    "湖南中医药大学": [
        {
            "url": "https://yjsy.hnucm.edu.cn/zsxx/tzgg.htm",
            "title": "//div[@class='news_nr']/ul//@title",
            "href": "//div[@class='news_nr']/ul//@href",
            "time": "//div[@class='news_nr']/ul//span/text()",
        },
        {
            "url": "https://yjsy.hnucm.edu.cn/zsxx/ssszs.htm",
            "title": "//div[@class='news_nr']/ul//@title",
            "href": "//div[@class='news_nr']/ul//@href",
            "time": "//div[@class='news_nr']/ul//span/text()",
        },
    ],
    "湖北民族大学": [
        {
            "url": "https://www.hbmzu.edu.cn/yjsc/zsxx.htm",
            "title": "//tr[@class='blak-14a']//a/text()",
            "href": "//tr[@class='blak-14a']//a/@href",
            "time": "//tr[@class='blak-14a']//nobr/text()",
        }
    ],
    "贵州中医药大学": [
        {
            "url": "http://yjs.gzy.edu.cn/zsjy/zsxx.htm",
            "title": "//a[@class='c191805']/@title",
            "href": "//a[@class='c191805']/@href",
            "time": "//span[@class='timestyle191805']/text()",
        }
    ],
    "山西中医药大学": [
        {
            "url": "https://yjsb.sxtcm.edu.cn/index/tzgg.htm",
            "title": "//div[@class='wape-right']/ul/li/a/@title",
            "href": "//div[@class='wape-right']/ul/li/a/@href",
            "time": "//div[@class='wape-right']/ul/li/span/text()",
        }
    ],
    "甘肃中医药大学": [
        {
            "charset": "gb2312",
            "url": "https://yjsc.gszy.edu.cn/index.php?m=content&c=index&a=lists&catid=12",
            "title": "//div[@class='base_news_listli1']//@title",
            "href": "//div[@class='base_news_listli1']//@href",
            "time": "//div[@class='base_news_listli1']//span/text()",
        }
    ],
    "陕西中医药大学": [
        {
            "url": "http://yzb.sntcm.edu.cn/info/iList.jsp?cat_id=1608",
            "title": "//div[@class='list_r_t']//li//@title",
            "href": "//div[@class='list_r_t']//li//@href",
            "time": "//div[@class='list_r_t']//li/span/text()",
        }
    ],
    "云南中医药大学": [
        {
            "url": "http://www.yjsc.ynutcm.edu.cn/zsgz/qrzssyjszs/index.shtml",
            "title": "//div[@id='container']//ul/li/a/@title",
            "href": "//div[@id='container']//ul/li/a/@href",
            "time": "//div[@id='container']//ul/li/span/text()",
        }
    ],
    "湖北中医药大学": [
        {
            "url": "https://yjs.hbtcm.edu.cn/zsgz/sszs/zytz.htm",
            "title": "//div[@class='l1']//li//@title",
            "href": "//div[@class='l1']//li//@href",
            "time": "//div[@class='l1']//li//span/text()",
        }
    ],
    "河南中医药大学": [
        {
            "url": "https://yjs.hactcm.edu.cn/list-5.html",
            "title": "//ul[@class='Notice']//a/@title",
            "href": "//ul[@class='Notice']//a/@href",
            "time": "//ul[@class='Notice']//dd/text()",
        }
    ],
    "山东中医药大学": [
        {
            "url": "https://yjs.sdutcm.edu.cn/zsgz1.htm",
            "title": "//table[@class='winstyle1253']//tr//a/@title",
            "href": "//table[@class='winstyle1253']//tr//a/@href",
            "time": "//td[@class='timestyle52ac20c85a788a1b015ab65635801921']/text()",
        }
    ],
    "江西中医药大学": [
        {
            "url": "https://yjsy.jxutcm.edu.cn/zsgz/lqxx.htm",
            "title": "//div[@class='list_r_d']//li//@title",
            "href": "//div[@class='list_r_d']//li//@href",
            "time": "//div[@class='list_r_d']//li//span/text()",
        }
    ],
    "广西中医药大学": [
        {
            "url": "https://yjsy.gxtcmu.edu.cn/Category_13/Index.aspx",
            "title": "//ul[@class='infoList newsList']/li/a/text()",
            "href": "//ul[@class='infoList newsList']/li/a/@href",
            "time": "//ul[@class='infoList newsList']/li/span/text()",
        }
    ],
    "福建中医药大学": [
        {
            "url": "https://yjsy.fjtcm.edu.cn/yjsb/1390339007786/",
            "title": "//div[@class='content']//li//text()",
            "href": "//div[@class='content']//li//@href",
            "time": None,
        }
    ],
    "南京中医药大学": [
        {
            "url": "https://gra.njucm.edu.cn/2898/list.htm",
            "title": "//div[@id='wp_news_w3']//tr//a/@title",
            "href": "//div[@id='wp_news_w3']//tr//a/@href",
            "time": None,
        }
    ],
    "黑龙江中医药大学": [
        {
            "url": "http://yjsy.hljucm.net/index/xwdt.htm",
            "title": "//div[@class='posts']/ul/li//a/@title",
            "href": "//div[@class='posts']/ul/li//a/@href",
            "time": "//div[@class='posts']/ul/li/span/text()",
        }
    ],
    "长春中医药大学": [
        {
            "url": "https://y.ccucm.edu.cn/zsgz/sszs.htm",
            "title": "//div[@class='zp']/ul/li/a/text()",
            "href": "//div[@class='zp']/ul/li/a/@href",
            "time": "//div[@class='zp']/ul/li/span/text()",
        }
    ],
    "天津中医药大学": [
        {
            "url": "https://yjsy.tjutcm.edu.cn/lby.jsp?urltype=tree.TreeTempUrl&wbtreeid=1976",
            "title": "//a[@class='c43004']/@title",
            "href": "//a[@class='c43004']/@href",
            "time": "//td[@class='timestyle43004']/text()",
        }
    ],
    "浙江中医药大学": [
        {
            "url": "https://yjsgl.zcmu.edu.cn/list/20",
            "title": "//div[@class='conts-list clearfix']/ul/li/a/@title",
            "href": "//div[@class='conts-list clearfix']/ul/li/a/@href",
            "time": "//div[@class='conts-list clearfix']/ul/li//span/text()",
        }
    ],
    "成都中医药大学": [
        {
            "url": "https://yjs.cdutcm.edu.cn/zsgz",
            "title": "//ul[@class='pageTPList']//div[@class='title']//@title",
            "href": "//ul[@class='pageTPList']//div[@class='title']//@href",
            "time": "//ul[@class='pageTPList']//div[@class='others']//span[@class='date']/text()",
        }
    ],
    "安徽中医药大学": [
        {
            "url": "http://yjsb.ahtcm.edu.cn/zsjy/zsdt.htm",
            "title": "//span[@class='Article_Title']//a/@title",
            "href": "//span[@class='Article_Title']//a/@href",
            "time": "//span[@class='Article_PublishDate']/text()",
        },
        {
            "url": "http://yjsb.ahtcm.edu.cn/xxgk/zszc.htm",
            "title": "//span[@class='Article_Title']//a/@title",
            "href": "//span[@class='Article_Title']//a/@href",
            "time": "//span[@class='Article_PublishDate']/text()",
        },
    ],
    "广州中医药大学": [
        {
            "url": "https://yjsy.gzucm.edu.cn/zsgz1/ssszs.htm",
            "title": "//a[@class='c71392']/@title",
            "href": "//a[@class='c71392']/@href",
            "time": "//span[@class='timestyle71392']/text()",
        }
    ],
    "上海中医药大学": [
        {
            "url": "https://yjsy.shutcm.edu.cn/1125/list.htm",
            "title": "//span[@class='Article_Title']/a/@title",
            "href": "//span[@class='Article_Title']/a/@href",
            "time": "//span[@class='Article_PublishDate']/text()",
        }
    ],
    "河北中医学院": [
        {
            "charset": "gb2312",
            "url": "https://yjsxy.hebcm.edu.cn/col/1628824153772/index.html",
            "title": "//div[@class='tza-listbt']/a/@title",
            "href": "//div[@class='tza-listbt']/a/@href",
            "time": "//div[@class='tza-listbt']/span/text()",
        }
    ],
    "北京中医药大学": [
        {
            "url": "https://yanjiusheng.bucm.edu.cn/zsjy/sszs/index.htm",
            "title": "//div[@class='ul_list']//li/a/text()",
            "href": "//div[@class='ul_list']//li/a/@href",
            "time": "//div[@class='ul_list']//li/span/text()",
        }
    ],
}


if __name__ == "__main__":
    for school, urls in school_info.items():
        for url in urls:
            url_str = url["url"]
            path_str = url["title"]
            time_str = url["time"]

            print(school)
            print(url_str)
            print(path_str)
            print(time_str)

        print()
