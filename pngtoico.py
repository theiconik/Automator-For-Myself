import os
import glob
from re import search
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://convertio.co/")
time.sleep(2)
fileUpload= driver.find_element_by_xpath('//*[@id="pc-upload-add"]')
# * matches all files in directory
# if you need other specific file types
# use *.[type], for example *.py
files_in_dir = glob.glob('C:/Users/ujjaw/Downloads/*.png') 
recent_file = max(files_in_dir, key=os.path.getctime)
fileUpload.send_keys(recent_file)
time.sleep(2)
typeSelector= driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[1]/table/tbody/tr/td[3]/div/div/button')
typeSelector.click()
time.sleep(1)
searchICO= driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[1]/table/tbody/tr/td[3]/div/div/div/div[1]/input')
searchICO.send_keys('ICO')
time.sleep(1)
selectICO = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[1]/table/tbody/tr/td[3]/div/div/div/div[2]/div/div[1]/div/ul/li[1]/span')
selectICO.click()
time.sleep(2)
convert= driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/button')
convert.click()
time.sleep(10)
download= driver.find_element_by_css_selector('body > div.main-container.full-height.bg-light-gray > div > div > div > div.converter-container > div.files-container > div > div.data-table-wrapper > table > tbody > tr > td.dt-col.dt-btn.text-right.order-3 > a')
download.click()
time.sleep(7)
driver.quit()




