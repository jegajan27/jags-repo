import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("http://www.python.org")
if "Python" in driver.title:
    print("yes")
time.sleep(10)    
elem = driver.find_element_by_name("q")
time.sleep(10)
elem.clear()
time.sleep(10)
elem.send_keys("pycon")
time.sleep(10)
elem.send_keys(Keys.RETURN)
time.sleep(10)
time.sleep(10)

if "No Results found" in driver.page_source:
    print("No Results found was displayed")
else:
    print("Results found")

print("Success")
time.sleep(10)
driver.close()    