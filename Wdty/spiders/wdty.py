import scrapy
from ..items import WdtyItem


class WdtySpider(scrapy.Spider):
    name = 'wdty'
    allowed_domains = ['p2peye.com']

    # start_urls = ['https://www.p2peye.com/platform/z1/']

    def start_requests(self):
        for p in range(2, 3):
            url = 'https://www.p2peye.com/platform/z1/p{}/'.format(p)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        li_list = response.xpath('//ul/li[@class="ui-result-item"]/div/div/a')
        for li in li_list:
            item = WdtyItem()
            item['name'] = li.xpath('./@title').get().strip()
            item['expected_rate_of_interest'] = li.xpath('./div[1]//strong/text()').get().strip()
            url = 'https:' + li.xpath('./@href').get().strip()
            item['status'] = li.xpath('./div[1]/p[2]/text()').get().strip()
            item['capital'] = li.xpath('./div[2]/div/p[1]/text()').get().strip()
            item['adress'] = li.xpath('./div[2]/div/p[2]/text()').get().strip()
            # 信而富 8%~12% //crfchina.p2peye.com 运营状态：正常运营11年  注册资本：25465万  注册地：上海市|嘉定区
            # print(name,expected_rate_of_interest,link,status,capital,adress)
            # print(expected_rate_of_interest)

            yield scrapy.Request(
                url=url, meta={'item': item}, callback=self.parse_page
            )

    def parse_page(self, response):
        item = response.meta['item']
        item['time'] = response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/span/text()').get()
        item['product_info'] = response.xpath('//*[@id="chanpinxinxi"]/ul/li[1]/span[2]/text()').get()
        yield item
