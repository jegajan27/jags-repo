import time

from selenium import webdriver
from selenium.webdriver import Chrome

'''
driver = webdriver.Chrome()
driver.get("https://selenium.dev")
test_url = driver.current_url
print("url" +test_url)

time.sleep(10)
driver.close()
'''
#driver = webdriver.Chrome(r'C:\Users\drivers\chromedriver.exe')
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.seleniumeasy.com/test/basic-first-form-demo.html")
assert "Selenium Easy Demo - Simple Form to Automate using Selenium" in driver.title
time.sleep(5)
eleUserMessage = driver.find_element_by_id("user-message")
time.sleep(5)
eleUserMessage.clear()
time.sleep(5)
eleUserMessage.send_keys("Test Python")
time.sleep(10)

eleShowMsgBtn=driver.find_element_by_css_selector('#get-input > .btn')
time.sleep(5)
eleShowMsgBtn.click()
time.sleep(5)

eleYourMsg=driver.find_element_by_id("display")
time.sleep(5)
assert "Test Python" in eleYourMsg.text
time.sleep(5)
driver.close()

