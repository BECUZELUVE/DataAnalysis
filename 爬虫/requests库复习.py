#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Project -> File   ：爬虫 -> requests库复习.py
@IDE    ：PyCharm
@Author ：Icey
@Date   ：2021/1/24 23:31
@Desc   ：
'''

import requests

url_douban_url = 'https://movie.douban.com/'
headers =  {'user-agent': 'my-app/0.0.1'}
response_douban_movie = requests.get(url_douban_url,headers=headers)
# response_douban_movie = requests.get(url_douban_url)
print(response_douban_movie.text)




