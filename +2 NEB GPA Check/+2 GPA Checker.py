from selenium import webdriver as wb
from selenium.webdriver.common.by import By
import time as t

web=wb.Chrome()
web.get('https://neb.ntc.net.np/')
t.sleep(3)

sn=int(input("Enter Your Symbol Number"))
dob=input("Enter Date OF Birth(yyyy/mm/dd)")

name=web.find_element(By.ID,'symbol')
dateob=web.find_element(By.ID,'dob')
submit=web.find_element(By.NAME,'submit')
t.sleep(1)    
name.send_keys(sn)
dateob.send_keys(dob)
t.sleep(2)
submit.click()
t.sleep(10)