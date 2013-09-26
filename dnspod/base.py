#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests

api_host = 'https://dnsapi.cn/'

headers = {
    'User-Agent': ''
}

'''---------------------------------------------------------------------公共参数
login_email              - [必选]用户帐号， 
login_password           - [必选]用户密码，
format {json,xml}        - [可选]返回的数据格式，默认为xml，建议用json
lang {en,cn}             - [可选]返回的错误语言，默认为en，建议用cn
error_on_empty {yes,no}  - [可选]没有数据时是否返回错误，默认为yes，建议用no
user_id                  - [可选]用户的ID，仅代理接口需要， 用户接口不需要提交此参数'''
common_params = {
    'login_email': '',
    'login_password': '',
    'format': 'json',
    'lang': 'cn',
    'error_on_empty': 'no'
}

'''---------------------------------------------------------------------共通返回
-1                       - 登陆失败
-2                       - API使用超出限制
-3                       - 不是合法代理 (仅用于代理接口)
-4                       - 不在代理名下 (仅用于代理接口)
-7                       - 无权使用此接口
-8                       - 登录失败次数过多，账号被暂时封禁
-99                      - 此功能暂停开放，请稍候重试
1                        - 操作成功
2                        - 只允许POST方法
3                        - 未知错误
6                        - 用户ID错误 (仅用于代理接口)
7                        - 用户不在您名下 (仅用于代理接口)'''

def api(url):
    def _api(func):
        def __api(params):
            func(params)
            res = requests.post(api_host+url, data=params, headers=headers)
            #print res.request.body  # ! test
            return res.json()
        return __api
    return _api


@api('Info.Version')
def get_api_version(params=None):
    '''获取API版本号'''
    pass