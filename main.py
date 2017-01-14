#coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
import time

def get_html(url):
    head={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'\
    'Accept-Encoding': 'gzip, deflate, sdch'\
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'\
    'Cache-Control': 'max-age=0'\
    'Connection': 'keep-alive'\
    'Cookie': '__jda=122270672.1484366011879587586832.1484366012.1484366012.1484366012.1; __jdb=122270672.1.1484366011879587586832|1.1484366012; __jdc=122270672; __jdv=122270672|direct|-|none|-|1484366011881; o2-webp=true; __jdu=1484366011879587586832'\
    'Host': 'www.jd.com'\
    #'If-Modified-Since': 'Sat, 14 Jan 2017 03:44:02 GMT'\
    'Upgrade-Insecure-Requests': '1'\
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
    }
    html=requests.get(url,headers=head).text
    time.sleep(3)
    return html

url='https://list.jd.com/list.html?cat=737,13297,1300&ev=3680_6820&trans=1&page=6&JL=6_0_0#J_main'
html=get_html(url)

#f = open('index.html','w')
#f.write(html.encode('utf-8'))
#f.close()