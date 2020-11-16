import requests
from simple_salesforce import Salesforce
from bs4 import BeautifulSoup

sf = Salesforce(username='13544205142@sina.cn', password='1qaz2wsx3edc', security_token='')
# query = 'SELECT Id, Name FROM Account LIMIT 10'
# data = sf.bulk.Account.query(query)
# for x in data:
#   print(x)

data = [
      {'Name':'Smith'},
      {'Name':'Jones'}
    ]

sf.bulk.ZhiHu__c.insert(data,batch_size=10000,use_serial=True)

"""
# 爬取知乎的头条并插入SF
data = []
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
        data.extend({"Name":con[i].text})
        sf.ZhiHu__c.create({"Name":con[i].text})
except:
    print("获取失败")

print(len(data))
"""

# sf.bulk.ZhiHu__c.upsert(data, 'Id', batch_size=10000, use_serial=True)


# sf.Account.update('0017F00002RSeZz',{'Name': 'Python Example'})

# data = [
#       {'Id': '0000000000AAAAA', 'Email': 'examplenew2@example.com'},
#       {'Email': 'foo@foo.com'}
#     ]
# sf.bulk.ZhiHu__c.upsert(data, 'Id', batch_size=10000, use_serial=True)

# def prn_obj(obj):
#     print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))
# prn_obj(sf)