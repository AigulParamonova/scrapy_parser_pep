import scrapy  # type: ignore


class PepParseItem(scrapy.Item):
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
