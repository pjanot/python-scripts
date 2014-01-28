from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.spider import BaseSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from leboncoin.items import AnnonceItem

import urlparse
from scrapy.http.request import Request

import pprint


def process_value(value):
    print value
    import pdb; pdb.set_trace()
    return value
    
class LeboncoinSpider(BaseSpider):
    name = "leboncoin"
    allowed_domains = ["leboncoin.fr"]
    start_urls = [
         # rhone alpes
         # "http://www.leboncoin.fr/ventes_immobilieres/offres/rhone_alpes/?f=a&th=1",
         # ain
         "http://www.leboncoin.fr/ventes_immobilieres/offres/rhone_alpes/ain/?f=a&th=1",
         # Meximieux:
         # "http://www.leboncoin.fr/ventes_immobilieres/offres/rhone_alpes/?o=1&location=Meximieux%2001800"
         ]

    def parse(self, response):      
        sel = Selector(response)
        links_to_annonces = sel.css('div[class="list-lbc"]').xpath('a/@href').extract()
        links_to_annonces = [a.encode('ascii').rstrip() for a in links_to_annonces]

        print response.url

        for link in links_to_annonces:
            # self.parseAnnonce(link)
            # print link
            item = AnnonceItem()
            yield Request(urlparse.urljoin(response.url, link), 
                          meta={'item':item},
                          callback=self.parse_annonce)
            # if 1: break

        # next page
        link_url = None
        links = sel.css('li[class="page"]')

        for link in links:
            link_text = link.xpath('a/text()').extract()
            print link_text
            if len(link_text) and link_text[0].find('suivante'):
                link_urls = link.xpath('a/@href').extract()
                if len(link_urls):
                    link_url = link_urls[0]
        if link_url:
            yield Request(urlparse.urljoin(response.url, link_url), 
                          meta={},
                          callback=self.parse)

            
    def parse_annonce(self, response):
        # print 'parsing annonce:', response.url
        item = response.request.meta['item'] 
        item['url'] = response.url

        sel = Selector(response)
        params = sel.css('div[class="lbcParams"]')
        price = params.xpath('table//td/span/text()').extract()

        data = params.xpath('//table//tr//text()').extract()
        data = [d.encode('ascii','replace').rstrip().lstrip() for d in data]
        data = [d for d in data if d!='']

        price = get_value(data,'Prix')
        if price: 
            price = price.translate(None,' ?')
        item['price'] = price

        surface = get_value(data,'Surface')
        if surface: 
            surface = surface.translate(None, ' m')
        item['surface'] = surface
        item['npieces'] = get_value(data,'Pi?ces')
        item['zipcode'] = get_value(data, 'Code postal')
        yield item


def get_value(data, field):
    index = None
    for i, d in enumerate(data): 
        if d.find(field)!=-1:
            index = i+1
    if index:
        return data[index]
    else:
        return None


