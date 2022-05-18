import scrapy
from ..items import BayutItem,BayutItem2

class BayutSpiderSpider(scrapy.Spider):
    name = 'bayut'
    allowed_domains = ['www.bayut.com']
    start_urls = ['https://www.bayut.com/to-rent/property/dubai/',]
    page_number=2

    def parse(self, response):
        items = BayutItem()
        href = response.xpath(('//li/article/div[1]/a[@class="_287661cb"]/@href')).extract()
        items['href1'] = href
        for i in href:
            next_url=i
            yield response.follow(next_url, callback=self.parse1)



    def parse1(self,response):
        price=BayutItem2()
        properties=BayutItem2()
        amenities1=BayutItem2()
        bed_bath_size1=BayutItem2()
        property_info=response.xpath('//li/span[@class="_812aa185"]/text()').extract()
        currency = response.xpath('//div[@class="c4fc20ba"]/span[1]/text()').get()
        amount = response.xpath('//div[@class="c4fc20ba"]/span[3]/text()').get()
        location = response.xpath('// div[2] / div[1] / div[2] / div[2]/text()').get()
        bed = response.xpath('//div[2] / div[3] / div[1] / span[2] /span[@class="fc2d1086"]/text()').get()
        bath = response.xpath('// div[1] / div[2] / div[3] / div[2] / span[2] / span[@class="fc2d1086"]/text()').get()
        size = response.xpath('//div[1] / div[2] / div[3] / div[3] / span[2] / span / span/text()').get()
        agent_name = response.xpath('//div[2]/div[2]/div[1]/div[1]/div/div[3]/span[2]/text()').get()
        permit_no = response.xpath('//div[2] / div[2] / div[1] / div[1] / div / div[2] / span[3]/text()[3]').get()
        url = response.xpath('//div[2]/div[1]/div[1]/div[1]/picture/source/@srcset').get()
        breadcrumbs = response.xpath('//div[2]/div[1]/div[2]/div[2]/text()').get()
        for i in response.xpath('//div[@class="_40544a2f"]/span[@class="_005a682a"]/text()'):
          amenities=(i.get())
          amenities1['amenities'] = amenities


        description=response.xpath('//div[2]/div[1]/div[4]/div/div[1]/div[1]/div/div/div/span/text()[2]').get()


        properties["property_info"]=property_info

        price["currency"]=currency
        price["amount"]=amount
        bed_bath_size1["bed"]=bed
        bed_bath_size1["bath"]=bath
        bed_bath_size1["size"]=size

        yield {'property':property_info,'price':price,'location':location,'bed_bath_size':bed_bath_size1,
                 'agent_name':agent_name,'permit_number':permit_no,"url":url,"breadcrumbs":breadcrumbs,
               "amenities":amenities1,"description":description
               }

        next_page = 'https://www.bayut.com/to-rent/property/dubai/page-' + str(BayutSpiderSpider.page_number) + '/'
        if BayutSpiderSpider.page_number <= 42:
            BayutSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

