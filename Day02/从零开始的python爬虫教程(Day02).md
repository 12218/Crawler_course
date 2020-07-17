@[TOC](目录)
# 爬虫的概念

> 网络爬虫（又称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常的称为网页追逐者），是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。另外一些不常使用的名字还有蚂蚁、自动索引、模拟程序或者蠕虫。(<a href="https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711?fromtitle=%E7%88%AC%E8%99%AB&fromid=22046949&fr=aladdin">来源于百度百科</a>)

爬虫的过程有三步：

 1. 获取网页
 2. 获取信息
 3. 保存信息
# 爬虫常用库
**请求库**
	urllib
	requests
**解析库**
	lxml
	BeautifulSoup
**自动化**
	Selenium
**框架**
	pyspider
	scrapy

# Requests库基础用法
## 01 安装
在命令行中输入：

```python
pip install requests
```
即可。

如果速度太慢，可以使用中科大的源：

```powershell
pip install --index https://pypi.mirrors.ustc.edu.cn/simple requests
```
安装完成之后，可以在python命令行输入“import requests”检验。
## 02 GET请求基本使用
#### (1) 基本操作
```python
import requests

response = requests.get('https://httpbin.org/get')
print(response.text)
```
请求结果为：

```javascript
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.23.0", 
    "X-Amzn-Trace-Id": "Root=1-5f107d75-db1210ba8a626de146e579e8"
  }, 
  "origin": "***.***.***.**", 
  "url": "https://httpbin.org/get"
}
```
这里的 requests.get 是用get方法请求网页。

get请求返回了一个response对象，这个对象包含了请求的类型、状态码、请求类型、cookie、内容。

以上实例中response.text是获取返回对象中的文字部分内容。

**以下为get请求的部分用法**

```python
import requests

response = requests.get('https://httpbin.org/get')
print(response)
print(type(response)) # response 类型
print(response.text) # 内容
print(response.content) # 二进制内容(可用于获取视频、图片)
print(response.status_code) # 状态码
print(response.cookies) # cookie
```

```python
# response
<Response [200]>
# type(response)
<class 'requests.models.Response'>
# response.text
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.23.0", 
    "X-Amzn-Trace-Id": "Root=1-5f108010-4f6006d11ae9755b42e9c0ec"
  }, 
  "origin": "182.116.195.12", 
  "url": "https://httpbin.org/get"
}
# response.content
b'{\n  "args": {}, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.23.0", \n    "X-Amzn-Trace-Id": "Root=1-5f108010-4f6006d11ae9755b42e9c0ec"\n  }, \n  "origin": "182.116.195.12", \n  "url": "https://httpbin.org/get"\n}\n'
# response.status_code
200
# response.cookies
<RequestsCookieJar[]>
```
#### (2) 携带参数
我们在浏览网页的时候经常会发现申请的网页需要携带参数。例如：

```
https://www.baidu.com/s?wd=%E7%88%AC%E8%99%AB
```

其中wd就是携带的一个参数。

requests可以携带参数进行get请求，用法是将参数以字典的方式传入。

```python
import requests

param = {
    'language':'python',
    'date':2020
    }
response = requests.get('https://httpbin.org/get', params = param)
print(response)
print(response.text)
```
结果为：

```python
<Response [200]>
{
  "args": {
    "date": "2020", 
    "language": "python"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.23.0", 
    "X-Amzn-Trace-Id": "Root=1-5f10f4ab-70ef76c5173e4e72b835dfef"
  }, 
  "origin": "***.***.***.**", 
  "url": "https://httpbin.org/get?language=python&date=2020"
}
```
可以看到，申请的url和参数language、date构成了一个url。

```python
https://httpbin.org/get?language=python&date=2020
```
#### (3) 添加请求头
我们如果使用上面的方式去请求一些网页，会发现有些网页无法请求到我们在网页看到的内容。

其中一个原因是，它识别出请求方并不是一个浏览器，而是一个python程序，可以看到上面程序的结果，请求头"User-Agent"是"python-requests/2.23.0"。

故此我们可以使用下面的方法进行请求头的添加：

```python
import requests

param = {
    'language':'python',
    'date':2020
    }

header = {'user-agent':'Mozilla/5.0'}

response = requests.get('https://httpbin.org/get', params = param, headers = header)
print(response)
print(response.text)
```
这样请求出来的请求头就是Mozilla/5.0。
## 03 POST请求基本使用
post请求的用法与get相似，只需要将requests.get换成requests.post就行了。

它还有一些特殊的用法，例如文件的上传等等：

```python
import requests

file = {
    'file':'01.png'
    }

response = requests.post('https://httpbin.org/post', files = file)
print(response)
print(response.text)
```

```python
<Response [200]>
{
  "args": {}, 
  "data": "", 
  "files": {
    "file": "01.png"
  }, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "146", 
    "Content-Type": "multipart/form-data; boundary=92058415dea9dc33df31608265fffb6f", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.23.0", 
    "X-Amzn-Trace-Id": "Root=1-5f10f8f9-0d04b1f17e223a03f35f9751"
  }, 
  "json": null, 
  "origin": "182.116.195.12", 
  "url": "https://httpbin.org/post"
}
```

