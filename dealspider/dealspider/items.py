from scrapy.item import Item, Field

class DealspiderItem(Item):
    description = Field()
    price = Field()
    url = Field()
