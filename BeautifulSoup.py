import urllib.request
from bs4 import BeautifulSoup

url="http://luanvan.net.vn/luan-van/do-an-bai-toan-nam-triet-gia-31150/"
page =urllib.request.urlopen(url);
soup =BeautifulSoup(page)
for link in soup.find_all('a'):
   print (link.get('href'))
