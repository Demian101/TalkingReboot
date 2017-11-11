# -*- coding: utf-8 -*-
import sys
import requests
import json

def GetText(info):
    appkey = "e5ccc9c7c8834ec3b08940e290ff1559"

    url = "http://www.tuling123.com/openapi/api?key=%s&info=%s"%(appkey,info)
    content = requests.get(url)
    answer = content.text

    ans=json.loads(answer)
    aa=ans['text']
    return aa

if __name__ == '__main__':
    print('Begin Talking !!')
    print('马上要进入聊天室了, 给自己起一个昵称吧 :')
    yourname = input('昵称:') 
    while True:
        info = input(yourname+' : ')
        if 'bye' == info:
            break
        print('小埋 : ',GetText(info))