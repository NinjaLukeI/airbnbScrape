# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import scrapy
import selenium
import time

from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("/Users/Luke/PycharmProjects/airbnbScrape/chromedriver")
driver.get("https://www.airbnb.co.uk/rooms/33090114?source_impression_id=p3_1635750796_viHgI2h1D%2BAutZov")

scrapy_selector = Selector(text = driver.page_source)
title = scrapy_selector.xpath("//span[@class='_1n81at5']//h1[@class='_fecoyn4']/text()").extract()

teams = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="site-content"]/div/div[1]/div[1]/div[1]/div/div/div/div/section/div[1]/span/h1')))
print([i.text for i in teams])


print("hi")
print(title)

driver.quit()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
