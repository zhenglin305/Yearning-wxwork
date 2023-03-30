from flask import Flask
from flask import request
import json
import requests

REQUEST_ID_HEADER = 'x-fc-request-id'

app = Flask(__name__)

# 企业微信群机器人

def send_wechat(md):
    wechat_bot_url = "企微机器人webhook"
    headers = {'Content-Type': 'application/json'}
    #request_data = {"msgtype": "markdown", "markdown": {"content": md}}
    request_data = md

    r = requests.post(wechat_bot_url, data=json.dumps(request_data))

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world():
        a = str(request.get_data(as_text=True)) #原始推送过来的数据
        b = a.replace('text','content')  #将text替换成content
        c = eval(b) #转换成dict格式，不然无法推送消息
        send_wechat(c)

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=9000)
