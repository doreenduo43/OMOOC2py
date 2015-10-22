#简易日记本使用
##功能

- 可**查看**以往的日记。

- 可**写入**新的日记。

##使用

###前提

本文件基于Python 2.7.10创作。

使用前请确保电脑中已经配置好python。

###基本使用

请[下载 diarybook.py](https://github.com/doreenduo43/OMOOC2py/blob/master/_src/om2py0w/0wex1/diarybook.py) 文件至本地。

执行 python diarybook.py

无需创建日记本文件，执行上述口令会自动创建txt日记文件。

- 以往内容显示

屏幕显示：欢迎来记录你的点滴. 是否需要显示以往日记.(y/n)

如输入y。

则会显示以往日记内容。如以前没有记录则会显示空行。

- 记录新内容

可直接输入想记录的内容。

想另起一行时，输入回车后可继续输入。

结束输入时请输入q并回车。

- 其他

彻底删除日记本
请在保存diarybook.py的路径中找到diarybook.txt。可直接删除该文件。

删除该文件后，如再次执行 python diarybook.py，则会在原有位置创建新的空白日记本。

修改日记内容
请在保存diarybook.py的路径中找到diarybook.txt。打开后可修改内容。但请勿更改文件后缀名。

###反馈（意见与吐槽）
请在此gitbook下留言，或在github此文件相关[issue](https://github.com/doreenduo43/OMOOC2py/issues/2)中提交。

##下一步完善方向

本文件目前会把每一次记录的日期自动添加至本次记录的最上方。

当一天之内有多于1次的记录时，会显示多次当天的日期。

下一步改进是，当一天即使有多次记录，也只会在当天第一次时记录一次日期。计划用find命令。