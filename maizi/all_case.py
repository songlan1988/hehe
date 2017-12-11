#-*-coding=utf-8-*-
import os

#列出某个文件夹下的所有case，这里用的是python
#所在py文件运行一次后会产生一个pyc副本

caselist=os.listdir("F:\\songlan\\project\\test_case")
for a in caselist:
	s=a.split('.')[1]
	if s=='py':
		#此处执行dos命令并将结果保存到log.txt
		os.system('F:\\songlan\\project\\test_case\\%s 1>>log.txt 2>&1'%a)
