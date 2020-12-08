import re

#有模式对象
pat = re.compile('AA')
m = pat.search('AAAAAAAAA')
print(m)

#没有模式对象
m2 = re.search('AA','AAyyyyyyy');
print(m2)

print(re.findall('a','a5454545a'))

print(re.findall('[A-Z]','a54A545SE45a')) #找到所有大写字母

print(re.findall('[A-Z]+','a54A545SE45a')) #找到所有大写字母，有组合的

print(re.sub('a','A','a5454545a')) #找到a用A替换