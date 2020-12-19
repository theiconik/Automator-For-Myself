import re
from re import search
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

c= input("Enter which company's stock price you want to know : ")
stcp= c + ' stock price'
driver= webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.google.com")
time.sleep(2)
searchBox= driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
searchBox.send_keys(stcp)
searchBox.send_keys(Keys.RETURN)
time.sleep(1)
value= driver.find_element_by_class_name('IsqQVc.NprOob.XcVN5d')
unit= driver.find_element_by_class_name('knFDje')
print("===================================================")
print(value.text + " " + unit.text)
print("===================================================")

driver.quit() 
