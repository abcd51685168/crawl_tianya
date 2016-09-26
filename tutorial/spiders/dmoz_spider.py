# coding=utf-8
import scrapy
import time
from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["bbs.tianya.cn"]
    start_urls = [
        "http://bbs.tianya.cn/post-no05-244449-1.shtml#ty_vip_look[73081143]",
    ]
    filename = '/root/dousuishanhe.txt'

    def parse(self, response):
        time.sleep(1)
        with open(self.filename, 'a') as f:
            for sel in response.xpath('//div[@class="bbs-content"]'):
                data = '\n'.join(sel.xpath('text()').extract()).replace('\t', '')
                if len(data) < 100:
                    f.write(str(len(data)))
                    f.write(data)

        next_page = response.xpath("//a[@class='js-keyboard-next']/@href")
        if next_page:
            url = "http://bbs.tianya.cn" + next_page[0].extract() + "#ty_vip_look[73081143]"
            yield scrapy.Request(url, self.parse)
