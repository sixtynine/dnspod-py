#!/usr/bin/env python
#-*- coding:utf-8 -*-
from base import api, common_params

@api('User.Detail')
def user_detail(params=None):
    '''获取帐户信息'''
    pass

@api('User.Modify')
def user_modify(params=None):
    '''---------------------------------------------------修改资料
    请求参数：
    公共参数
    real_name     - 真实姓名，如果用户类型是企业，则为公司名称
    nick          - 用户称呼，用于与用户联系时称呼用户
    telephone     - 用户手机号码
    im            - 用户qq
    
    响应代码：
    共通返回
    8 手机号码不正确
    9 用户qq不正确'''
    pass

@api('Userpasswd.Modify')
def user_passwd_modify(params=None):
    '''---------------------------------------------------修改密码
    请求参数：
    公共参数
    old_password  - 旧密码
    new_password  - 新密码
    
    响应代码：
    共通返回
    8 旧密码错误
    9 新密码错误'''
    pass

@api('Useremail.Modify')
def user_email_modify(params=None):
    '''---------------------------------------------------修改邮箱
    请求参数：
    公共参数
    old_email     - 旧邮箱
    new_email     - 新邮箱
    password      - 当前密码
    
    响应代码：
    共通返回
    8 旧邮箱错误
    9 新邮箱错误
    10 当前密码错误'''
    pass

@api('Telephoneverify.Code')
def telephone_verify_code(params=None):
    '''---------------------------------------------------获取手机验证码
    请求参数：
    公共参数
    old_email     - 旧邮箱
    new_email     - 新邮箱
    password      - 当前密码
    
    响应代码：
    共通返回
    8 旧邮箱错误
    9 新邮箱错误
    10 当前密码错误'''
    pass

@api('User.Log')
def user_log(params=None):
    '''获取用户日志'''
    pass