# 导入库
import jieba.analyse  # 导入关键字提取库
import pandas as pd  # 导入pandas
import newspaper

# 读取文本数据
# 获取文章 银保监会出台新政为例
article = newspaper.Article('https://mp.weixin.qq.com/s?__biz=MjM5MDU3NDQ2MA==&mid=2651281698&idx=5&sn=56017e3a340b1e8b1ab5c42702f9e48a&chksm=bdb14b318ac6c227edb87adbcf2a84845a2bacf252255d448f1d8db345128e15cd70728b2fc3&scene=0&xtrack=1&key=29495e6e9fe7db132cdcaa3d45a8670330f354de528bcb930605c9a9b7656c30e3ff31a73617431d39f054eaf880d21b5e5a730a8c2b7a6ba83f5d771ca236a471dc95430cd11c990dfd5157962901c4d01fb929affd42871e518d20826e001f99fb36dacc13d1ae9873139e354c57fb2fc4a1ef3ca630db5d18f2eb38c7fa50&ascene=1&uin=Mjg0OTQ2MjUwOQ%3D%3D&devicetype=Windows+10+x64&version=6300002f&lang=zh_CN&exportkey=A%2FikVlyuRRk1Le5lQ%2BZUWSE%3D&pass_ticket=jyI5RrL%2Bp8eufZhKw1EjO7AcNIJtuqxR1jqXZsGr8mBIGwe%2BNGDBR9lcl%2BfOIZji&wx_header=0',
                            language='zh')
# 下载文章
article.download()
# 解析文章
article.parse()
# 对文章进行nlp处理
article.nlp()
# nlp处理后的文章拼接
string_data = "".join(article.keywords)


# 关键字提取
def get_key_words(string_data, how=''):
    # topK：提取的关键字数量，不指定则提取全部；
    # withWeight：设置为True指定输出词对应的IF-IDF权重
    if how == 'textrank':
        # 使用TextRank 算法
        tags_pairs = jieba.analyse.textrank(string_data, topK=5, withWeight=True)  # 提取关键字标签
    else:
        # 使用TF-IDF 算法
        tags_pairs = jieba.analyse.extract_tags(string_data, topK=5, withWeight=True)  # 提取关键字标签
    tags_list = []  # 空列表用来存储拆分后的三个值
    for i in tags_pairs:  # 打印标签、分组和TF-IDF权重
        tags_list.append((i[0], i[1]))  # 拆分三个字段值
    tags_pd = pd.DataFrame(tags_list, columns=['word', 'weight'])  # 创建数据框
    return tags_pd


keywords = get_key_words(string_data)
print("#####################TF-IDF####################")
print(keywords)

keywords_tr = get_key_words(string_data, how='textrank')
print("#####################textrank####################")
print(keywords_tr)