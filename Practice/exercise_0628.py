#TODO# 06,28,24 --- 爬取网页数据

'''import urllib.request
response = urllib.request.urlopen("https://www.csdn.net/")
data = response.readlines()
with open("csdn.html", "wb") as fp:
    fp.writelines(data)'''
import urllib.request
import re

def getlink(url):
    headers = ("User-Agent", "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]

    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = file.read().decode('utf-8')

    pat = r'(https?://[^\s"\'<>]+)'      # 正则表达式
    link = re.compile(pat).findall(data)
    Link = list(set(link))
    return Link

url = "https://www.csdn.net/"
linklist = getlink(url)

for i in linklist:
    print(i)

#todo# beautifulsoup4 --- 爬取另一个形式。

import requests
from bs4 import BeautifulSoup


def get_questions(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    data = response.content.decode('utf-8')

    soup = BeautifulSoup(data, 'html.parser')

    questions = soup.find_all('h2')

    question_texts = []
    for question in questions:
        question_texts.append(question.get_text(strip=True))

    return question_texts


url = "https://www.zhihu.com/"
question_list = get_questions(url)

for question in question_list:
    print(question)

