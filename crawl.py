import sys
import requests
from bs4 import BeautifulSoup


def crawler():
    # 搜尋字詞
    query = 'ai概念股'

# 設定hearers
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

# 執行爬蟲下載搜尋結果頁面標題
    url = 'https://www.google.com/search?q=' + query
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find_all('div', class_='g')
    title = [elem.find('h3').getText() for elem in content]
    link = [ele.find('a').get('href') for ele in content]
    output = ''
    # 輸出查詢結果
    # print('Google搜尋結果頁面共有以下標題與連結:')

    for elem, ele in zip(title, link):

        output += '{}\n{}\n'.format(elem, ele)
        # print("- " + elem + "\n" + ele)
    return output


# import requests
# import sys
# from bs4 import BeautifulSoup
# import numpy as np

# # def scrape_news():
# #     url = 'https://news.sina.com.cn/'
# #     response = requests.get(url)

# #     if response.status_code == 200:
# #         soup = BeautifulSoup(response.text, 'html.parser')
# #         headlines = soup.find_all(
# #             'a', {'target': '_blank', 'suda-data': 'key=news_headline'})

# #         for headline in headlines:
# #             title = headline.text.strip()
# #             link = headline.get('href')
# #             print(f"{title} - {link}")
# #     else:
# #         print('無法獲取新聞資訊。')


# # if __name__ == '__main__':
# #     scrape_news()


# # 搜尋字詞

# headers = {
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 '}

# # 執行爬蟲下載搜尋結果頁面標題
# url = 'https://www.bnext.com.tw/'
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, 'html.parser')
# content = soup.find(
#     'div', class_="col-sm-6 col-md-4 col-lg-4 col-12 BG-Col")
# print(content)
# content = soup.find_all(
#     'a', class_="lst px-0 py-2 d-flex align-center v-list-item v-list-item--link theme--light")[0].find_all('div').getText()
# print(content)
# for title in content:
#     print(title.a.string)
#     print(title.a.get("href"))
# title = [ele.find('a').gethref() for ele in content]
# text = [ele.find('span').getText() for ele in content]

# print('目前特價的品項包含：')
# [print(ele) for ele in title]
# [print(ele) for ele in price]


# content = soup.find_all('div', class_='g')
# title = [elem.find('h3').getText() for elem in content]

# # 輸出查詢結果
# print('Google搜尋結果頁面共有以下標題:')
# [print(elem) for elem in title]
