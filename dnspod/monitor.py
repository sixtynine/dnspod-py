#!/usr/bin/env python
#-*- coding:utf-8 -*-
from base import api, common_params

@api('Monitor.Listsubdomain')
def monitor_list_sub_domain(params=None):
    '''---------------------------------------------------列出包含A记录的子域名
    请求参数：
    公共参数
    domain或domain_id, 必选
    
    响应代码：
    共通返回
    6 域名不存在
    7 域名编号错误
    8 此域名没有任何记录'''
    pass

@api('Monitor.Listsubvalue')
def monitor.list_sub_value(params=None):
    '''---------------------------------------------------列出子域名的A记录
    请求参数：
    公共参数
    domain或domain_id, 必选
    subdomain          子域名，必选
    
    响应代码：
    共通返回
    6 域名不存在
    7 域名编号错误'''
    pass

@api('Monitor.List')
def monitor_list(params=None):
    '''监控列表'''
    pass

@api('Monitor.Create')
def monitor_create(params=None):
    '''---------------------------------------------------监控添加
    请求参数：
    公共参数
    domain_id                       - 域名编号，必选
    record_id                       - 记录编号，必选
    port                            - 监控端口，比如80，必选
    monitor_interval                - 监控间隔，支持{60|180|360|}，必选
    host                            - 监控主机头，比如 www.dnspod.cn，必选
    monitor_type                    - 监控类型，支持{http|https}，必选
    monitor_path                    - 监控路径，比如/，必选
    points                          - 监控节点，用,分隔多个，只能选择列表中的节点，并且有数量限制，必选
    bak_ip                          - 宕机备用，必选，支持任选以下选项中的一个：
        pass                            - 只监控，不切换
        pause                           - 智能暂停
        auto                            - 智能切换
        用逗号分隔的IP 设置备用IP           
    keep_ttl                        - 宕机不修改ttl，可选
    sms_notice                      - 短信通知，me域名所有者，share共享用户，用,分隔多选择，比如me,share, 可选
    email_notice                    - 邮件通知，me域名所有者，share共享用户，用,分隔多选择，比如me,share，可选
    less_notice                     - {yes|no}是否一个小时内只发一次通知，可选
    callback_url                    - 可选，回调URL，宕机了会将相关的参数提交到此设置的URL，具体参考回调URL说明，可选
    callback_key                    - 可选，回调密钥，如果设置了回调URL请设置此参数以保证安全，可选

    响应代码：
    共通返回
    6 域名编号错误
    7 记录编号错误
    8 监控主机头错误
    9 监控端口错误，端口只能是正整数1~65535
    10 监控类型不正确
    11 监控路径不正确
    12 监控间隔不正确
    13 监控节点不正确
    14 监控节点数量超出限制
    15 备用IP不正确
    16 备用url不正确
    17 备用IP不正确
    18 短信设置不正确
    19 邮件设置不正确
    20 此记录已经存在监控
    21 监控数量超出限制
    22 回调URL不正确'''
    pass

@api('Monitor.Modify')
def monitor_modify(params=None):
    '''---------------------------------------------------监控修改
    请求参数：
    公共参数
    monitor_id                      - 监控编号，必选
    port                            - 监控端口，比如80，必选
    monitor_interval                - 监控间隔，支持{60|180|360|}，必选
    monitor_type                    - 监控类型，支持{http|https}，必选
    monitor_path                    - 监控路径，比如/，必选
    points                          - 监控节点，用,分隔多个，只能选择列表中的节点，并且有数量限制，必选
    bak_ip                          - 宕机备用，必选，支持任选以下选项中的一个：
        pass                             - 只监控，不切换
        pause                            - 智能暂停
        auto                             - 智能切换
        用逗号分隔的IP 设置备用IP
    host                            - 监控主机头，比如 www.dnspod.cn，可选
    keep_ttl                        - 宕机不修改ttl，可选
    sms_notice                      - 短信通知，me域名所有者，share共享用户，用,分隔多选择，比如me,share, 可选
    email_notice                    - 邮件通知，me域名所有者，share共享用户，用,分隔多选择，比如me,share，可选
    less_notice                     - {yes|no}是否一个小时内只发一次通知，可选
    callback_url                    - 可选，回调URL，宕机了会将相关的参数提交到此设置的URL，具体参考回调URL说明，可选
    callback_key                    - 可选，回调密钥，如果设置了回调URL请设置此参数以保证安全，可选
    
    响应代码：
    共通返回
    7 监控编号错误
    8 监控主机头错误
    9 监控端口错误，端口只能是正整数1~65535
    10 监控类型不正确
    11 监控路径不正确
    12 监控间隔不正确
    13 监控节点不正确
    14 监控节点数量超出限制
    15 备用IP不正确
    16 备用url不正确
    17 备用IP不正确
    18 短信设置不正确
    19 邮件设置不正确
    22 回调URL不正确'''
    pass

@api('Monitor.Remove')
def monitor_remove(params=None):
    '''---------------------------------------------------监控删除
    请求参数：
    公共参数
    monitor_id                   - 监控编号
    
    响应代码：
    共通返回
    6 监控编号错误'''
    pass

@api('Monitor.Info')
def monitor_info(params=None):
    '''---------------------------------------------------获取监控信息
    请求参数：
    公共参数
    monitor_id                   - 监控编号
    
    响应代码：
    共通返回
    7 监控编号错误'''
    pass

@api('Monitor.Setstatus')
def monitor_set_status(params=None):
    '''---------------------------------------------------设置监控状态
    请求参数：
    公共参数
    monitor_id                   - 监控编号，必选
    status {enabled|disabled}    - 新的状态，必选
    
    响应代码：
    共通返回
    6 监控编号错误
    7 新状态代码错误
    8 请先启用域名
    9 请先启用记录'''
    pass

@api('Monitor.Gethistory')
def monitor_get_history(params=None):
    '''---------------------------------------------------获取监控历史
    请求参数：
    公共参数
    monitor_id                  - 监控编号，必选
    hours                       - 获取最近多少个小时的记录，可选
    
    响应代码：
    共通返回
    6 监控编号错误'''
    pass

@api('Monitor.Userdesc')
def monitor_user_desc(params=None):
    '''获取监控概况'''
    pass

@api('Monitor.Getdowns')
def monitor_get_downs(params=None):
    '''---------------------------------------------------获取监控警告
    请求参数：
    公共参数
    offset                       - 记录开始的偏移，第一条记录为 0，依次类推，可选
    length                       - 共要获取的记录的数量，比如获取20条，则为20，可选
    
    响应代码：
    共通返回'''
    pass