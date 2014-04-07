# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log
import sqlite3 
import os
import shutil

class LeboncoinPipeline(object):

    def open_spider(self, spider):
        dbfilename = '.'.join([spider.name, 'db'])
        # need to find out how to append to the same db, without duplicating entries.
        if os.path.isfile(dbfilename):
            os.remove(dbfilename)
        self.conn = sqlite3.connect( dbfilename )
        self.c = self.conn.cursor()
        # Create table
        self.c.execute('''CREATE TABLE ads
        (zipcode int, npieces int, price real, surface real,
        date text, 
        url text)
        ''')
        self.conn.commit()
             
    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()
        
    def process_item(self, item, spider):
        # cannot print, I think because of twisted. but I can use the logger.
        # log.msg(str(item), level=log.WARNING)
        # pas de pieces -> c'est un terrain. discard.
        if item['npieces'] is None:
            print 'WARNING: number of rooms not found'
            return None 
        qry = "INSERT INTO ads VALUES ({zipcode},{npieces},{price},{surface},'{date}','{url}')".format(
            zipcode = item['zipcode'],
            npieces = item['npieces'],
            price = item['price'],
            surface = item['surface'],
            date = '{year}-{month}-{day}'.format(year='2014',
                                                 month=str( item['month'] ).zfill(2),
                                                 day=str( item['day'] ).zfill(2) ), 
            url = item['url'],
            )
        print qry
        self.c.execute(qry)
        return item
