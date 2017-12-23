import requests
from bs4 import BeautifulSoup
from docx import Document

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
        except:
            print "[-] fail to connect "
            ret=[]
        return ret
    def analysis(self,ret):
        pic=[]
        urls=[]
        soup=BeautifulSoup(ret,"lxml")
        tags=soup.findAll("img")
        for i in tags:
            pic.append(i.get('src'))
        for i in range(0,len(pic)):
            url=self.url+str(pic[i])
            urls.append(url)
        return urls
obj=spider("http://www.jit.edu.cn/")
ret=obj.visit("http://www.jit.edu.cn/")
urls=obj.analysis(ret)
for i in range(0,len(urls)):
    r=requests.get(urls[i],headers=obj.headers)
    with open("%s"%i+".jpg","wb") as f:
        f.write(r.content)
