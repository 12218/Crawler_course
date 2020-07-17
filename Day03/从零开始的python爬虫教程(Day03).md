# 简介

> 正则表达式，又称规则表达式。（英语：Regular Expression，在代码中常简写为regex、regexp或RE），计算机科学的一个概念。正则表达式通常被用来检索、替换那些符合某个模式(规则)的文本。(来源于<a href="https://baike.baidu.com/item/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F/1700215?fr=aladdin">百度文库</a>)
# 常用匹配规则
**<font color="red">详细匹配规则请参考<a href="https://www.runoob.com/regexp/regexp-tutorial.html">菜鸟教程</a>。</font>**
## 01 普通字符
在正则表达式里面写入普通字符，则可以直接匹配出来。
## 02 元字符
|字符| 作用 |
|--|--|
| \w | 匹配字母、数字、下划线 |
| \W | 匹配非字母、非数字、非下划线 |
| \s | 匹配空白字符 |
| \S | 匹配非空白字符 |
| \d | 匹配数字 |
| \D | 匹配非数字 |
| \A | 匹配字符串开头 |
| \z | 匹配字符串结尾(包括换行) |
| \Z | 匹配字符串结尾(不包括换行) |
| \n | 匹配换行符 |
| \t | 匹配制表符 |
| ^ | 匹配字符串开头 |
| $ | 匹配字符串结尾 |
| * | 匹配0个以上的任意字符 |
| + | 匹配1个以上的任意字符 |

## 03 限定符
|字符| 作用 |
|--|--|
| [] | 匹配一组字符，匹配[]内的任意字符 |
| () | 匹配括号内的表达式，或一个组 |
| \| | a\|b匹配a或b |
| {n} | 匹配n个前面的表达式 |
| ? | 匹配0-1个前面的表达式定义的片段 |
| {m,n} | 匹配m-n个前面的表达式定义的片段 |

## 04 特殊字符
由于正则表达式里面的很多字符都有其独特的作用，故此，需要用一种方式来匹配这些有作用的字符。

就是在这些字符前面加上“\”。

这些字符包括：
|特殊字符| 匹配方法 |
|--|--|
| ^ | \\^ |
| * | \\* |
| + | \\+ |
| . | \\. |
| ? | \\? |
| \| | \\\| |
| [] | \\[ |
| {} | \\{ |
| () | \\(、\\) |
| \ | \\\ |
## 05 修饰符
修饰符为正则表达式里面添加的标志，用于控制匹配模式。
|修饰符| 作用 |
|--|--|
| re.I | 匹配对大小写不敏感 |
| re.M | 可以匹配多行 |
| re.S | 使.可以匹配换行 |
| re.U | 匹配Unicode解析字符 |

# re库的部分方法
## 01 match
match会从字符串的头开始进行匹配，如果开头不匹配，则返回None。

```python
sentence = "Hello! I'm 12218. ✧٩(ˊωˋ*)و✧"
```

```python
text = re.match(r'^Hello.*?(\d+).*', sentence)
print(text)
print(text.group())
print(text.group(0)) # group()和group(0)作用一样，都是匹配到的全部字符串
print(text.group(1)) # group(1)是取匹配到的第一个字符串
```

## 02 search
search会从字符串的任意位置开始进行匹配，如果非发现匹配部分，则返回None。

```python
text = re.search(r'ello.*?(\d+).*', sentence) # search会从字符串的任意位置开始进行匹配
print(text)
print(text.group())
print(text.group(0))
print(text.group(1))
```

## 03 findall
findall是从字符串里面寻找所有符合条件的匹配部分，匹配部分返回一个列表类型，如果非发现匹配部分，则返回空列表。

```python
text = re.findall(r'\d', sentence) # findall是从字符串里面寻找所有符合条件的匹配部分
print(text)
print(type(text))
```

## 04 compile
compile的方法是用于将一个正则表达式编译成一个正则表达式对象，以便重复使用。

```python
content = re.compile(r'.*?(\d+).*?') # 将一个正则表达式编译成一个正则表达式对象，可以更方便地使用
text = re.findall(content, sentence)
print(text)
```