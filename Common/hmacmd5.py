#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 16:56
# @Author  : taojian
# @Site    : 
# @File    : hmacmd5.py
# @Software: PyCharm


import hmac

def hmac_md5(key, s):
    '''
    :param key:key就是你们的秘钥
    :param s:s就是你要去拼接的参数
    :return:
    '''
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest().upper()


key='1234567890abcdef'
s='12345ABCDmYvffpNoFf4E/ZTC1tOw4xAtlzJ8iDQ7piNNiKgQpHlhTiJwbO5Ehc1CPOF1fk9JngohSuu7jgBIEPvCb2PILg==201708221132320001'
print(hmac_md5(key=key,s=s))