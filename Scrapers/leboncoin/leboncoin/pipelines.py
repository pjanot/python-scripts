# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log

class LeboncoinPipeline(object):
    def process_item(self, item, spider):
        log.msg(str(item), level=log.WARNING)
        return item
