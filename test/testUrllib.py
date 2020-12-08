import urllib.request
import urllib.parse
# url = "http://httpbin.org/post"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({"name":"aiden"}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

url = "http://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}
req = urllib.request.Request(url=url,headers=headers,method="GET")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))