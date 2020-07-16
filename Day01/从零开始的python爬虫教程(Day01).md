# HTTP简介
## 01HTTP和HTTPS
我们在访问某一个网页时，总是能看到申请的url是以http或者https开头的。

http和https都是访问资源时的协议类型。
它们不同的地方在于https是经过ssl加密的http。

这两者都是我们写爬虫时常用的请求过程。
## 02查看请求
查看请求的方法很简单，只需要在某一个网页右键，点击“检查”；或是按“F12”进入开发者模式。

下图中红色箭头指向的每一条都是一个请求。
![http](https://img-blog.csdnimg.cn/20200716232047330.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDMzODc4MA==,size_16,color_FFFFFF,t_70)
在上图中的第一列Name是请求的名称。
第二列Status是请求的状态码。当状态码为200时，请求为正常请求。
第三列时请求的文档类型。

我们点击某一条请求，就能看到这一条请求的细则。
![请求](https://img-blog.csdnimg.cn/20200716233027387.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDMzODc4MA==,size_16,color_FFFFFF,t_70)
# 网页基础
## 01 网页的组成部分
网页由HTML、CSS、JavaScript三部分组成。

其中HTML构建框架，CSS负责页面的美化、位置控制，JavaScript负责让网页有功能、控制网页的运转。
## 02 网页的结构与标签
以下是一个简单的网页代码：

```css
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
```
当它显示在网页中，是这个样子：![HTML](https://img-blog.csdnimg.cn/20200716234346562.png)
|标签| 作用 |
|--|--|
| html | 最外层包裹所有标签元素 |
| head | 网页头 |
| body | 网页的正文 |
| p | 在网页中是一个个段落 |
| a | 网页中的链接 |
## 03 网页的属性
在有的标签中包含着class、id、style等属性。

```css
<a class="sister" href="http://example.com/lacie" id="link2">
```

其中class、id为CSS等区分各个元素的一个名称。

style是CSS对这个标签进行美化。

这些属性都能成为爬虫抓取特定标签的重要“依凭”。
