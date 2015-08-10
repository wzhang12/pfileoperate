# coding=utf-8
import requests
import chardet
import os
from bs4 import *
from bs4 import Tag
import bs4
import codecs


import sys
reload(sys)
sys.setdefaultencoding("utf-8")

post_headers = {
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
           'referer':'https://ssl.chunyuyisheng.com/ssl/api/weblogin/?next=http%3A//www.chunyuyisheng.com/home'
}



url = 'https://ssl.chunyuyisheng.com/ssl/api/weblogin/'
r=requests.get(url,headers=post_headers)
_cookies = r.cookies
soup = BeautifulSoup(r.text)
print(tuple(r.cookies))
print(soup)
code = soup.find("input", {"name":"csrfmiddlewaretoken"})['value']

url ="https://ssl.chunyuyisheng.com/ssl/api/weblogin/?next=http%3A//www.chunyuyisheng.com/home"
r2 = requests.post(url,{"csrfmiddlewaretoken":code,"next":"http://www.chunyuyisheng.com/home","username":"","password":""},headers=post_headers,verify=True,allow_redirects=True,cookies={"csrftoken":_cookies['csrftoken']})
print r2.content

print(tuple(r2.cookies))

s = requests.Session()

s.get(url,headers=post_headers)
request = s.get(url)

print(r.text)
a = [1, 2]
b = [3, 4]
a.extend(b)