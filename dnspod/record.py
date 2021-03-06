#!/usr/bin/env python
#-*- coding:utf-8 -*-
from base import api

@api('Record.Create')
def record_create(params=None):
    '''---------------------------------------------------添加记录
    请求参数：
    公共参数
    domain_id                   - 域名ID, 必选
    sub_domain                  - 主机记录, 如 www, 默认@，可选
    record_type                 - 记录类型，通过API记录类型获得，大写英文，比如：A, 必选
    record_line                 - 记录线路，通过API记录线路获得，中文，比如：默认, 必选
    value                       - 记录值, 如 IP:200.200.200.200, CNAME: cname.dnspod.com., MX: mail.dnspod.com., 必选
    mx                          - {1-20} MX优先级, 当记录类型是 MX 时有效，范围1-20, MX记录必选
    ttl                         - {1-604800} TTL，范围1-604800，不同等级域名最小值不同, 可选
    
    响应代码：
    共通返回
    -15 域名已被封禁
    -7 企业账号的域名需要升级才能设置
    -8 代理名下用户的域名需要升级才能设置
    6 缺少参数或者参数错误
    7 不是域名所有者或者没有权限
    21 域名被锁定
    22 子域名不合法
    23 子域名级数超出限制
    24 泛解析子域名错误
    25 轮循记录数量超出限制
    26 记录线路错误
    27 记录类型错误
    30 MX 值错误，1-20
    31 URL记录数超出限制
    32 NS 记录数超出限制
    33 AAAA 记录数超出限制
    34 记录值非法
    36 @主机的NS纪录只能添加默认线路'''
    pass

@api('Record.List')
def record_list(params=None):
    '''---------------------------------------------------记录列表
    请求参数：
    公共参数
    domain_id 域名ID，必选
    offset 记录开始的偏移，第一条记录为 0，依次类推，可选
    length 共要获取的记录的数量，比如获取20条，则为20，可选
    sub_domain 子域名，如果指定则只返回此子域名的记录，可选
    
    响应代码：
    共通返回
    -7 企业账号的域名需要升级才能设置
    -8 代理名下用户的域名需要升级才能设置
    6 域名ID错误
    7 记录开始的偏移无效
    8 共要获取的记录的数量无效
    9 不是域名所有者
    10 没有记录
    
    注意事项：
    如果域名的记录数量超过了3000，将会强制分页并且只返回前3000条，这时需要通过 offset 和 length 参数去获取其它记录。'''
    pass

@api('Record.Modify')
def record_modify(params=None):
    '''---------------------------------------------------修改记录
    请求参数：
    公共参数
    domain_id                    - 域名ID，必选
    record_id                    - 记录ID，必选
    sub_domain                   - 主机记录，默认@，如 www，可选
    record_type                  - 记录类型，通过API记录类型获得，大写英文，比如：A，必选
    record_line                  - 记录线路，通过API记录线路获得，中文，比如：默认，必选
    value                        - 记录值, 如 IP:200.200.200.200, CNAME: cname.dnspod.com., MX: mail.dnspod.com.，必选
    mx                           - {1-20} MX优先级, 当记录类型是 MX 时有效，范围1-20, mx记录必选
    ttl                          - {1-604800} TTL，范围1-604800，不同等级域名最小值不同，可选
    
    响应代码：
    共通返回
    -15 域名已被封禁
    -7 企业账号的域名需要升级才能设置
    -8 代理名下用户的域名需要升级才能设置
    6 域名ID错误
    7 不是域名所有者或没有权限
    8 记录ID错误
    21 域名被锁定
    22 子域名不合法
    23 子域名级数超出限制
    24 泛解析子域名错误
    25 轮循记录数量超出限制
    26 记录线路错误
    27 记录类型错误
    29 TTL 值太小
    30 MX 值错误，1-20
    31 URL记录数超出限制
    32 NS 记录数超出限制
    33 AAAA 记录数超出限制
    34 记录值非法
    35 添加的IP不允许
    36 @主机的NS纪录只能添加默认线路'''
    pass

@api('Record.Remove')
def record_remove(params=None):
    '''---------------------------------------------------删除记录
    请求参数：
    公共参数
    domain_id                    - 域名ID，必选
    record_id                    - 记录ID，必选
    
    响应代码：
    共通返回
    -15 域名已被封禁
    -7 企业账号的域名需要升级才能设置
    -8 代理名下用户的域名需要升级才能设置
    6 域名ID错误
    7 不是域名所有者或没有权限
    8 记录ID错误
    21 域名被锁定'''
    pass

@api('Record.Ddns')
def record_ddns(params=None):
    '''---------------------------------------------------更新动态DNS记录
    请求参数：
    公共参数
    domain_id                    - 域名ID，必选
    record_id                    - 记录ID，必选
    sub_domain                   - 主机记录，如 www
    record_line                  - 记录线路，通过API记录线路获得，中文，比如：默认，必选
    value                        - IP地址，例如：6.6.6.6，可选
    
    响应代码：
    共通返回
    -15 域名已被封禁
    -7 企业账号的域名需要升级才能设置
    -8 代理名下用户的域名需要升级才能设置
    6 域名ID错误
    7 不是域名所有者或没有权限
    8 记录ID错误
    21 域名被锁定
    22 子域名不合法
    23 子域名级数超出限制，比如免费套餐域名不支持三级域名
    24 泛解析子域名错误，比如免费套餐载名不支持 a*
    25 轮循记录数量超出限制，比如免费套餐域名只能存在两条轮循记录
    26 记录线路错误，比如免费套餐域名不支持移动、国外'''
    pass

@api('Record.Remark')
def record_remark(params=None):
    '''---------------------------------------------------设置记录备注
    请求参数：
    公共参数
    domain_id                 - 域名ID，必选
    record_id                 - 记录ID，必选
    remark                    - 域名备注，删除备注请提交空内容，必选
    
    响应代码：
    共通返回
    6 域名ID错误
    8 记录 ID 错误'''
    pass

@api('Record.Info')
def record_info(params=None):
    '''---------------------------------------------------获取记录信息
    请求参数：
    公共参数
    domain_id                 - 域名ID，必选
    record_id                 - 记录ID，必选
    
    响应代码：
    共通返回
    -15 域名已被封禁
    -7 企业账号的域名需要升级才能设置
    -8 代理名下用户的域名需要升级才能设置
    6 域名ID错误
    7 不是域名所有者或没有权限
    8 记录ID错误'''
    pass

@api('Record.Status')
def record_status(params=None):
    '''---------------------------------------------------设置记录状态
    请求参数：
    公共参数
    domain_id                 - 域名ID，必选
    record_id                 - 记录ID，必选
    status {enable|disable}   - 新的状态，必选
    
    响应代码：
    共通返回
    -15 域名已被封禁
    -7 企业账号的域名需要升级才能设置
    -8 代理名下用户的域名需要升级才能设置
    6 域名ID错误
    7 不是域名所有者或没有权限
    8 记录ID错误
    21 域名被锁定'''
    pass