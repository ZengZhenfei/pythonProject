
import xlwt

# workbook = xlwt.Workbook(encoding="utf-8") #创建workbook对象
# worksheet = workbook.add_sheet('sheet1') #创建工作表
# worksheet.write(0,0,'hello') #写入数据 行 列 内容
# workbook.save('students.xls') #保持数据表

# workbook = xlwt.Workbook(encoding="utf-8") #创建workbook对象
# worksheet = workbook.add_sheet('sheet2') #创建工作表
# for i in range(0,9):
#     for j in range(0,i+1):
#         worksheet.write(i,j,"%d * %d = %d"%(i+1,j+1,(i+1)*(j+1))) #写入数据 行 列 内容
# workbook.save('chengfa.xls') #保存数据表

col = ("电影详情链接","图片链接","影片中文名","影片外国名","评分","评价数","概述","香港信息")
print(len(col))