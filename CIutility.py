import requests
import time
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from PIL import ImageGrab
from selenium import webdriver



class utility:
	# 定义为类级变量,而不是实例变量,则不会实例化而分配新的内存
	driver = None

	session = None

	def __init__(self):
		pass
		# self.url = 'https://localhost:8080/wb'

	# 将方法定义为类级方法,直接通过类名就可以调用,不需要实例化
	@classmethod
	def get_wd(cls):
		if cls.driver is None:
			cls.driver = webdriver.Chrome()
			cls.driver.maximize_window()
			cls.driver.implicitly_wait(10)
			cls.driver.get('https://localhost:8080/wb')
			time.sleep(2)

		return cls.driver

	@classmethod
	def get_session(cls):
		if cls.session is None:
			cls.session = requests.session()

		return cls.session

	# 断言
	@classmethod
	def assert_equal(cls, expect, actual, case):
		if expect == actual:
			cls.result(case=case)
		else:
			cls.result(case=case, result='失败')

	@classmethod
	def assert_re(cls, express, actual, case):
		if re.match(express, actual, case):
			cls.result(case=case)
		else:
			cls.result(case=case, result='失败')

	@classmethod
	def assert_contain(cls, expect, actual, case, type):
		if expect in actual:
			cls.result(case=case, type=type)
		else:
			screenshot = time.strftime('%Y%m%d_%H%M%S.png')
			ImageGrab.grab().save(f'../CI_report/{screenshot}')
			cls.result(case=case, result='失败', screenshot=screenshot, type=type)

	# 写入测试结果到csv文件中
	@classmethod
	def result(cls, case, type='自动化测试', result='成功', message='无', screenshot='无'):
		now = time.strftime('%Y-%m-%d %H:%M:%S')
		with open('../CI_report/result.csv', 'a+', encoding='utf-8') as file:
			file.write(now + ',' + case + ',' + type + ',' + result + ',' + message + ',' + screenshot + '\n')

	# 生成测试报告
	@classmethod
	def report(cls):
		with open('../CI_report/result.csv', encoding='utf-8') as file:
			line_list = file.readlines()