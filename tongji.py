# encoding: utf-8
"""
@version: 1.0
@author: Jarrett_UESTC
@file: tongji
@time: 2020/1/19 22:35
"""

import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve  #方法直接将远程数据下载到本地

#四川省统计局网址
url = 'http://tjj.sc.gov.cn/sjfb/sjxz/'
#获取网页内容
r = requests.get(url)

file_lst = [] #保存文件链接
file_name = [] #保存文件名
bs = BeautifulSoup(r.content, "html.parser") #解析网页，比如加上.content的内容。
hyperlink = bs.find_all('a')
for h in hyperlink:
    hh = h.get('href')
    if hh and '.xlsx' in hh:
        file_lst.append(hh)
        file_name.append(h.string)

def download(url, savepath, filename):
    """
    download file from internet
    :param url: path to download from
    :param savepath: path to save files
    :return: None
    """
    def reporthook(a, b, c):
        """
        显示下载进度
        :param a: 已经下载的数据块
        :param b: 数据块的大小
        :param c: 远程文件大小
        :return: None
        """
        t =  (a * b * 100.0 / c)
        if t >= 100:
            t = 100
        print("\rdownloading: %5.1f%%" % t, end="")
    #filename = os.path.basename(url)

    # 判断文件是否存在，如果不存在则下载
    if not os.path.isfile(os.path.join(savepath, filename)):
        print('Downloading data from %s' % url)
        urlretrieve(url, os.path.join(savepath, filename), reporthook=reporthook)
        print('\nDownload finished!')
    else:
        print('File already exsits!')
    # 获取文件大小
    filesize = os.path.getsize(os.path.join(savepath, filename))
    # 文件大小默认以Bytes计， 转换为Mb
    print('File size = %.2f Mb' % (filesize/1024/1024))

#print(file_lst)
#print(file_name)
for i in range(len(file_lst)):
    download(url+file_lst[i][2:], savepath='./file/', filename = file_name[i]+'.xlsx')

