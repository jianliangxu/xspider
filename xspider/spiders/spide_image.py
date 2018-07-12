import time

import scrapy
from selenium import webdriver
from xspider.items import SxspiderItem
import re
import os


class Sxspider(scrapy.Spider):
    name = "sxspider_image"
    allowed_domians = ["http://ladyxingbs.com/"]
    start_urls = [
        "http://ladyxingbs.com/"
    ]

    agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
    header = {
        "HOST": "http://ladyxingbs.com/",
        "Referer": "http://ladyxingbs.com/",
        'User-Agent': agent
    }

    def parse_item(self, response):
        xitem = response.meta['item']
        title = response.css("#thread_subject::text").extract()
        xitem['title'] = title
        img_urls = response.css("img::attr(file)").extract()
        img_useful_url = []
        for img_url in img_urls:
            if re.match(r"^http", img_url):
                img_useful_url.append(img_url)
        xitem['image_urls'] = img_useful_url
        yield xitem

    def parse(self, response):
        urls = response.css("th.new > a.s.xst::attr(href)").extract()
        for url in urls:
            full_url = os.path.join("http://ladyxingbs.com/", url)
            item = SxspiderItem(url=full_url, page=response.meta['page'])
            req = scrapy.Request(full_url, callback=self.parse_item)
            req.meta['item'] = item
            yield req

    '''
        通过selenium登录sex8
    '''
    def start_requests(self):
        browser = webdriver.Chrome(executable_path="D:\\pycharm\\drivers\\chromedriver.exe")
        browser.get("http://ladyxingbs.com/")
        time.sleep(2)
        browser.find_element_by_css_selector("#goin").click()
        time.sleep(2)
        browser.find_element_by_css_selector("#ls_username").send_keys("jianliang_xu")
        browser.find_element_by_css_selector("#ls_password").send_keys("2009fendou")
        browser.find_element_by_css_selector(
            "#lsform > div.fastlg.cl > div > table > tbody > tr:nth-child(4) > td > button").click()

        cookiess = browser.get_cookies()
        cookie_dict = {}
        for cookie in cookiess:
            cookie_dict[cookie['name']] = cookie['value']

        for i in range(50):
            yield scrapy.Request(url="http://ladyxingbs.com/forum-798-" + str(i + 1) + ".html", dont_filter=True,
                                 cookies=cookie_dict, meta={"page": "page" + str(i + 1)})

        # http://ladyxingbs.com/forum-798-1.html 华人sex ai
        # http://ladyxingbs.com/forum-723-1.html 无码
        # http://ladyxingbs.com/forum-713-1.html 有码
        # http://ladyxingbs.com/forum-525-1.html oumei
        # http://ladyxingbs.com/forum-280-1.html 图文并冒
