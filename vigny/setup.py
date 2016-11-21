from distutils.core import setup 
import py2exe # ICI j'indique de maniere Explicite les lib a charger ! (pour email & Co) 
opts = { "py2exe": { "includes": "xml.etree.ElementTree, urllib2, bs4" } } 
setup( options = opts, name="spider_main.exe", version="0.1", console=["spider_main.py"])