# [Learn Python the Hard Way](http://learnpythonthehardway.org/book/intro.html)笔记

- 25＊3%4
 
  代表25＊3%＊4，结果为3.
  
- 文字与数字的连接

  cars = 100
  
  print "there are", car, "cars available."
  
  运行以上代码，可显示为
  
  There are 100 cars available.
  
  + 与ruby不同处：
  当需要将文字连接起来时，ruby需要加加号“+”.但python直接用逗号“,”也可以连接（用加号也可以，参照[ex7](http://learnpythonthehardway.org/book/ex7.html)）,另外当数字想要加入文字code中时，需要将数字转化为文字比如说上述print文换成ruby应写成:
  
    print "there are" + car.to_s + "cars available."
 - [ex6](http://learnpythonthehardway.org/book/ex6.html)
   + 如果写成false，会显示如下错误信息。
  
   ```
   Traceback (most recent call last):
  File "ex6.py", line 12, in <module>
    hilarious=false
NameError: name 'false' is not defined
```

   + false负责真伪判断时，首字母应大写，为False
   + 还是不太明白%r %d %s之间什么区别。大概明白这个%是为了把文字插入文字列中间而使用的。
 - 换行问题
   + python
     - 执行print "Jan\nFeb\nMar"则返回如下
     
     ```
     Feb
     Mar
     Apr
     ```
     - 如果忘记打“\n”的“n”，执行print "Jan\Feb\Mar"则会返回结果
     
     ```
     Jan\Feb\Mar
     ```
    
   + ruby
     
     - 执行print "Jan\nFeb\nMar"，则返回如下
     
     ```
     Jan
     Feb
     Mar => nil 
     ```
     - 如果忘记打“\n”的“n”，执行print "Jan\Feb\Mar"则会报错
     
     ```
      Invalid escape character syntax
      print "Jan\Feb\Mar"
     ```
      
     - 有序列 a=["a","g","t"]，执行 print a，则返回如下
     ```
     ["a", "g", "t"] => nil 
     ```
     
     - 执行puts"Jan\nFeb\nMar"，则返回如下（puts会在末尾默认加上换行符），忘记n则会出现跟print忘记n一样的报错
     
      ```
     Jan
     Feb
     Mar
     => nil  
     ```
     
      - 有序列 a=["a","g","t"]，执行 puts a，则返回如下
       
      ```
     a
     g
     t
     => nil
     ```
 - 转义序列・エスケープシーケンス (escape sequence)
    + [wikipedia](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%82%B9%E3%82%B1%E3%83%BC%E3%83%97%E3%82%B7%E3%83%BC%E3%82%B1%E3%83%B3%E3%82%B9)
    + [THW列表](http://learnpythonthehardway.org/book/ex10.html)
    

     
    