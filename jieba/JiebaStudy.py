from jieba.analyse import *

with open('sample.txt', encoding='utf-8') as f:
    data = f.read()

# for keyword, weight in extract_tags(data, withWeight=True):
#     print('%s %s' % (keyword, weight))

for keyword, weight in textrank(data, withWeight=True):
    print('%s %s' % (keyword, weight))