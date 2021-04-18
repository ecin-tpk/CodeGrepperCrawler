from urllib.parse import urljoin

import scrapy


def parse_answers(response):
    answers = response.xpath('//div[@class="answer_info_holder_outer"]')
    for answer in answers:
        title = answer.xpath('./div/div[@class="answer_info_title"]/text()')[0].extract()
        code = answer.xpath('./textarea/text()')[0].extract()
        yield {
            'title': title,
            'code': code
        }


class CodeSpider(scrapy.Spider):
    name = 'code'
    start_urls = ['https://www.codegrepper.com/code-examples/javascript']

    def parse(self, response, **kwargs):
        # urls = urljoin(response.url,
        #                response.xpath("//div[@id='language_snipper_cats_holder']/div/ul/li/a/@href").extract())
        # for url in urls:
        #     yield scrapy.Request(url, callback=parse_answers)

        urls = urljoin(response.url,
                       response.xpath("//div[@id='language_snipper_cats_holder']/div/ul/li/a/@href")[0].extract())
        # for url in urls:
        #     yield scrapy.Request(url, callback=parse_answers)

        yield scrapy.Request(urls, callback=parse_answers)
