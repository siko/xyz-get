#!/usr/bin/env python

__all__ = ['teahour_download_aid','teahour_download']

from ..common import *
from bs4 import BeautifulSoup


def teahour_download_aid(url, output_dir='.', info_only=False):
    html = get_content(url)
    soup = BeautifulSoup(html)
    title = str_strip(soup.find('h2',class_='title').contents[6])
    audiourl = str_strip(soup.find('audio')['src'])

    ext = r1(r'\.([^.]+)$', audiourl)
    _, _, size = url_info(audiourl)

    print_info(site_info, title, ext, size, audiourl)
    if not info_only:
        download_urls([audiourl], title, ext, size, output_dir = output_dir)


def teahour_download(url, output_dir='.', info_only=False, limit='0,10'):

    if url == 'http://teahour.fm/':
        l = limit.split(',')
        l_begin   = 0 if len(l)==1 else int(l[0])
        l_end     = int(l[0]) if len(l)==1 else int(l[1])

        html = get_content(url)
        soup = BeautifulSoup(html)
        articles = soup.find('li',attrs={'id':'episodes'}).findAll('li')

        reallen = len(articles)
        begin = l_begin if l_end > l_begin else l_end
        end = l_end if l_end > l_begin else l_begin

        # print(begin,end,reallen)

        if reallen < begin:
            arts = articles[:reallen]
        elif (reallen > begin and reallen < end ):
            arts = articles[begin:reallen]
        else:
            arts = articles[begin:end]

        for art in arts:
            teahour_download_aid(url+art.find('a')['href'],output_dir,info_only)

    else:
        teahour_download_aid(url,output_dir,info_only)

site_info = "teahour.fm"
download = teahour_download
