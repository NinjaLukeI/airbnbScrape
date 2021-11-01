import scrapy
import selenium

from scrapy.selector import Selector
from selenium import webdriver

#driver = webdriver.Chrome("/Users/Luke/PycharmProjects/airbnbScrape/chromedriver")
#driver.get('https://www.airbnb.co.uk/rooms/33090114?guests=1&adults=1')

#scrapy_selector = Selector(text = driver.page_source)
#scrapy_selector.xpath('//*[@id="site-content"]/div[1]/div/div/section/div/div/div/div[1]/ol')

class scrapeBNB(scrapy.Spider):
    name = "airbnb"

    def start_requests(self):
        urls = [
            'https://www.airbnb.co.uk/rooms/33090114',
            'https://www.airbnb.co.uk/rooms/50633275sc',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')