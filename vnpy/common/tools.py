# -*- coding: utf-8 -*-
# Author: zhangchao
# Date: 2020-03-20
# Desc:

#
#
# class PushWechat:
#     API_URL = 'https://wxsendmsg.bytetrade.com/send?%s'
#
#     def __init__(self, send_key):
#         self.send_key = send_key
#
#     def send(self, title, body=''):
#         url = PushWechat.API_URL % (urllib.parse.urlencode(dict(sendkey=self.send_key, text=title, desp=body)))
#         return json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
#
#
# from functools import wraps
#
# logger = getLog()
#
#
#
# def send_SMS(phone_num, SMS_content):
#     # 初始化client,apikey作为所有请求的默认值
#     # 通用模板就是
#     # 机器  # name#预警：#errCode#
#     ##内的可以换成任意字符
#
#     _ip = configs["_ip"]
#     env = configs["_env"]
#
#     cont = f"机器{env}做市预警：{SMS_content}"
#
#     clnt = YunpianClient('4d41b81cf3f5307c0c49afca60673041')
#
#     param = {YC.MOBILE: str(phone_num), YC.TEXT: cont}
#     res = clnt.sms().single_send(param)
#     print(f"{res._code} {res._detail} {res._msg}")
#
#
# # wechat 告警
# pushwechat = PushWechat(wechat_channel)
#
#
# def send_mail(content, subject, receiver, file_path=None):
#     # 链接邮箱服务器
#     wy = yagmail.SMTP(user="autosend@bytetrade.io", password="bytetrade@2018")
#     # password
#     # 通常是
#     # 授权码
#
#     # 发送邮件
#     if file_path:
#         wy.send(
#             to=receiver,
#             # to=['nengchibawanfan@163.com']
#             subject=subject,
#             contents=[content, file_path])
#     else:
#         wy.send(
#             # to=['nengchibawanfan@163.com'],
#             to=receiver,
#             subject=subject,
#             contents=[content])
import requests

SendKey = "SCU68292Tf5fc283545f4b12548d0438da14df96d5deded0eb5903"

def push_bear(title, content):

    url = f"https://sc.ftqq.com/{SendKey}.send?"
    data = {
        "text": title,     # title
        "desp": content
    }
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0"}
    requests.post(url, data=data, headers=headers)


if __name__ == '__main__':
    push_bear("策略成交", "啊")