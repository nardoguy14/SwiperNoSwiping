from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://tinder.com")

count = 0
time.sleep(60)
while True:
    time.sleep(3)
    try:
        if count % 5:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button").click()
    except:
        print("try again")
    count += 1
    print(f"count now: {count}")
