#!/usr/bin/env python

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
