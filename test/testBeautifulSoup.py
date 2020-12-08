import re
from bs4 import BeautifulSoup
file = open("./baiduhtml.html","rb")
html = file.read()
bs = BeautifulSoup(html,"html.parser")

# 1.Tag
# 2. NavigableString
# 3. BeautifulSoup 表示整个文档
# 4.Comment 是一个特殊的NavigableString，输出的内容不包含注释符号

print(bs.head)
print(type(bs.head)) #<class 'bs4.element.Tag'> 1.Tag:标签及其内容，默认它所拿到的第一个内容

print(bs.title.string) #2.拿到标签的内容
print(type(bs.title.string)) #<class 'bs4.element.NavigableString'> 2.拿到标签的内容

print(bs.a.attrs)
print(type(bs.a.attrs)) #{'class': ['mnav'], 'herf': 'http://news.baidu.com'}<class 'dict'> 3.拿到一个标签里面所有的属性 attrs

print(type(bs)) #<class 'bs4.BeautifulSoup'> 4.表示整个文档
print(bs.name) #[document]
# print(bs) #拿到所有源代码

print(bs.a.string)
print(type(bs.a.string)) # <class 'bs4.element.Comment'> Comment 是一个特殊的NavigableString，输出的内容不包含注释符号

# 文档的遍历
print("文档的遍历===========================")
print(bs.head.contents)
print(bs.head.contents[1])

for child in bs.body.children:
    print(child)

for child in bs.descendants:
    print(child)

for s in bs.stripped_strings : #获取所有字符串内容
    print(repr(s))

# 搜索文档树
print("搜索文档树===========================")
print(bs.find_all('a'))

for tag in bs.find_all(re.compile("^b")): #正则表达式搜索 找出所有以 b 开头的标签
    print(tag.name)

print(bs.find_all(['a','span'])) #传入列表搜索

print(bs.find_all(id='a2')) #id搜索

print(bs.find_all('a',class_="mnav"))  #class搜索

# 传入一个函数，根据函数的要求搜索
def name_is_exist(tag):
    return tag.has_attr("name")

print(bs.find_all(name_is_exist))

print(bs.find_all(attrs={ "class":"bb"}))

print(bs.find_all(text=['你好']))

print(bs.find_all(text=re.compile("\d"))) #应用正则查找包含特定文本的内容， 本实例查找包含数字的内容

print(bs.find_all('a',limit=2))

print(bs.select('title'))

print(bs.select('.bb'))

print(bs.select('#u2'))

print(bs.select('.mnav ~ .bb')) ##mnav的兄弟节点 bb
print(bs.select('.mnav ~ .bb')[0].get_text()) ##mnav的兄弟节点 bb的内容