#任务完成过程笔记
```
本周整体任务概述:

完成一个极简交互式日记系统,需求如下:
一次接收输入一行日记
保存为本地文件
再次运行系统时,能打印出过往的所有日记
时限: 0wd4~1wd3
发布: 发布到各自仓库的 _src/om2py0w/0wex1/ 目录中
指标:
包含软件使用说明书: README.md
能令其它学员根据说明书,运行系统,完成所有功能

```
##目前状态
在学习thw，进展至ex11。［2015/10/20］

##思路杂货铺（不分条理记录）
- ［2015/10/20］

会用到:raw_input()

参照：python系统里的help(file)

##代码

```
# -*- coding: utf-8 -*-

def mydiarybook():

	readdiary = open('diarybook.txt')	

	print "欢迎来记录你的点滴. 是否需要显示以往日记.(y/n)"

	prediary=raw_input()

	if prediary=="y":
		print readdiary.read()

	readdiary.close()

	writediary = open('diarybook.txt','a')

	print"记录今天的点滴? (y/n)"
	if raw_input()=="y":
		import datetime
		todaydate = datetime.date.today()
		writediary.write(str(todaydate)+"\n")

		print "请直接输入内容,输入q结束本次记录."

		mydiary=raw_input()

		while mydiary != "q":
			writediary.write(mydiary+"\n")
			mydiary=raw_input()

	writediary.close()

	print "再见 :)"

mydiarybook()

```