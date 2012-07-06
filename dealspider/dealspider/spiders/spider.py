from scrapy.spider import BaseSpider
from dealspider.items import DealspiderItem
from scrapy.selector import HtmlXPathSelector

class SG_GroupOn_Spider(BaseSpider):
    name = 'SgGroupOn'
    allowed_domains = ['groupon.sg']
    start_urls = [
            'http://www.groupon.sg',
            ]
    
    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/div/h1/a/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/form/div/span/span/text()').extract()
        url = 'http://www.groupon.sg'
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class SG_BigDeal_Spider(BaseSpider):
    name = 'SgBigDeal'
    allowed_domains = ['plus.bigdeal.sg']
    start_urls = [
            'http://plus.bigdeal.sg',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/div/div/div/div/div/div/h1/div/a/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/text()').extract()
        url = hxs.select('/html/body/div/div/div/div/div/div/div/div/div/div/div/h1/div/a/@href').extract()
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class SG_ShiokDeal_Spider(BaseSpider):
    name = 'SgShiokDeal'
    allowed_domains = ['shiokdeal.com']
    start_urls = [
            'http://www.shiokdeal.com',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/div/h1/text()').extract()  
        price = hxs.select('/html/body/div/div/div/div/div/div/div/div/p/strong/text()').extract()
        url = 'http://www.shiokdeal.com'
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class SG_AllDealsAsia_Spider(BaseSpider):
    name = 'SgAllDealsAsia'
    allowed_domains = ['alldealsasia.com']
    start_urls = [
            'http://www.alldealsasia.com',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/div/div/div/div/div/h2/a/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/text()').extract()
        url = hxs.select('/html/body/div/div/div/div/div/div/div/div/div/div/h2/a/@href').extract()
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class SG_VoucherWow_Spider(BaseSpider):
    name = 'SgVoucherWow'
    allowed_domains = ['voucherwow.com']
    start_urls = [
            'http://www.voucherwow.com/cities/singapore',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/div/div/a/h2/span/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/div/div/div/div/p/text()').extract()
        url = hxs.select('/html/body/div/div/div/div/div/div/div/a/@href').extract()
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item
        
class SG_DealComSg_Spider(BaseSpider):
    name = 'SgDealComSg'
    allowed_domains = ['deal.com.sg']
    start_urls = [
            'http://www.deal.com.sg',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/a/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[@id="deal-price"]/text()').extract()
        url = hxs.select('/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/a/@href').extract()
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class BNG_GroupOn_Spider(BaseSpider):
    name = 'BngGroupOn'
    allowed_domains = ['crazeal.com']
    start_urls = [
            'http://www.crazeal.com/deals/bangalore',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/div/h1/a/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/form/div/span/span/text()').extract()
        url = 'http://www.crazeal.com/deals/bangalore'
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class BOM_GroupOn_Spider(BaseSpider):
    name = 'BomGroupOn'
    allowed_domains = ['crazeal.com']
    start_urls = [
            'http://www.crazeal.com/deals/mumbai',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/div/h1/a/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/form/div/span/span/text()').extract()
        url = 'http://www.crazeal.com/deals/mumbai'
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class CHE_GroupOn_Spider(BaseSpider):
    name = 'CheGroupOn'
    allowed_domains = ['crazeal.com']
    start_urls = [
            'http://www.crazeal.com/deals/chennai',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/div/h1/a/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/form/div/span/span/text()').extract()
        url = 'http://www.crazeal.com/deals/delhi-ncr'
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item
    
class DEL_GroupOn_Spider(BaseSpider):
    name = 'DelGroupOn'
    allowed_domains = ['crazeal.com']
    start_urls = [
            'http://www.crazeal.com/deals/delhi-ncr',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/div/h1/a/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/form/div/span/span/text()').extract()
        url = 'http://www.crazeal.com/deals/delhi-ncr'
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class KOL_GroupOn_Spider(BaseSpider):
    name = 'KolGroupOn'
    allowed_domains = ['crazeal.com']
    start_urls = [
            'http://www.crazeal.com/deals/kolkata',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/div/h1/a/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/form/div/span/span/text()').extract()
        url = 'http://www.crazeal.com/deals/delhi-ncr'
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class BNG_TimesDeal_Spider(BaseSpider):
    name = 'BngTimesDeal'
    allowed_domains = ['timesdeal.com']
    start_urls = [
            'http://www.timesdeal.com/bangalore-deals',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/div/h2/a/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/div/ul/li/a/span/text()').extract()
        url = hxs.select('/html/body/div/div/div/div/div/div/h2/a/@href').extract()
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class BOM_TimesDeal_Spider(BaseSpider):
    name = 'BomTimesDeal'
    allowed_domains = ['timesdeal.com']
    start_urls = [
            'http://www.timesdeal.com/mumbai-deals',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/div/h2/a/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/div/ul/li/a/span/text()').extract()
        url = hxs.select('/html/body/div/div/div/div/div/div/h2/a/@href').extract()
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class CHE_TimesDeal_Spider(BaseSpider):
    name = 'CheTimesDeal'
    allowed_domains = ['timesdeal.com']
    start_urls = [
            'http://www.timesdeal.com/chennai-deals',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/div/h2/a/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/div/ul/li/a/span/text()').extract()
        url = hxs.select('/html/body/div/div/div/div/div/div/h2/a/@href').extract()
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class DEL_TimesDeal_Spider(BaseSpider):
    name = 'DelTimesDeal'
    allowed_domains = ['timesdeal.com']
    start_urls = [
            'http://www.timesdeal.com/delhi-ncr-deals',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/div/h2/a/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/div/ul/li/a/span/text()').extract()
        url = hxs.select('/html/body/div/div/div/div/div/div/h2/a/@href').extract()
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class KOL_TimesDeal_Spider(BaseSpider):
    name = 'KolTimesDeal'
    allowed_domains = ['timesdeal.com']
    start_urls = [
            'http://www.timesdeal.com/kolkata-deals',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/div/h2/a/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/div/ul/li/a/span/text()').extract()
        url = hxs.select('/html/body/div/div/div/div/div/div/h2/a/@href').extract()
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class BNG_RediffDeal_Spider(BaseSpider):
    name = 'BngRediffDeal'
    allowed_domains = ['rediff.com']
    start_urls = [
            'http://dealhojaye.rediff.com/bangalore',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/table/tr/td/div/div/div/h1//text()').extract()
        price = hxs.select('/html/body/div/div/div/div/table/tr/td/div/div/div/div/div/text()').extract()
        url = 'http://dealhojaye.rediff.com/bangalore'
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class BOM_RediffDeal_Spider(BaseSpider):
    name = 'BomRediffDeal'
    allowed_domains = ['rediff.com']
    start_urls = [
            'http://dealhojaye.rediff.com/mumbai',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/table/tr/td/div/div/div/h1//text()').extract()
        price = hxs.select('/html/body/div/div/div/div/table/tr/td/div/div/div/div/div/text()').extract()
        url = 'http://dealhojaye.rediff.com/mumbai'
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class CHE_RediffDeal_Spider(BaseSpider):
    name = 'CheRediffDeal'
    allowed_domains = ['rediff.com']
    start_urls = [
            'http://dealhojaye.rediff.com/chennai',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/table/tr/td/div/div/div/h1//text()').extract()
        price = hxs.select('/html/body/div/div/div/div/table/tr/td/div/div/div/div/div/text()').extract()
        url = 'http://dealhojaye.rediff.com/chennai'
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class DEL_RediffDeal_Spider(BaseSpider):
    name = 'DelRediffDeal'
    allowed_domains = ['rediff.com']
    start_urls = [
            'http://dealhojaye.rediff.com/delhi',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/table/tr/td/div/div/div/h1//text()').extract()
        price = hxs.select('/html/body/div/div/div/div/table/tr/td/div/div/div/div/div/text()').extract()
        url = 'http://dealhojaye.rediff.com/delhi'
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class KOL_RediffDeal_Spider(BaseSpider):
    name = 'KolRediffDeal'
    allowed_domains = ['rediff.com']
    start_urls = [
            'http://dealhojaye.rediff.com/kolkata',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/table/tr/td/div/div/div/h1//text()').extract()
        price = hxs.select('/html/body/div/div/div/div/table/tr/td/div/div/div/div/div/text()').extract()
        url = 'http://dealhojaye.rediff.com/kolkata'
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class BNG_BuzzInTownDeal_Spider(BaseSpider):
    name = 'BngBuzzInTownDeal'
    allowed_domains = ['buzzintown.com']
    start_urls = [
            'http://deals.buzzintown.com/bangalore/home.html',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/h1/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/dl/dd/span[@class="price"]/text()').extract()
        url = 'http://deals.buzzintown.com/bangalore/home.html'
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class BOM_BuzzInTownDeal_Spider(BaseSpider):
    name = 'BomBuzzInTownDeal'
    allowed_domains = ['buzzintown.com']
    start_urls = [
            'http://deals.buzzintown.com/mumbai/home.html',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/h1/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/dl/dd/span[@class="price"]/text()').extract()
        url = 'http://deals.buzzintown.com/mumbai/home.html'
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class CHE_BuzzInTownDeal_Spider(BaseSpider):
    name = 'CheBuzzInTownDeal'
    allowed_domains = ['buzzintown.com']
    start_urls = [
            'http://deals.buzzintown.com/chennai/home.html',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/h1/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/dl/dd/span[@class="price"]/text()').extract()
        url = 'http://deals.buzzintown.com/chennai/home.html'
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class DEL_BuzzInTownDeal_Spider(BaseSpider):
    name = 'DelBuzzInTownDeal'
    allowed_domains = ['buzzintown.com']
    start_urls = [
            'http://deals.buzzintown.com/delhi/home.html',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/h1/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/dl/dd/span[@class="price"]/text()').extract()
        url = 'http://deals.buzzintown.com/delhi/home.html'
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class KOL_BuzzInTownDeal_Spider(BaseSpider):
    name = 'KolBuzzInTownDeal'
    allowed_domains = ['buzzintown.com']
    start_urls = [
            'http://deals.buzzintown.com/kolkata/home.html',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/h1/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/dl/dd/span[@class="price"]/text()').extract()
        url = 'http://deals.buzzintown.com/kolkata/home.html'
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class BNG_MyDala_Spider(BaseSpider):
    name = 'BngMyDala'
    allowed_domains = ['mydala.com']
    start_urls = [
            'http://www.mydala.com/deals-bangalore/restaurant',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/h1/a/div/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/div/div/h1/text()').extract()
        url= hxs.select('/html/body/div/div/div/div/div/h1/a/@href').extract()
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class BOM_MyDala_Spider(BaseSpider):
    name = 'BomMyDala'
    allowed_domains = ['mydala.com']
    start_urls = [
            'http://www.mydala.com/deals-mumbai/restaurant',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/h1/a/div/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/div/div/h1/text()').extract()
        url= hxs.select('/html/body/div/div/div/div/div/h1/a/@href').extract()
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class CHE_MyDala_Spider(BaseSpider):
    name = 'CheMyDala'
    allowed_domains = ['mydala.com']
    start_urls = [
            'http://www.mydala.com/deals-chennai/restaurant',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/h1/a/div/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/div/div/h1/text()').extract()
        url= hxs.select('/html/body/div/div/div/div/div/h1/a/@href').extract()
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class DEL_MyDala_Spider(BaseSpider):
    name = 'DelMyDala'
    allowed_domains = ['mydala.com']
    start_urls = [
            'http://www.mydala.com/deals-delhi/restaurant',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/h1/a/div/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/div/div/h1/text()').extract()
        url= hxs.select('/html/body/div/div/div/div/div/h1/a/@href').extract()
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item

class KOL_MyDala_Spider(BaseSpider):
    name = 'KolMyDala'
    allowed_domains = ['mydala.com']
    start_urls = [
            'http://www.mydala.com/deals-kolkata/restaurant',
            ]

    def parse(self, response):
        item = DealspiderItem()
        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/h1/a/div/text()').extract()
        price = hxs.select('/html/body/div/div/div/div/div/div/div/div/h1/text()').extract()
        url= hxs.select('/html/body/div/div/div/div/div/h1/a/@href').extract()
        item['description'] = description
        item['price'] = price
        item['url'] = url
        return item
