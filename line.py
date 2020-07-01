#!  /usr/bin/env python

#-*- coding: utf-8-*-


import requests

def line():
    url = "https://notify-api.line.me/api/notify"
    token = "v1Pf5dUAeJXf1RAyXjpxorisyuIhykpztTchJ8ndJmi"
    headers = {"Authorization": "Bearer " + token}
    message = 'テストだよ！'
    payload = {"message":  message}
    requests.post(url, headers=headers, params=payload)


if __name__ == '__main__':
    line()