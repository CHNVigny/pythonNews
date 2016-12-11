from distutils.core import setup 
import py2exe
opts = { "py2exe": { "includes": "xml.etree.ElementTree, urllib2, bs4, feedparser" } }
setup( options = opts, name="china.exe", version="0.1", console=["china.py"])