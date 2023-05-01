import requests
from bs4 import BeautifulSoup

header = {'User-agent' : 'Mozila/2.0'}
keword = input("Enter what you want : ")
url = "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={}".format(keword)
response = requests.get(url ,headers=header)

html = response.text

#html 번역
soup = BeautifulSoup(html, 'html.parser')

# class명으로 가져옴
titles = soup.select('.news_tit')

for i in titles:
    print(i.text)