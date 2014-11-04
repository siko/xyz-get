#!/usr/bin/env python
# -- coding:utf-8 --

import os, re, sys, time, datetime
import urllib,urllib2,threading,requests
from bs4 import BeautifulSoup

downurls = []
threads=[]
f=open('log.txt', 'w+')

class downloader(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.info=[]

    def run(self):
        for i in self.info:
            print '下载 %s\r\n' % i['url']
            try:
                # urllib.urlretrieve(i['url'], i['name'].decode('utf8'))
                urllib.urlretrieve(i['url'], i['name'])
            except Exception as e:
                f.write('url:' + i['url'] + '\r\n' + str(e) + '\r\n')

def createurls(channel,begin,end):
    # print channel
    page = requests.get(channel)
    soup = BeautifulSoup(page.text)
    articles = soup.findAll('article')[begin:end]
    for art in articles:
        filename = art.find('h1').find('a').contents[2].replace(' ','').replace('\n','')
        audiourl = channel+art.find('a',class_='button fa-download')['href']
        downurls.append([filename,audiourl])

def downfiles():
    i=0
    for g in downurls:
        name=g[0] + ".mp3"
        path=g[1]
        print 'name=',name,'path=',path
        if i%6==0:
            t=downloader()
            threads.append(t)
        t.info.append({'url':path, 'name':name})
        i=i+1

if __name__ == '__main__':
    channel = int(input('将从「IT 公论」（http://ipn.li/）下载,请选择节目- 1,IT公论 2,内核恐慌 3,太医来了 4,味之道 :'))
    channels = {
        1: 'itgonglun/',
        2: 'kernelpanic/',
        3: 'taiyilaile/',
        4: 'weizhidao/',
        }
    channelurl = 'http://ipn.li/'+channels.get(channel,'itgonglun/')

    begin = int(input('请输入开始的期数：'))
    end   = int(input('请输入结束的期数：'))

    createurls(channelurl,begin,end)
    downfiles()

    print 'threads length is : %d' % len(threads)

    for t in threads:
        t.start()

    time.sleep(1)
    f.flush()

    for t in threads:
        t.join()