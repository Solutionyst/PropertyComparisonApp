import requests
from scrapy import Selector
import scraper_helper
from datetime import date
from app.models import propertyData

switch = True

date = date.today()
date_format = date.strftime("%d/%m/%y")

date_format2 = date.strftime("%y-%m-%d")

property = propertyData()

def scraper():
    r = requests.session()
    for num in range(1, 10):
        req = r.get(f'https://www.places.je/propertysearch/residential-buy?propertyCategoryId=1&page={num}')
        resp = Selector(text=req.text)
        links = resp.xpath('//a[@class="places-property-result"]/@href').getall()
        for link in links:
            link = link.split('/')[-1]
            print(link)
            req = r.get(f'https://www.places.je/property/{link}')
            resp = Selector(text=req.text)
            price = resp.xpath('//span[@class="property-info-price"]/text()').get()
            price = price.replace("£","")
            price = price.replace(",", "")

            location = resp.xpath('//span[@class="d-block mb-1 mb-md-2"]/text()').get()
            location = scraper_helper.cleanup(location)
            road_name = location.split(',')[0]
            area = location.split(',')[-1]

            bedrooms = resp.xpath(
                '//div[@class="places-property-features text-left"]/div/div[1]/div/span[1]/text()').get()
            bathrooms = resp.xpath(
                '//div[@class="places-property-features text-left"]/div/div[2]/div/span[1]/text()').get()
            parking = resp.xpath(
                '//div[@class="places-property-features text-left"]/div/div[4]/div/span[1]/text()').get()

            data = {
                'id': link,
                'price': price,
                'road name': road_name,
                'area': area,
                'number of bedrooms': bedrooms,
                'number of bathrooms': bathrooms,
                'number of car parking spots': parking
            }

            property.propertyID = link
            property.dateFound = date
            property.price = price
            property.roadName = road_name
            property.jerseyArea = area
            property.bedrooms = bedrooms
            property.bathrooms = bathrooms
            property.parking = parking

            if link in property.propertyID:
                print("No New Properties Found!")
            else:
                property.save()
                print("New Property Found!")