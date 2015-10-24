#编程思想的具象
   ～如何科学的进入思维升级状态

##流水账
   
###REPL
  
 - dir()
 - help()
 - read-eval-print loop

###搜索

 - **Google**
 
###框架构造

 - 头部声明
 
 - 全局引用
 
 - 全局变量
 
 - 函式撰写
 
 - 自检区
   
###pythonic
>[The Zen of Python](https://www.python.org/dev/peps/pep-0020/)

- Pythonista八荣八耻

###GUI之Tkinter

###PS
>所有东西都能教授，但！求知欲和学习能力除外。
 
 - 屏幕顶端出现的 5+-2
 - M$(Microsoft)
 - putty
 - keep calm and use the force **原力**
 - keep calm and sleep

##TOP有3
###1.Google搜索语法
延续上周学会“渔”的话题，这周又说到了大家搜索能力令人忧伤的事情。下面这些搜索功能虽然自己都知道，但真用的不多，都是偷懒在关键字之间加空格解决。

参考网址：某人简书 [Google搜索语法](http://www.jianshu.com/p/37fe4f1381ef)

我来精简了一下：

- 基本符号： +, -, or
- related:www.网站A.com

  搜索与网站A有相似内容的网页
- define:苹果

  搜索“苹果”的定义。
- filetype:pdf

  查找pdf的文件。支持PDF,doc,xls,ppt等文件格式。
- 图片搜索

  可直接上传图片文件搜索，或粘贴图片所在网址。
- 苹果+site:www.douban.com
  只在douban里搜索“苹果”。
  

###2.框架构造的自检区
其他几个虽然不能说理解怎么深，但基本上也算是明白在干嘛。至于最后的自检区的 if __name__=='__main__'，真的完全没看懂。大妈也解说了一下，大概如下：
>当调用一个函数／脚本时，这对于文件／脚本来说是一种测试，每一个文件是一个模块，这个模块可以被其他文件引用。用if __name__=='__main__'时，这个单元当被引用时不会被触发。

每个字都懂，可是整体意思，却，没看懂（摊手）。
于是查了下：

- [python中if __name__ == "__main__"：用法解析](http://keliang.blog.51cto.com/3359430/649318)

  (这个讲得是比较简单的,但没给例子，也是昏昏沉沉。)
- [大步's Blog－－if __name__== “__main__” 的意思(作用)python代码复用](http://www.dabu.info/if-__-name__-__main__-mean-function-python-code-reuse.html)

  （这个用了几个分解步骤分解讲解，明白了。）  

###3.Keep calm and ◯◯◯.
虽说这个句式是“保持**冷静**，然后◯◯◯”。

怎么冷静呢？抓狂的时候就失去理智了，用心理学的话说，认知资源耗尽了。