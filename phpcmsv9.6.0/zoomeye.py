#coding=utf-8
import requests
import re
from bs4 import BeautifulSoup as bs
import time

headers = {
            #"Connection":"keep-alive",
            "Cookie":"__jsluid=76bd0f5c14d44261872539a1eaac1cc4; Hm_lvt_e58da53564b1ec3fb2539178e6db042e=1492605715,1492951198,1493030131; Hm_lpvt_e58da53564b1ec3fb2539178e6db042e=1493031167; __jsl_clearance=1493038578.835|0|alNMQc9yfE6flWGXqNAtLmpdEN8%3D",
            #Cookie:__jsluid=2c2b0c6c3b78ee5998e174fe6bb63d06; Hm_lvt_e58da53564b1ec3fb2539178e6db042e=1492740090; Hm_lpvt_e58da53564b1ec3fb2539178e6db042e=1492993973; __jsl_clearance=1493023396.272|0|z%2FrfdfIQo6k%2F8GpZhbKbWPQJC2o%3D
            #"Referer":"www.zoomeye.org",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        }

url = "https://www.zoomeye.org/search?q= app:phpcms ver:9&t=web&p="

for i in range(1, 10):
	res = requests.get(url + str(i), headers=headers)
	#print res
	soup = bs(res.content, 'lxml')
	ul = soup.find_all(name='ul',  attrs={"class": "result web"})
	if ul:
		targets = ul[0].find_all(name='a', attrs={"target": "_blank"})
		for target in targets:
			print target['href']

	time.sleep(1)
