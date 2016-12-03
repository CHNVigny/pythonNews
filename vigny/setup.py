from distutils.core import setup 
import py2exe
opts = { "py2exe": { "includes": "xml.etree.ElementTree, urllib2, bs4" } } 
setup( options = opts, name="spider_main.exe", version="0.1", console=["spider_main.py"])