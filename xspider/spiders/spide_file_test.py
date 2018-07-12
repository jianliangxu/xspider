import time

import scrapy
from selenium import webdriver
from xspider.items import SxspiderItem
import re
import os


class Sxspider(scrapy.Spider):
    name = "sxspider_file_test"
    allowed_domians = ["http://ladyxingbs.com/", "https://www.wifi588.net/"]
    start_urls = [
        "http://ladyxingbs.com/"
    ]

    agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
    header = {
        "HOST": "http://ladyxingbs.com/",
        "Referer": "http://ladyxingbs.com/",
        'User-Agent': agent
    }

    def parse(self, response):
        # xitem = response.meta['item']
        # title = response.css("#thread_subject::text").extract()
        # xitem['title'] = title
        #

        file_usefull_urls = [
            'http://ladyxingbs.com/forum.php?mod=attachment&aid=Nzk4MTc3NXwyYzJmNDNhZXwxNTMxMjg4MDU3fDB8OTk1NzgzOA%3D%3D']
        xitem = SxspiderItem()
        # file_urls = response.css("a[href*='attachment']::attr(href)").extract()
        # for file_url in file_urls:
        #     if re.match(r"^forum", file_url):
        #         file_usefull_urls.append(os.path.join("http://ladyxingbs.com/", file_url))

        xitem['file_urls'] = file_usefull_urls
        yield xitem

    # def parse(self, response):
    #     # urls = response.css("th.new > a.s.xst::attr(href)").extract()
    #     # count = 0
    #     # for url in urls:
    #     #     count = count + 1
    #     #     if count == 1:
    #     #         continue  # 过滤掉第一条
    #     #
    #     #     full_url = os.path.join("http://ladyxingbs.com/", url)
    #     item = SxspiderItem(url=[])
    #     req = scrapy.Request([], callback=self.parse_item)
    #     req.meta['item'] = item
    #     yield req

    # def start_requests(self):
    #     browser = webdriver.Chrome(executable_path="D:\\pycharm\\drivers\\chromedriver.exe")
    #     browser.get("http://ladyxingbs.com/")
    #     time.sleep(2)
    #     browser.find_element_by_css_selector("#goin").click()
    #     time.sleep(2)
    #     browser.find_element_by_css_selector("#ls_username").send_keys("jianliang_xu")
    #     browser.find_element_by_css_selector("#ls_password").send_keys("2009fendou")
    #     browser.find_element_by_css_selector(
    #         "#lsform > div.fastlg.cl > div > table > tbody > tr:nth-child(4) > td > button").click()
    #
    #     cookiess = browser.get_cookies()
    #     cookie_dict = {}
    #     for cookie in cookiess:
    #         cookie_dict[cookie['name']] = cookie['value']
    #
    #     for i in range(1):
    #         yield scrapy.Request(url="http://ladyxingbs.com/forum-798-" + str(i + 1) + ".html", dont_filter=True,
    #                              cookies=cookie_dict, meta={"page": "page" + str(i + 1)})

    # http://ladyxingbs.com/forum-798-1.html 华人sex ai
    # http://ladyxingbs.com/forum-723-1.html 无码
    # http://ladyxingbs.com/forum-713-1.html 有码
    # http://ladyxingbs.com/forum-525-1.html oumei
    # http://ladyxingbs.com/forum-280-1.html 图文并冒
