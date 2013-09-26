#!/usr/bin/env python
#-*- coding:utf-8 -*-
from dnspod import base
from dnspod import user

# init

base.headers.update({
    'User-Agent': 'dnspod python api/1.0.0.0(chenkun0128@126.com)'
})

base.common_params.update({
    'login_email': 'your email',
    'login_password': 'your password'
})

# test
print base.get_api_version(base.common_params)

print user.user_detail(base.common_params)

user.user_modify(dict(base.common_params, **{
    'real_name': '张三',
    'nick': 'zhangsan',
    'telephone': '1390000000',
    'im': '123456'
}))