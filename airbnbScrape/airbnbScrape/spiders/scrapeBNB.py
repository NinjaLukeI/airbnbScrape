import scrapy
import selenium
from time import sleep

from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# driver = webdriver.Chrome("/Users/Luke/PycharmProjects/airbnbScrape/chromedriver")
# driver.get('https://www.airbnb.co.uk/rooms/33090114?guests=1&adults=1')

# scrapy_selector = Selector(text = driver.page_source)
# scrapy_selector.xpath('//*[@id="site-content"]/div[1]/div/div/section/div/div/div/div[1]/ol')

class scrapeBNB(scrapy.Spider):
    name = "airbnb"

    # def start_requests(self):
    start_urls = (
        'https://www.airbnb.co.uk/rooms/33090114',
        'https://www.airbnb.co.uk/rooms/50633275',
        'https://www.airbnb.co.uk/rooms/33571268'

    )

    # for url in urls:
    # yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        #locating chromedriver. path may need to be changed to be relative
        driver = webdriver.Chrome("/Users/Luke/PycharmProjects/airbnbScrape/chromedriver")

        #using the urls from start_urls
        driver.get(response.url)

        #using try except to catch sites that give 403 error or any layout errors
        try:
            property_name = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, '//*[@id="site-content"]/div/div[1]/div[1]/div[1]/div/div/div/div/section/div[1]/span/h1')))
            property_beds = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, '//*[@id="site-content"]/div[1]/div/div/section/div/div/div/div[1]/ol/li[2]/span[2]')))
            property_bathrooms = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, '//*[@id="site-content"]/div[1]/div/div/section/div/div/div/div[1]/ol/li[4]/span[2]')))
            property_type = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, '//*[@id="site-content"]/div[1]/div/div/section/div/div/div/div[1]/div/h2')))

            property_type_noHosted = property_type[0].text.split(" hosted", 1)
            property_type_noHosted = property_type_noHosted[0]





            yield {
                'property name': ([property_name[0].text]),
                'property beds': ([property_beds[0].text]),
                'property bathrooms': ([property_bathrooms[0].text]),
                'property type': ([property_type_noHosted])
            }


        except:

            #airbnb website doesn't return a proper 403 error code so making a check for the
            #text box that's shown on the website with the error code
            error_code = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div/div/section/div[2]/div')))

            ##print(f'THIS IS THE ERROR CODE, {error_code[0].text}')

            if "403" in error_code[0].text:
                print("Site isn't allowing access.")

        print("RUNNING THIS!!!!!!!")

        driver.quit()
