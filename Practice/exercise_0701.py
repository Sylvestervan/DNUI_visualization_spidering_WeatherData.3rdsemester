from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
# import random
# import datetime
# import scrapy
# random.seed(datetime.datetime.now())


# --- 1
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), features="lxml")

print(bsObj.prettify())
print(bsObj.h1)
print(bsObj.html.body.h1)
print(bsObj.body.h1)
print(bsObj.html.h1)

# --- 2
html1 = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj1 = BeautifulSoup(html1.read(), features="lxml")

nameSet = set()
nameList = bsObj1.findAll("span", {"class": "green"})
for name in nameList:
    nameSet.add(name.get_text())

print(nameSet)

nameList1 = bsObj1.findAll(string="the prince")
print(len(nameList1))

allText = bsObj1.findAll(id="text")
if allText:
    print(allText[0].get_text())

# --- 3
html3 = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj2 = BeautifulSoup(html3, features="lxml")
for child in bsObj2.find("table", {"id": "giftList"}).children:
    print(child)

bsObj3 = BeautifulSoup(html3, features="lxml")
giftListTable = bsObj3.find("table", {"id": "giftList"})

if giftListTable and giftListTable.tr:
    print("\nSiblings of the first row in the gift list table:")
    for sibling in giftListTable.tr.next_siblings:
        print(sibling)
else:
    print("\nGift list table or first row not found.")

bsObj4 = BeautifulSoup(html3, features="lxml")
images = bsObj4.findAll("img", {"src": re.compile(r"\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])

html.close()
html1.close()
html3.close()

# --- 4

# def get_links(article_url):
#     html = urlopen("https://baike.baidu.com"+article_url)
#     bsObj = BeautifulSoup(html, features="lxml")
#     return bsObj.find("div", {"class":"lemma-relation-item"}).findAll("a", href=re.compile("^(/item/)((?!:).)*$"))
#
# links = get_links("/item/李大钊/115618")
# while len(links) > 0:
#     newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
#     print(newArticle)
#     links = get_links(newArticle)

# --- 5
# pages = set()
#
# def get_link(pageUrl):
#     global pages
#     html = urlopen("" + pageUrl)
#     bsObj = BeautifulSoup(html, features="lxml")
#     for link in bsObj.findAll("a", herf=re.compile("^(/item/)")):
#         if "href" in link.attrs:
#             newPage = link.attrs["href"]
#             print(newPage)
#             pages.add(newPage)
#             get_link(newPage)
# get_link("/item/%E6%9D%8E%E5%A4%A7%E9%92%BA/115618")