import requests
from bs4 import BeautifulSoup
pre={'User-agent':'Mozilla/5.0'}
try:
    res=requests.get("https://www.zhihu.com/billboard",headers=pre)
    res.raise_for_status
    rep=res.text
except:
    print("连接失败")
try:
    soup=BeautifulSoup(rep,"html.parser")
    con=soup.find_all('div',class_="HotList-itemTitle")
    for i in range(len(con)):
        print(con[i].text)
except:
    print("获取失败")