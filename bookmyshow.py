import os
import glob
from re import search
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print('=================================')
n= input("No of people going: ")
print('=================================')
driver= webdriver.Chrome(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver.get("https://in.bookmyshow.com/explore/home/kanpur")
time.sleep(3)
popUp= driver.find_element_by_xpath('//*[@id="wzrk-confirm"]')
popUp.click()
time.sleep(1)
signIn= driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/header/div[1]/div/div/div/div[2]/div[2]/div[1]')
signIn.click()
time.sleep(2)

continueWithGoogle= driver.find_element_by_xpath('//*[@id="modal-root"]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div')
continueWithGoogle.click()
another_window = list(set(driver.window_handles) - {driver.current_window_handle})[0]
driver.switch_to.window(another_window);
inputEmail = driver.find_element_by_xpath('//*[@id="identifierId"]')
inputEmail.send_keys("kumarujjawal51")
next1= driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
next1.click()
time.sleep(2)
password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys('ujjawal2')
next2= driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
next2.click()
time.sleep(8)
main_window = list(set(driver.window_handles))[0]
driver.switch_to_window(main_window)
recentMovie= driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[3]/div[1]/div[2]/div/div/div[2]/div/div[1]/a[1]/div/div[2]/div/img')
recentMovie.click()
time.sleep(2)
bookTicket= driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/div[2]/div/button')
bookTicket.click()
time.sleep(2)
slot= driver.find_element_by_xpath('//*[@id="venuelist"]/li[1]/div[2]/div[2]/div[1]/a')
slot.click()
time.sleep(2)
noOfPeople= driver.find_element_by_xpath(f'//*[@id="pop_{n}"]')
noOfPeople.click()
selectSeats= driver.find_element_by_xpath('//*[@id="proceed-Qty"]')
selectSeats.click()




