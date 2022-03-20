#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# CampusNetwork-AutoLogin 广西农业职业技术大学校园网登录
# update：2022/03/20 22:30
# https://github.com/keaiye/CampusNetwork-Login
from datetime import datetime
from bs4 import BeautifulSoup
import json5
import requests
import time
import re

# 学号 密码
StudentID = ""
Password = ""
# 联通unicom 电信telecom
Operator = "telecom"


def network():
    url = "http://10.10.10.2/"
    headers = {
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Host": "10.10.10.2",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
    }

    title = "注消页"
    r = requests.get(url, headers=headers)
    state_title = BeautifulSoup(r.text, 'html.parser').title.string

    if title[0] in state_title[0]:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "校园网处于登录状态，正在尝试注消后在登录")
        logout()
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "等待15秒后登录")
        time.sleep(15)
        login()
    else:
        login()


def login():
    url = f"http://10.10.10.2/drcom/login?callback=dr1003&DDDDD={StudentID}@{Operator}&upass={Password}&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&v6ip=&terminal_type=1"
    headers = {
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Host": "10.10.10.2",
        "Referer": "http://10.10.10.2/a79.htm",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
    }

    r = requests.get(url, headers=headers).text

    pattern = re.compile('(?<="result":).*?(?=,)')
    result = pattern.search(r).group(0)

    if "1" in result:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "登录成功", r)
        print("------------------------------------------")
    else:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "登录失败:", r)
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "正在尝试重新登录")
        login()


def logout():
    url = f"http://10.10.10.2/drcom/logout?callback=dr1005"
    headers = {
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Host": "10.10.10.2",
        "Referer": "http://10.10.10.2/a79.htm",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
    }

    r = requests.get(url, headers=headers).text
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "注消成功")


network()
