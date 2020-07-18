# 简介

> XPath即为XML路径语言（XML Path Language），它是一种用来确定XML文档中某部分位置的语言。(来源于[百度百科](https://baike.baidu.com/item/XPath/5574064?fr=aladdin))
# 常用规则
| 符号 | 含义 |
|--|--|
| 节点名称 | 选取此节点以及所有子节点 |
| / | 选取此节点的子节点 |
| // | 选取子节点的子孙节点 |
| \. | 选取当前节点 |
| \.\. | 选取当前节点的父节点 |
| @ | 选取属性 |
# XPath使用方法(lxml.etree)
导入lxml库：

```python
from lxml import etree
```

**test.html**

```python
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
```

从文件中获取HTML：
```python
html = etree.parse('./test.html', etree.HTMLParser())
```

## 01 获取父节点


```python
# result = html.xpath('//a[@href="link4.html"]/../@class') # 使用/..来获取选中节点的父节点
result = html.xpath('//a[@href="link4.html"]/parent::*/@class') # 使用/parent::来获取选中节点的父节点
print(result)
```

    ['item-1']


## 02 获取节点文本


```python
result = html.xpath('//a[@href="link1.html"]/text()') # 获取某个节点中的文本内容使用/text()
print(result)
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)
```

    ['first item']
    ['first item', 'fifth item']


## 03 属性多值匹配


```python
result = html.xpath('//a[contains(@href, "html")]/text()') # 使用contains()函数来进行属性多值匹配
print(result)
```

    ['first item', 'second item', 'third item', 'fourth item', 'fifth item']


## 04 多属性匹配


```python
text = '<li class="li li-first" name="item"><a href="link.html">first item</a></li>'
text_html = etree.HTML(text)
result = text_html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()') # 使用and添加需要匹配的属性
print(result)
```

    ['first item']
