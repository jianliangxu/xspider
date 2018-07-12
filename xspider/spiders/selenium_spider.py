# from selenium import webdriver
# import requests
# import time
#
# browser = webdriver.Chrome(executable_path="D:\\pycharm\\drivers\\chromedriver.exe")
# browser.get("https://www.zhihu.com/signup?next=%2F")
# browser.find_element_by_css_selector("div.SignContainer-switch > span").click()
# browser.find_element_by_css_selector("div.SignFlow-accountInput.Input-wrapper > input").send_keys("18688714924")
# browser.find_element_by_css_selector("div.SignFlow-password > div > div.Input-wrapper > input").send_keys("2018Fendou")
# browser.find_element_by_css_selector("div.Login-content > form > button").click()
#
# time.sleep(5)
#
# cookie = [item["name"] + "=" + item["value"] for item in browser.get_cookies()]
# cookiestr = ';'.join(item for item in cookie)
# print(cookiestr)
#
# headers = {
#     "origin": "https://www.xueqiu.com/",
#     "referer": "https://www.xueqiu.com/",
#     "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
#     'cookie': cookiestr
# }
# re = requests.get("https://www.zhihu.com/collections", headers=headers)
# print(re.status_code)
# print(re.text)
#
# # cookie_dict = {}
# # 格式化打印cookie
# # for cookie in cookie_list:
# #     cookie_dict[cookie['name']] = cookie['value']
# # print(cookie_dict)
# #
# # from http.cookiejar import LWPCookieJar
# #
# # session = requests.session()
# # LWPCookieJar.
# # for cookie in cookies:
# #     print(cookie)
# # session.cookies.set_cookie(cookie=cookie_dict)
#
# # browser.sess
# # response = requests.get("https://www.zhihu.com/collections", cookies=cookie_list)
# # print(response.status_code)
# # print(response.text)
