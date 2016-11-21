#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import requests
if __name__ == '__main__':
    link="http://go.rss.sina.com.cn/redirect.php?url=http://tech.sina.com.cn/d/v/2016-11-17/doc-ifxxwrwh4515927.shtml"
    res=requests.get(link)
    res.encoding='utf-8'
    print(res.text)