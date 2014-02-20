# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'
ITEM_PIPELINES = ['tutorial.pipelines.TutorialPipeline']
DEFAULT_REQUEST_HEADERS = {'Accept':'text/heml,application/xhtml+xml;q=0.9,*/*;q=0.8','Accept-Language':'ch',}
DOWNLOAD_DELAY = 5
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
COOKIES_ENABLED = False
