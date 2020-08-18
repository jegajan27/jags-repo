import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.google.com")
search_txt = driver.find_element_by_name('q')
search_txt.send_keys("Selenium WebDriver Interview questions")
search_txt.submit()

time.sleep(10)
list_txt = driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div[1]/div/div/div[1]/a")
print ("List of r " + list_txt.text + "searches:")

i=0
for item in list_txt:
    print(item.get_attribute("innerHTML"))
    i = i+1
    if(i>10):
        break

driver.close()

new line