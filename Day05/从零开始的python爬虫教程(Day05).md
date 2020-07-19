@[TOC](目录)
# BeautifulSoup简介

> Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库.它能够通过你喜欢的转换器实现惯用的文档导航,查找,修改文档的方式.Beautiful Soup会帮你节省数小时甚至数天的工作时间.(摘自[BeautifulSoup中文文档](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/))

和lxml库一样，BeautifulSoup库是一个功能强大的解析库，可以方便地提取各个网页元素，是爬虫的一大利器。

安装BeautifulSoup库：

```python
pip install bs4
```
BeautifulSoup在解析网页时需要**解析器**。以下是一些BeautifulSoup库支持的解析器：
| 解析器 | 使用方法 |
|--|--|
| python标准库 | BeautifulSoup(html, "html.parser") |
| lxml HTML解析器 | BeautifulSoup(html, "lxml") | 
| lxml xml解析器 | BeautifulSoup(html, "xml") | 
| html5lib | BeautifulSoup(html, "html5lib") | 
# BeautifulSoup用法

导入BeautifulSoup库：
```python
from bs4 import BeautifulSoup
import re
```
实例html网页代码：

```python
html = """
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title" name="dromouse">
   <b>
    The Dormouse's story
   </b>
  </p>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">
    <!-- Elsie -->
   </a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
   </a>
   and
   <a class="sister" href="http://example.com/tillie" id="link3">
    Tillie
   </a>
   ;
and they lived at the bottom of a well.
  </p>
  <p class="story">
   ...
  </p>
 </body>
</html>
"""
```

## 基本用法


```python
soup = BeautifulSoup(html, 'lxml')
print(soup.title.string.strip()) # 使用string来获取标签里面的字符串
print(soup.p.name) # name获取标签名称
print(soup.p.attrs) # attrs获取标签属性
```

    The Dormouse's story
    p
    {'class': ['title'], 'name': 'dromouse'}


## 嵌套选择


```python
print(soup.head.title.string.strip()) # 可以使用[标签1.标签2]的形式对标签1下一层节点进行选择
```

    The Dormouse's story


## 关联选择(直接获取所选元素的子节点)


```python
print(soup.p.contents)
```

    ['\n', <b>
        The Dormouse's story
       </b>, '\n']



```python
print(soup.body.children)
for child in soup.body.children:
    print(child)
    print('---------')
```

    <list_iterator object at 0xaddcbe70>



    ---------
    <p class="title" name="dromouse">
    <b>
        The Dormouse's story
       </b>
    </p>
    ---------


    ---------
    <p class="story">
       Once upon a time there were three little sisters; and their names were
       <a class="sister" href="http://example.com/elsie" id="link1">
    <!-- Elsie -->
    </a>
       ,
       <a class="sister" href="http://example.com/lacie" id="link2">
        Lacie
       </a>
       and
       <a class="sister" href="http://example.com/tillie" id="link3">
        Tillie
       </a>
       ;
    and they lived at the bottom of a well.
      </p>
    ---------



    ---------
    <p class="story">
       ...
      </p>
    ---------



    ---------


## find_all find_all(name, attrs, recursive, text, **kwargs)

(1)name


```python
print(soup.find_all(name='b')) # name为标签类型
```

    [<b>
        The Dormouse's story
       </b>]


(2)attrs


```python
print(soup.find_all(attrs = {'class':'sister'})) # 根据标签属性选择标签
```

    [<a class="sister" href="http://example.com/elsie" id="link1">
    <!-- Elsie -->
    </a>, <a class="sister" href="http://example.com/lacie" id="link2">
        Lacie
       </a>, <a class="sister" href="http://example.com/tillie" id="link3">
        Tillie
       </a>]



```python
print(soup.find_all(class_ = 'sister')) # 使用标签属性名称加“_”效果相同
```

    [<a class="sister" href="http://example.com/elsie" id="link1">
    <!-- Elsie -->
    </a>, <a class="sister" href="http://example.com/lacie" id="link2">
        Lacie
       </a>, <a class="sister" href="http://example.com/tillie" id="link3">
        Tillie
       </a>]


(3)text


```python
print(soup.find_all('a', {'href': re.compile(r'http://(.*?)')})) # 匹配标签属性的方法
```

    [<a class="sister" href="http://example.com/elsie" id="link1">
    <!-- Elsie -->
    </a>, <a class="sister" href="http://example.com/lacie" id="link2">
        Lacie
       </a>, <a class="sister" href="http://example.com/tillie" id="link3">
        Tillie
       </a>]



```python
print(soup.find_all(text = re.compile('Dormouse'))) # 匹配标签内容的方法
```

    ["\n   The Dormouse's story\n  ", "\n    The Dormouse's story\n   "]


## CSS选择器


```python
print(soup.select('.sister')) # 选择所有class为sister的标签
```

    [<a class="sister" href="http://example.com/elsie" id="link1">
    <!-- Elsie -->
    </a>, <a class="sister" href="http://example.com/lacie" id="link2">
        Lacie
       </a>, <a class="sister" href="http://example.com/tillie" id="link3">
        Tillie
       </a>]
