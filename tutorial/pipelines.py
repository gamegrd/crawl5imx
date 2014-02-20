# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
class TutorialPipeline(object):
    
    def __init__(self):
        #self.file = codecs.open('scraped_data_utf8.json', 'w', encoding='utf-8')
        print("\n\n\n\n\n_______________________BEGIN_____________________\n\n\n\n")
 
    def process_item(self, item, spider):
        self.file = codecs.open('scraped_data_utf8.json', 'a', encoding='utf-8')
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line.decode('gbk','ignore').decode("unicode_escape"))
        self.file.close()
        return item

    def spider_closed(self, spider):
            #self.file.close()
            print("\n\n\n\n\n_______________________Finished_____________________\n\n\n\n")
