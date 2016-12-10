#!E:\Py_trade\pythonNews
# -*- coding: UTF-8 -*-






import xml_parser
import xml_outputer
import xml_downloader


class SpiderMain(object):

    def __init__(self):
        #self.urls = url_manager.UrlManager()
        self.downloader = xml_downloader.XmlDownloader()
        self.parser = xml_parser.XmlParser()
        self.outputer = xml_outputer.XmlOutputer()



    def craw(self, root_url):
        #count = 1
        """
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try :
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)


                if count == 100:
                    break
                count = count + 1
            except:
                print 'craw failed'
                
        """
        try :
            
            #print 'craw %d : %s' % (count, new_url)
            xml_cont = self.downloader.download(root_url)#xml_cont�����غõ�xml����
#             print xml_cont
            items = self.parser.parse(xml_cont)
            #self.urls.add_new_urls(new_urls)
            #self.outputer.collect_data(new_data)


            
        except:
            print 'craw failed'

        self.outputer.output_xml(items)

    
        
if __name__ == "__main__":
#     news_categoties = ["china","world","society"]
#     for news_categotie in news_categoties:
    root_url = "http://rss.sina.com.cn/news/allnews/finance.xml"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)