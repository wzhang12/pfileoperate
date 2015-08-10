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

def get_Data(language,link):
    list=[]
    url='http://www.ted.com'+link[0:link.index('?')]+'/transcript?language='+language
    r = requests.get(url,{"language":language,"talkarticle":"true"})
    text = u""+str(r.text)
    soup = BeautifulSoup(text)
    cells = soup.find_all("span", "talk-transcript__fragment")
    for cell in cells:
        list.append(cell.get_text(separator=u'', strip=False, types=(bs4.element.NavigableString, bs4.element.Comment)))
    return list

def get_article_links(num):
    page = num

    #language=zh-cn&sort=newest&page=2
    url = 'http://www.ted.com/talks/'
    params = {'language':'zh-cn','sort':'newest','page': page}
    try:
        r = requests.get(url,params)
    except:
        return None
    #print chardet.detect(str(r.text))
    text = u""+str(r.text)
    soup = BeautifulSoup(text,"html.parser")
    cells = soup.find_all("h4", "m5")
    href_list=[];
    for cell in cells:
        anchor=cell.find("a")
        href_list.append(str(anchor['href']))
    return href_list

def saveToFile(filePath,list=[]):
    afile=open(filePath,'w')
    for line in list:
            afile.write(line+"\n")
    afile.close()

num = 30
foldernum=1043
full_links = [];
while True:
    print num
    num+=1
    links = get_article_links(num)
    if(links and len(links)==0):
        print "no more links"
        break
    else:
        for link in links:
            print(link)
            if("michael_anti_behind_the_great_firewall_of_china" in link):
                continue
            filename = link['/talks/'.__len__():link.index('?')]
            print filename
            content=get_Data("zh-cn",link)
            if(not os.path.exists('D:/webdata/ted/'+filename)):
                os.makedirs(r'D:/webdata/ted/'+filename)
            saveToFile(r'D:/webdata/ted/'+filename+'/zh-cn.txt',content)
            content=get_Data("en",link)
            saveToFile(r'D:/webdata/ted/'+filename+'/en.txt',content)
            foldernum+=1
            print str(foldernum)+' finished'
print('finished!!!')






#fileWriter =open(u'J:\\ted.txt','w')
#hrefs=[];
#for title in titles:
    #anchor=title.find("a")
    #hrefs.append(u""+str(anchor['href']))
    #print u""+str(anchor)
    #fileWriter.writelines(u""+str(anchor))
#print hrefs
#fileWriter.write(text)
#fileWriter.close
