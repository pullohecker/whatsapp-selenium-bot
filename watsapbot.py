from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

k = input("How many times?   ")
u = input("What text?   ")

web = webdriver.Chrome()

web.get('https://web.whatsapp.com')

sleep(1)

input("Sign in")
input("select target")

for i in range(int(k)):
    o = web.find_element(By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
    o.send_keys(u + Keys.ENTER)
    sleep(0.1)
web.quit()
