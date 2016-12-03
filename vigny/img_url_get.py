#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup





class get_img_url(object):
    def __init__(self):
        pass
#         self.html_downloader=html_downloader.HtmlDownloader()
    
    def htmldownload(self, link):
        res=requests.get(link)
        res.encoding='utf-8'
        return res.text
        
    def get_url(self,link):
        urls = []
        if link is None:
            return
#         print link
        html_cont = self.htmldownload(link)
#         print html_cont
        soup = BeautifulSoup(html_cont, 'html.parser')
        try:
            nodes = soup.find('div',class_="article article_16").find_all('div')
            for node in nodes:
                img_node = node.find('img')
                url = img_node['src']
                urls.append(url)
        except:
            return '-'
#         for node in nodes:
#             url = node['src']
#             urls.append(url)
        return urls
        

    
        