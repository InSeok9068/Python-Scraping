from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

#자식 다루기
for child in bsObj.find("table",{"id":"giftList"}).children:
     print(child)

#형제 다루기
for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)

#부모 다루기
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())