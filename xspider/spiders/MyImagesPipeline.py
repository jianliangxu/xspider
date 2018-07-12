import scrapy
from scrapy.pipelines.images import ImagesPipeline


class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        img_urls = item['image_urls']
        for img_url in img_urls:
            yield scrapy.Request(img_url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        title = request.meta['item']['title'][0].replace('/', '-') \
            .replace('\\.', '') \
            .repalce('\\!', '') \
            .repalce('\\:', '') \
            .replace('\\?', '') \
            .replace('\\*', '') \
            .replace('\\<', '') \
            .replace('\\>', '')
        page = request.meta['item']['page']
        named = request.url.split('/')[-1]
        path = 'newfull5/huarensss/' + page + '/' + title + '/' + named
        return path
