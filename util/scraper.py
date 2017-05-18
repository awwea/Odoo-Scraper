import requests
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self, url):
        self.source = requests.get(url)
        self.soup = BeautifulSoup(self.source.content, "lxml")

    def getName(self):
        pn = self.soup.find("div", {"class": "small-12 columns product-title"})
        product_name = pn.find("h1").text
        return product_name

    def getPrice(self):
        price = self.soup.find("div", {"class": "text-default price-container"})
        price_value = price.find("h3").text
        return price_value.replace("EGP", "").replace(",","")

    def getDescription(self):
        description = self.soup.find("div", {"class": "item-details-mini"})
        desc = description.find("p").text
        return desc

    def getImageUrl(self):
        image = self.soup.find("div", {"class": "img-bucket"})
        image_url = image.find('img').get('src')
        return image_url
