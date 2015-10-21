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