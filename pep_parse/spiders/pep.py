import scrapy  # type: ignore

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Паук собирает все ссылки на документы PEP."""
        all_pep_links = response.css('a.reference.external::attr(href)')
        for pep_link in all_pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Парсит страницы с документами и формирует Items."""
        data = {
            'number': response.css('dt:contains("PEP") + dd::text').get(),
            'name': response.css('h1.page-title::text').get(),
            'status': response.css('dt:contains("Status") + dd::text').get()
        }
        yield PepParseItem(data)
