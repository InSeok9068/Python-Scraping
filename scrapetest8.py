from urllib.request import urlopen
from bs4 import BeautifulSoup

import datetime
import random
import re

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
    # 개정 내역 페이지 URL은 다음과 같은 형식입니다.
    #htpp://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace("/wiki/","")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="
    historyUrl += pageUrl + "&action=history"
    print("history url is:" + historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    # 사용자명 대신 IP 주소가 담긴, 클래스가 mw-anonuserlink인 링크만 찾습니다.
    ipAddresses = bsObj.findAll("a", { "class":"mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

links = getLinks("/wiki/Python_(programming_language)")

while(len(links) > 0 ):
    for link in links :
        print("---------------")
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            print(historyIP)

    newLink = links[random.randint(0, len(links)-1)].attrs["href"]

    link = getLinks(newLink)