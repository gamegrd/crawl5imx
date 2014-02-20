#coding=utf-8
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.http import Request

from tutorial.items import TutorialItem

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["bbs.5imx.com"]
    start_urls = [
        "http://bbs.5imx.com/bbs/forum.php?mod=forumdisplay&fid=453&filter=author&orderby=dateline",
    ]

    def parse(self, response):
        #items = []
        hxs = Selector(response)
        sites = hxs.xpath(".//table[@id='threadlisttableid']/tbody")
        for site in sites.xpath('tr/th/a[2]'):
            page_url="http://bbs.5imx.com/bbs/"+site.xpath('@href').extract()[0]
            print(page_url);
            #返回一个 Request 继续抓
            yield Request(page_url, callback=self.detail)
            
#             item = TutorialItem()
#             item['title'] =site.xpath('text()').extract()
#             print(item['title'])
#             item['content']=''.join(site.xpath('@href').extract())           
#             items.append(item)
#         return items
    #默认返回一个null 停止工作
    pass

    def detail(self,response):
        item = TutorialItem()
        hxs = Selector(response)
        # scrapy 使用的是 xpath1.0 协议  不可以有tbody  firefox 的 tbody 是他自己增加的 除非你确定源代码中有 tbody 这项
        # 在使用firefox测试的时候 tbody 用*代替  
        title = hxs.xpath(".//*[@id='thread_subject']/text()").extract()
        item['title']=title
        #得到每层楼数据
        floors=[]
        for floor in hxs.xpath(".//div[@class='t_fsz'][1]/table/tr/td[@class='t_f']"):
            #得出 text 数据 如果使用 floor.extract() 可以得到 html 编码  
            content=floor.xpath('text()').extract()
            floors.append(content);
#             try:
#                #字符串转换一定要用 ignore 否则会有问题 空格转不过去
#                 print("".join(content).encode("gbk",'ignore'))
#             except:
#                 print(content) 
    
        item['content']=floors
        
        #显示工作状态
        title = title[0].encode('gbk').strip()
        print "title:",title
        '''
        title_file = open("title.txt","a")
        title_file.write("title:%s\n"%(title))
        title_file.close()
        '''
        #返回抓到的数据
        return item
    
    