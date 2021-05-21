#!/usr/bin/env python
# coding=utf-8
from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify
from urlparse import urlparse, parse_qs
import time
import sys
import requests
import json


app = Flask(__name__)

base_path = ''
dedata = {'ret': 0, 'msg': "success"}

# 企业微信群机器人

def send_wechat(md):
    wechat_bot_url = "企微机器人webhook"
    headers = {'Content-Type': 'application/json'}
    #request_data = {"msgtype": "markdown", "markdown": {"content": md}}
    request_data = md

    r = requests.post(wechat_bot_url, data=json.dumps(request_data))

@app.route('/', methods=['POST'])
def home():
    # 接收推过来的信息
    a = str(request.get_data(as_text=True)) #原始推送过来的数据为dict格式，转换成str
    b = a.replace('text','content')  #将text替换成content
    c = eval(b) #转换成dict格式，不然无法推送消息
    send_wechat(c)
    return (jsonify(dedata))


def handler(environ, start_response):
    parsed_tuple = urlparse(environ['fc.request_uri'])
    li = parsed_tuple.path.split('/')
    global base_path
    if not base_path:
        base_path = "/".join(li[0:5])
    return app(environ, start_response)
