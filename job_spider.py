#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
url = 'https://search.51job.com/list/070300,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
html = requests.get(url)
html.encoding = 'GBK'
html_text = html.text
soup = BeautifulSoup(html_text, 'lxml')
div1 = soup.find_all('div', attrs={'class': 'dw_table'})
soup = BeautifulSoup(str(div1[0]), 'lxml')
div2 = soup.find_all('div', class_='el')
# 解析字段的标题
soup = BeautifulSoup(str(div2[0]), 'lxml')
el_title = soup.find_all('span')
title_lst = []
for each in el_title:
    title_lst.append(each.string)
# 解析内容
content_lst = []
for i in range(1, len(div2)):
    a = []
    soup = BeautifulSoup(str(div2[i]), 'lxml')
    t1 = soup.find_all('span')
    a.append(str(soup.a.string).replace('\r\n', '').replace(' ', ''))
    for k in range(1, len(t1)):
        a.append(t1[k].string)
    content_lst.append(a)
#     t1 = soup.find_all('a')
#     a.append(t1[0].string)
#     a.append(t1[1].string)
#     t2 = soup.find_all('span')
#     a.append(t2[2].string)
#     a.append(t2[3].string)
#     a.append(t2[4].string)
#     content_lst.append(a)
print(content_lst)
