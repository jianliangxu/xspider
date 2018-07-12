# import requests
# import time
#
# if __name__ == '__main__':
#     agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
#     header = {
#         'User-Agent': agent
#     }
#     response = requests.get("http://ladyxingbs.com/portal.html", headers=header)
#     print(response.status_code)
#     if not response.status_code == '200':
#         time.sleep(10)
#         response = requests.get("http://ladyxingbs.com/portal.html", headers=header)
#         print(response.status_code)
#