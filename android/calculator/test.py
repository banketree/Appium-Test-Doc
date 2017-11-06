#coding=utf-8
from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['deviceName'] = 'Test26'
#计算器
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

# desired_caps['unicodeKeyboard'] = True  # 使用unicodeKeyboard的编码方式来发送字符串
# desired_caps['resetKeyboard'] = True  # 将键盘给隐藏起来
second = 3;
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_name("1").click()
sleep(second);
driver.find_element_by_name("5").click()
driver.find_element_by_name("9").click()
driver.find_element_by_name("delete").click()
sleep(second);
driver.find_element_by_name("9").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("+").click()
driver.find_element_by_name("6").click()
driver.find_element_by_name("=").click()
sleep(second);
driver.quit()