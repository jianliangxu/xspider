import scrapy
from scrapy.pipelines.files import FilesPipeline


class MyFilePipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        file_urls = item['file_urls']
        for file_url in file_urls:
            yield scrapy.Request(file_url, meta={'item': item})

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
        path = 'newfull5/huarensss/' + page + '/' + title + '/' + title + ".torrent"
        return path
