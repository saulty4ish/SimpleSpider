#-*- coding:utf-8 -*-

'''payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("url", params=payload)
print r.url
最终访问：url?key2=value2&key1=value1'''
import optparse
import requests
from BeautifulSoup import BeautifulSoup
headers = {'Connection': 'keep-alive','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0'}
url_contaionor=[]
url2_contaionor=[]
def catch_url(url):
	r=requests.get(url,headers=headers)
	html=r.text
	soup=BeautifulSoup(html)
	links=soup.findAll(name='a')
	for link in links:
		a=link['href']
		if 'http' in a:
			url_contaionor.append(a)
			print "[+]url get:"+str(a)+"\n"
		else:
			url_contaionor.append(url+a)
			print "[+]url get:"+str(url+a)+"\n"
	print "[+] catch the urls successfully !\n"
	print "[*] please check it in [url.txt]\n"
	return url_contaionor
def main():
	parser =optparse.OptionParser('input parsers:-u <target url>')
	parser.add_option('-u',dest='url',type='string',help='cin the target url')
	(options,args)=parser.parse_args()
	url=options.url
	if(url==None):
		print parser.usage
		exit(0)
	catch_url(url)
	with open('url.txt','a') as f:
		for url in url_contaionor:
			f.write(url+"\n")
main()