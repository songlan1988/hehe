#-*-coding=utf-8-*-
import unittest
#这里需要导入测试文件
from test_case import *
import HTMLTestRunner
import os,time

listaa='F:\\songlan\\hehe\\maizi\\test_case'
def creatsuitel():
	testunit=unittest.TestSuite
	#discover方法定义
	discover=unittest.defaultTestLoader.discover(listaa,
		pattern='start_*.py',
		top_level_dir=None)

	#discover方法筛选出来的用例，循环添加到测试套件中
	for test_suite in discover:
		for test_case in test_suite:
			testunit.addTests(test_case)
			print(testunit)
	return testunit

alltestnames=creatsuitel()

			



# testunit=unittest.TestSuite()

# #将测试用例加入到测试（容器）套件中
# testunit.addTest(unittest.makeSuite(baidu.Baidu))
# testunit.addTest(unittest.makeSuite(youdao.Youdao))

#取前面时间
now=time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime(time.time()))

#定义报告存放路径，支持相对路径
filename='F:\\songlan\\hehe\\maizi\\report\\'+now+'report.html'
fp=open(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(
	stream=fp,
	title=u'百度测试报告',
	description=u'用例执行情况：')

runner.run(alltestnames)
# runner.run(testunit)


