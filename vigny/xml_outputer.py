#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import  MySQLdb

class XmlOutputer(object):


    def output_xml(self, items):
        '''
        Constructor
        '''
        for item in items:
            print "%s %s %s %s %s %s %s" %(item['title'], item['link'], item['author'], item['category'], item['pubDate'], item['description'], item['img_url'])
            
    def oprate_db(self, items):
        conn=MySQLdb.connect(host="localhost",user="root",passwd="123456",db="newsdata",charset="utf8")
        cursor = conn.cursor()
        for item in items:
            sql = "INSERT INTO news(Title,Description, Date, Source, ImgUrl, Url) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" %(item['title'], item['description'], item['pubDate'], item['author'], item['img_url'], item['link'])
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 提交到数据库执行
                conn.commit()
            except:
                # Rollback in case there is any error
                conn.rollback()
                
        conn.close()
    def output_html(self, items):
        pass