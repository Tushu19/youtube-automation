from selenium import webdriver
import time
from random import randrange

driver1=webdriver.Chrome()
driver2=webdriver.Chrome()
driver3=webdriver.Chrome()

refresh_time=10
broswer_list=[]

broswer_list.append(driver1)
broswer_list.append(driver2)
broswer_list.append(driver3)

for broswer in broswer_list:
    broswer.get('https://youtube.com')
    searchbox=broswer.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
    searchbox.send_keys('Mr. BadEye')
    searchbutton=broswer.find_element_by_xpath('//*[@id="search-icon-legacy"]')
    searchbutton.click()

while True:
    broswer_num=randrange(0,len(broswer_list))
    broswer_list[broswer_num].refresh()
    print('Broswer number',broswer_num,'getting refreshed')
    time.sleep(refresh_time)
