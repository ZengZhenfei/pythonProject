# f = open("demofile2.txt", "w", encoding="utf-8")
# f.write("Now the file has more content!")
# f.close()
#
# # 追加后，打开并读取该文件：
# f = open("demofile2.txt", "r", encoding="utf-8")
# print(f.read())

# import os
# if  os.path.exists("demofile2.txt"):
#     print("文件存在")
# else:
#     print("文件不存在")

# import pymongo
#
# client = pymongo.MongoClient('localhost', 27017)    # 连接服务器，需要先开启服务
# db = client['mymongo']  # 选择数据库
# # # 插入单条
# # students = db['students']
#
# print(db.list_collection_names())
# # db.students.insert_one({"name": "zuo", "age": 40, "grate": "九年级"})
#
# # 修改单条
# # db.students.update_one(filter={"name": "zuo"}, update={"$set": {"grate": "十年级"}})
#
# # db.students.delete_many({"name":"zuo"}) # 删除全部匹配项
#
# data = db.students.find()   # 查询数据，返回一个游标，通过对游标进行遍历来获取每条数据
# for x in data:
#     print(dict(x))


import requests        #导入requests包
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story" id="myStory">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
# 获取标签名称
print("获取标签名称===================")
print(soup.title.name)
# 获取属性
print("获取属性===================")
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p['name'])
print(soup.p['class'])
# 获取内容
print("获取内容===================")
print(soup.p.string)
# 嵌套选择
print("嵌套选择===================")
print(soup.head.title.string)

print("得到子孙节点===================")
for i, child in enumerate(soup.p.children):
    print(i, child)

# descendants 得到所有子孙节点
print("得到所有子孙节点===================")
for i, child in enumerate(soup.p.descendants):
    print(i, child)

# 父节点
print("父节点===================")
print(soup.a.parent)

print("所有父节点================")
print(type(soup.a.parents))
print(list(enumerate(soup.a.parents)))

print("兄弟节点================")
print('Next Sibling', soup.a.next_sibling)
print('Prev Sibling', soup.a.previous_sibling)
print('Next Siblings', list(enumerate(soup.a.next_siblings)))
print('Prev Siblings', list(enumerate(soup.a.previous_siblings)))

# find_all，顾名思义，就是查询所有符合条件的元素
print("find_all================")
print(soup.find_all(name='p'))
for p in soup.find_all(name='p'):
    for a in p.find_all(name='a'):
        print(a.string)

print("根据标签名查询================")
print(soup.find_all(attrs={'id': 'myStory'}))
print(soup.find_all(attrs={'name': 'dromouse'}))