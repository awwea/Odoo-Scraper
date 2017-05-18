from odoo import models, fields, api
from ..util.scraper import Scrapper

class MyProduct(models.Model):
    _name = 'scraper.product'

    name = fields.Char(string='Product')
    category = fields.Char(string='Category')
    title = fields.Char(string='Title')
    price = fields.Float(string='Price')
    description = fields.Char(string='Description')
    image = fields.Binary()
    imagePath=''
    url = fields.Char(string='URL')


    def getData(self):
        scraper = Scrapper(self.url)
        self.name = scraper.getName()
        self.description = scraper.getDescription()
        # self.category = scraper.get_category()
        self.price = scraper.getPrice()
        self.imagePath = scraper.getImageUrl()


    def updateProducts(self):
        products = self.env['scraper.product'].search([])
        for product in products:
            temp = self.env['scraper.product'].browse([product.id])
            scraper = Scrapper(temp.link)
            temp.write({"name": scraper.getName(), "description": scraper.getDescription(),
                        "price": scraper.getPrice(), 'imagePath': scraper.getImageUrl()})