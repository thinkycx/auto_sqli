#!/usr/bin/env python

import requests
import json
from time import sleep
import util



api_url = "http://192.168.10.147:8775"
headers = {'Content-Type':'application/json'}


class task(object):
    "describe each scan from the request"
    def __init__(self, scan_url, data=None, cookie=None):
        self.scan_url = scan_url
        self.data = data
        self.cookie = cookie
        self.taskid = json.loads(requests.get(api_url + '/task/new').text)['taskid']
        self.content = dict({'url':scan_url})
        self.content['data'] = data
        self.content['cookie'] = cookie

        r = requests.post(api_url + '/option/' + str(self.taskid) + '/set',
                          data = json.dumps(self.content), headers=headers)
        print 'init...'

    def start(self):
        r_start = requests.post(api_url + '/scan/' + str(self.taskid) + '/start', data=json.dumps({}), headers=headers)
        self.result =  r_start.json()
        while json.loads(requests.get(api_url + '/scan/' + str(self.taskid) + '/status').text)['status'] != 'terminated':
            sleep(1)
            print 'loading'
        print requests.get(api_url + '/scan/' + str(self.taskid) + '/data').text

if __name__ == '__main__':
    cookie = "security=low; PHPSESSID=8um6qef43dq6t9e42rtgoqlmm6"
    url ='http://127.0.0.1/DVWA-1.9/vulnerabilities/sqli_blind/?id=1&Submit=Submit#'
    t = task(scan_url=url,cookie=cookie)
    t.start()
    print t.taskid
    print t.content




