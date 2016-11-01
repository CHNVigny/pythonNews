#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

class XmlOutputer(object):


    def output_xml(self, items):
        '''
        Constructor
        '''
        for item in items:
            print "%s %s %s %s %s %s" %(item['title'], item['link'], item['author'], item['category'], item['pubDate'], item['description'])