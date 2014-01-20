# Scrapy settings for leboncoin project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'leboncoin'

SPIDER_MODULES = ['leboncoin.spiders']
NEWSPIDER_MODULE = 'leboncoin.spiders'

ITEM_PIPELINES = {
    'leboncoin.pipelines.LeboncoinPipeline': 300,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'leboncoin (+http://www.yourdomain.com)'
