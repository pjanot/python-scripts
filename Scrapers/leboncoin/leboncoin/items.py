# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class AnnonceItem(Item):
    # define the fields for your item here like:
    zipcode = Field()
    url = Field()
    price = Field()
    surface = Field()
    npieces = Field()
    day = Field()
    month = Field() 
    pass
