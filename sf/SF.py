import requests
from simple_salesforce import Salesforce
from bs4 import BeautifulSoup
import json
sf = Salesforce(username='13544205142@sina.cn', password='1qaz2wsx3edc', security_token='')


# 爬取知乎的头条并插入SF
data = {}
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
        # 创建一个字典
        info_dict = {"Name": (con[i].text)}
        # 把创建的字典放入列表
        data = data.update(info_dict);
        # sf.ZhiHu__c.upsert('Name',{"Name":con[i].text})
except:
    print("获取失败")

print(data)
# data = [{'Name': 'Python Example','Description__c':'I am ok'}]
# sf.bulk.ZhiHu__c.upsert(data, 'Name', batch_size=10000, use_serial=True)


# sf.Account.update('0017F00002RSeZz',{'Name': 'Python Example'})

# data = [
#       {'Id': '0000000000AAAAA', 'Email': 'examplenew2@example.com'},
#       {'Email': 'foo@foo.com'}
#     ]
# sf.bulk.ZhiHu__c.upsert(data, 'Id', batch_size=10000, use_serial=True)

# def prn_obj(obj):
#     print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))
# prn_obj(sf)