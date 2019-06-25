#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 16:56
# @Author  : taojian
# @Site    : 
# @File    : hmacmd5.py
# @Software: PyCharm


import hmac

def hmac_md5(SigSecret,s):
    '''
    :param key:key就是签名秘匙
    :param s:s就是你要去拼接的参数
    :return:
    '''
    return hmac.new(SigSecret.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest().upper()


# SigSecret='a77b249029c22ee5'
# sig='MA35PU38X2/cNwWYNSKtY94JOwMyBdJ4NARIbeNWMHtNnc9UkY+NVTtNGHrG6EzN8AW4cRpPqZj3/e73u3ub/jhGoGQn0Eg==201906201441430001'
# print(hmac_md5(SigSecret,sig))