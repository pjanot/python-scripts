from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from leboncoin.items import AnnonceItem

import urlparse
from scrapy.http.request import Request

import pprint


class DivTree( object ):
    def __init__(self, node, depth=0):
        self.depth = depth
        classes = node.xpath('@class').extract()
        self.nodes = []
        self.data = node.xpath('text()').extract()
        #encoding (accents...)
        self.data = [ d.encode('ascii', 'replace').rstrip() for d in self.data]
        #clean up empty lines
        self.data = [d for d in self.data if d!='']
        if len(classes)==0: 
            # print 'no class'
            self.classname = 'no class'
            return
        else:
            self.classname = classes[0]
            # print self.classname
            self.nodes = [DivTree(path, depth+1) for path in node.xpath('div')]
            
            
    def __str__(self):
        tab = '\t'*self.depth 
        print 'data length : ', len(self.data)
        lines = [tab + self.classname]
        if len(self.data):
            lines.append(tab + tab.join(self.data))
        for node in self.nodes:
            lines.append(node.__str__())
        return '\n'.join(lines)

         
        
class LeboncoinSpider(BaseSpider):
    name = "leboncoin"
    allowed_domains = ["leboncoin.fr"]
    start_urls = [
         # "http://www.leboncoin.fr/annonces/offres/rhone_alpes/"
         # "http://www.leboncoin.fr/ventes_immobilieres/offres/rhone_alpes/?f=a&th=1",
         # Meximieux:
         "http://www.leboncoin.fr/ventes_immobilieres/offres/rhone_alpes/?o=2&location=Meximieux%2001800"
         ]

    def parseAnnonce(self, link):
        print link
        pass
        # detail = annonce.css('div[class="detail"]')
        
        
    def parse(self, response):
        sel = Selector(response)

        links_to_annonces = sel.css('div[class="list-lbc"]').xpath('a/@href').extract()
        links_to_annonces = [a.encode('ascii').rstrip() for a in links_to_annonces]

        for link in links_to_annonces:
            # self.parseAnnonce(link)
            print link
            item = AnnonceItem()
            yield Request(urlparse.urljoin(response.url, link), 
                          meta={'item':item},
                          callback=self.parse_annonce)
            # if 1: break
            
    def parse_annonce(self, response):
        print 'parsing annonce:', response.url
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
            surface.translate(None, ' m')
        item['surface'] = surface
        item['npieces'] = get_value(data,'Pi?ces')
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
