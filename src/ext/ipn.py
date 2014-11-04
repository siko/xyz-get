#!/usr/bin/env python

__all__ = ['ipn_download']

from ..common import *
from bs4 import BeautifulSoup

def ipn_download(url, output_dir='.', info_only=False, limit='0,10'):

    l = limit.split(',')
    l_begin   = 0 if len(l)==1 else int(l[0])
    l_end     = int(l[0]) if len(l)==1 else int(l[1])

    html = get_content(url)
    soup = BeautifulSoup(html)
    articles = soup.findAll('article',class_='episode')

    reallen = len(articles)
    begin = l_begin if l_end > l_begin else l_end
    end = l_end if l_end > l_begin else l_begin

    print(begin,end,reallen)

    if reallen < begin:
        arts = articles[:reallen]
    elif (reallen > begin and reallen < end ):
        arts = articles[begin:reallen]
    else:
        arts = articles[begin:end]

    for art in arts:
        title = art.find('h1').find('a').contents[2].strip().replace(' ','-').replace('\n','')
        audiourl = url+art.find('a',class_='button fa-download')['href']
        ext = r1(r'\.([^.]+)$', audiourl)
        _, _, size = url_info(audiourl)

        print_info(site_info, title, ext, size, audiourl)
        if not info_only:
            download_urls([audiourl], title, ext, size, output_dir = output_dir)


site_info = "ipn.li"
download = ipn_download
