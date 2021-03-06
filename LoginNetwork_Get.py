#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
'''
    @Name: CampusNetwork-Login 广西农业职业技术大学校园网登录
    @File: LoginNetwork_Get.py
    @Version: 1.5
    @UpdateTime: 2022/03/23 23:55
    @CreateTime: 2020/11/15 18:15
    @Github https://github.com/keaiye/CampusNetwork-Login
'''

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
# True开启 False关闭 用于登录失败后是否重试（无限重试，直到登录成功才结束进程）
Retry = True


def network():
    url = "http://10.10.10.2/"
    headers = {
        "Host": "10.10.10.2",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
    }

    title = "注消页"
    r = requests.get(url, headers=headers)
    state_title = BeautifulSoup(r.text, 'html.parser').title.string

    print("####################开始执行####################")
    if title[0] in state_title[0]:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "校园网处于登录状态")
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "正在尝试注消后登录")
        logout()  # 注消登录
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "等待15秒后登录")
        time.sleep(15)
        login()  # 登录
    else:
        login()  # 登录


def login():
    url = f"http://10.10.10.2/drcom/login?callback=dr1003&DDDDD={StudentID}@{Operator}&upass={Password}&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&v6ip=&terminal_type=1"
    headers = {
        "Host": "10.10.10.2",
        "Referer": "http://10.10.10.2/a79.htm",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
    }

    r = requests.get(url, headers=headers).text

    pattern = re.compile('(?<="result":).*?(?=,)')
    result = pattern.search(r).group(0)

    if "1" in result:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "登录成功", r)
        return
    else:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "登录失败:", r)
        if Retry:
            print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "正在尝试重新登录")
            login()
        else:
            return


def logout():
    url = f"http://10.10.10.2/drcom/logout?callback=dr1005"
    headers = {
        "Host": "10.10.10.2",
        "Referer": "http://10.10.10.2/a79.htm",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
    }

    r = requests.get(url, headers=headers).text
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "注消成功")


if __name__ == '__main__':
    network()
