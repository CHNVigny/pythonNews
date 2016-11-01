#!/usr/bin/env python2
# -*- coding: UTF-8 -*-


import xml.etree.ElementTree as ET

class XmlParser(object):





    
    def parse(self, xml_cont):
        items=[]
        root = ET.fromstring(xml_cont)
        channel = root.find('channel')
        for item in channel.findall('item'):
            title = item.find('title').text
            link = item.find('link').text
            author = item.find('author').text
            category = item.find('category').text
            pubDate = item.find('pubDate').text
            description = item.find('description').text
            dic = {"title" : title, "link" : link, "author" : author, "category" : category, "pubDate" : pubDate, "description" : description}
            items.append(dic)    
        return items
            