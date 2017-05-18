from odoo import models, fields, api


class MyProduct(models.Model):
    _name = 'scraper.product'

    name = fields.Char(string='Product')
    category = fields.Char(string='Category')
    title = fields.Char(string='Title')
    price = fields.Float(string='Price')
    description = fields.Char(string='Description')
    image = fields.Binary()
    url = fields.Char(string='URL')
    



