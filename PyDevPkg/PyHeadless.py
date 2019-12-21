'''
Created on 10 Dec 2019

@author: Jega
'''
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.set_headless()
assert opts.headless #operating in headless mode

browser = webdriver.Firefox(options=opts)
browser.get('https://duckduckgo.com')


browser.close()
