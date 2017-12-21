# -*- coding:utf-8 -*-  
import requests
from bs4 import BeautifulSoup
import re
class spider:
    def __init__(self,url):
        self.url=url
        self.headers = {
             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
             'Referer': 'http://www.baidu.com',
             'Cookie': 'whoami=saulty4ish',
             }
    def visit(self,url):
        try:
            r=requests.get(url,headers=self.headers)
            ret=r.text
            return ret
        except:
            print "[-] fail to connect!"
    def getsitemap(self,ret):
        urls=[]
        try:
            soup=BeautifulSoup(ret,"lxml")
            tags_a =soup.findAll(name='a',attrs={'href':re.compile("^https?://")})
            for tag_a in tags_a:
                urls.append(tag_a['href'])
            return urls
        except:
            print "[-] fail to analysis!"
    def dealurl(self,ret):
        urls=[]
        soup=BeautifulSoup(ret,"lxml")
        tags_with_relativeurls=soup.findAll(name="a",attrs={"href":re.compile("^/\w+.\w+")})
        if(tags_with_relativeurls):
            for tag in tags_with_relativeurls:
                url=self.url+str(tag)
                urls.append(url)
        else:
            print "[-] none relative url found"
        return urls
obj=spider("http://60.205.228.7")
ret=obj.visit("http://60.205.228.7")
test=obj.getsitemap(ret)
test2=obj.dealurl(ret)
test.append(test2)
for i in range(0,len(test)):
    print test[i]
