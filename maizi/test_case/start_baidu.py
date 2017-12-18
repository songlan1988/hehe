# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.action_chains import ActionChains

import HTMLTestRunner
class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #百度搜索用例
    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)


    #百度设置用例
    def test_baidu_set(self):
    	driver=self.driver
    	driver.get(self.base_url+"/gaoji/preferences.html")

    	# driver.get(self.base_url+"/")
    	# above=driver.find_element_by_link_text(u"设置")
    	# ActionChains(driver).move_to_element(above).perform()
    	# driver.find_element_by_link_text(u"搜索设置").click()

    	#设置每页搜结果为50条
    	m=driver.find_element_by_id("nr")
    	m.find_element_by_xpath(".//*[@id='nr']/option[3]").click()
    	time.sleep(2)

    	#保存设置的信息
    	driver.find_element_by_id("save").click()
    	time.sleep(2)
    	driver.switch_to_alert().accept()
		    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__=="__main__":
	# #定义一个单元测试容器
	# testunit=unittest.TestSuite()

	# #将测试用例加入到测容器中
	# # testunit.addTest(Baidu("test_baidu_search"))
	# testunit.addTest(Baidu("test_baidu_set"))

	# #定义一个测试报告的存放路径，支持相对路径
	# filename='F:\\songlan\hehe\maizi\\report\\results.html'
	# fp=open(filename,'wb')

	# #定义测试报告
	# runner=HTMLTestRunner.HTMLTestRunner(
	# 	stream=fp,
	# 	title=u'百度搜索测试报告',
	# 	description=u'用例执行情况：')

	# #运行测试用例
	# runner.run(testunit)
	
	unittest.main()
