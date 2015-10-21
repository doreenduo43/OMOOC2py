# -*- coding: utf-8 -*-

def mydiarybook():

	f = file('diarybook.txt', 'w')	
	print "欢迎来记录你的点滴. 是否需要显示以往日记.(y/n)"

	import datetime
	today = datetime.date.today()

	if raw_input()=="y":
		for row in f:
			print row

	else:
		if today in f= True:
			f.write(today)
			while raw_input() != "y":
				f.write(raw_input)
				print "是否结束今天的记录? 结束请输入y, 继续记录请直接输入."

		print "请告诉我你的今天. (请直接输入内容,按回车键结束一次输入. )"
		todaydiary=raw_input()

		while todaydiary != "y":
			f.write(todaydiary)
			print "是否结束今天的记录? 结束请输入y, 继续记录请直接输入."


f.close()

print “再见 :)”

mydiarybook()

