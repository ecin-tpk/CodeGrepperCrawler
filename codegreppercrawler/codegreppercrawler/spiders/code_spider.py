from urllib.parse import urljoin
from ..items import CodegreppercrawlerItem

import scrapy


def parse_answers(response):
    item = CodegreppercrawlerItem()
    answers = response.xpath('//div[@class="answer_info_holder_outer"]')
    for answer in answers:
        title = answer.xpath('./div/div[@class="answer_info_title"]/text()')[0].extract()
        code = answer.xpath('./textarea/text()')[0].extract()
        vote = answer.css('.commando-voting-number::text').extract_first()

        answer_info = answer.css('.answer_info_by::text').extract()
        tag = answer_info[0].strip().rsplit(' ', 1)[0]
        date = answer_info[-2]

        posted_by = answer.css('.answer_info_by a::text').extract_first()

        tags = ['javascript', 'flutter']

        source = answer.css('.answer_source a')
        source_name = source.css('::text').extract_first()
        source_url = source.css('::attr(href)').extract_first()

        item['title'] = title.strip()
        item['code'] = code
        item['date'] = date.strip()[4:]
        item['vote'] = int(vote)
        if tag not in tags:
            tags.append(tag)
        item['tags'] = tags
        item['posted_by'] = posted_by
        item['source_name'] = source_name
        item['source_url'] = source_url

        yield item


class CodeSpider(scrapy.Spider):
    name = 'code'
    start_urls = ['https://www.codegrepper.com/code-examples/javascript/frameworks/flutter']

    def parse(self, response, **kwargs):
        sub_urls = response.css('#language_snipper_cats_holder a::attr(href)').extract()

        for sub_url in sub_urls:
            url = urljoin(response.url, sub_url)

            yield scrapy.Request(url, callback=parse_answers)
