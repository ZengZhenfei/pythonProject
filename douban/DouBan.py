
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup
import xlwt
import sqlite3

findLink = re.compile(r'<a href="(.*?)">') #创建正则表达式对象,表示规则(字符串模式) r忽视所有的空格符合 .表示一个字符 *0个或多个字符 ？表示重复前面内容的0次或一次，也就是要么不出现，要么出现一次
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S) #加上re.S表示忽视换行符
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>') #\d表示数字
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

def main():
    baseUrl = "https://movie.douban.com/top250?start="

    dataList = getData(baseUrl)

    savePath = 'top250.xls'

    # saveData(dataList,savePath)

    dbpath = 'movie.db'

    saveDataToDB(dataList,dbpath)

# 爬取网页
def getData(baseUrl):
    dataList = []
    for i in range(0,10):
        url = baseUrl + str(i*25)
        html = askURL(url) #网页源码

        # 逐一解析数据
        soup = BeautifulSoup(html,'html.parser')
        for item in soup.find_all('div',class_='item'): #查找符合要求的字符串，形成列表
            # print(item) #测试：查看电影item所有信息
            data = [] #保持一部电影的所有信息
            item = str(item)

            link = re.findall(findLink,item)[0] #正则匹配电影详情link，获取第一个link即可
            data.append(link)

            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle,item)
            #片名可能只有一个
            if len(titles)==2:
                cTitle = titles[0]
                data.append(cTitle) #添加中文名
                oTitle = titles[1].replace("/","").strip() #去掉无关的符号
                data.append(oTitle) #添加外国名
            else:
                data.append(titles[0])
                data.append(' ') #留空

            rating = re.findall(findRating,item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge,item)[0] #添加评价认输
            data.append(judgeNum)

            inq = re.findall(findInq,item) #评价概述
            if len(inq)!=0:
                data.append(inq[0].replace("。",''))
            else:
                data.append(' ') #留空

            bd = re.findall(findBd,item)[0]
            # bd = re.sub('<br\s+>?/>(\s+)?',' ',bd)
            bd = bd.replace("<br>","").replace("<br/>","").replace("</br>","")
            data.append(bd.strip()) #去掉前后的空格

            # print(data)
            dataList.append(data)
    print(len(dataList))
    return dataList

# 得到指定url的网页内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
    }
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

def saveData(dataList,savePath):
    workbook = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook对象
    worksheet = workbook.add_sheet('top250',cell_overwrite_ok=True)  # 创建工作表
    col = ("电影详情链接","图片链接","影片中文名","影片外国名","评分","评价数","概述","相关信息")
    for i in range(0, 8):
        worksheet.write(0, i, col[i])  # 表格列名
    for i in range(0, 250):
        print('第%d条数据' %(i+1))
        for j in range(0,8):
            data = dataList[i]
            worksheet.write(i+1, j, data[j])  # 表格列名

    workbook.save(savePath)  # 保存数据表

def saveDataToDB(dataList,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in dataList:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'

        sql = '''
            insert into movie250(
                info_link,pic_link,cname,ename,score,rated,instro,info 
            )
            values(%s)'''%",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()

def init_db(dbpath):
    sql = '''
        create table movie250(
            id integer primary key autoincrement,
            info_link text,
            pic_link text,
            cname varchar,
            ename varchar,
            score numeric,
            rated numeric,
            instro text,
            info text
        )
    ''' #创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
    # init_db("movietest.db")
    print("爬取完毕")
