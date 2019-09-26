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
    #hexdigest() 作为十六进制数据字符串值  upper()转为大写
    return hmac.new(SigSecret.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest().upper()

def hmac_md5_low(SigSecret,s):
    '''
    :param key:key就是签名秘匙
    :param s:s就是你要去拼接的参数
    :return:
    '''
    return hmac.new(SigSecret.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

def new_hmac_md5(SigSecret,data):
    '''
        :param key:key就是签名秘匙
        :param data:data就是你要去拼接的参数
        :return:
    '''
    # 第一步，设所有发送或者接收到的数据为集合M，将集合M内非空参数值的参数按照参数名ASCII码从小到大排序（字典序），使用URL键值对的格式（即key1 = value1 & key2 = value2…）拼接成字符串stringA。
    # 特别注意以下重要规则：1.
    # 参数名ASCII码从小到大排序（字典序）；2.
    # 如果参数的值为空不参与签名；3.
    # 参数名区分大小写；
    # 第二步，采用HMAC - MD5算法，采用MD5作为散列函数，通过签名密钥（SigSecret）对stringA进行加密，然后采用Md5信息摘要的方式形成新的密文
    a=dict(sorted(data.items(),key=lambda x:x[0],reverse=False))
    str1 = []
    for i, u in zip(a.keys(), a.values()):
        str1.append(i + "=" + u)
    # print(str1)
    str_night = '&'.join(str1)
    # print(str_night)

    return hmac.new(SigSecret.encode('utf-8'), str_night.encode('utf-8'), 'MD5').hexdigest()
if __name__ == '__main__':

    # SigSecret='a77b249029c22ee5'
    # sig='MA35PU38X2/cNwWYNSKtY94JOwMyBdJ4NARIbeNWMHtNnc9UkY+NVTtNGHrG6EzN8AW4cRpPqZj3/e73u3ub/jhGoGQn0Eg==201906201441430001'
    # print(hmac_md5(SigSecret,sig))
    #
    # SigSecret='204414295c2f3fbc5818f604793f1ba2'
    # sig='getMemberType1.0.020190823182427{"company_id": 1}'
    # print(hmac_md5_low(SigSecret,sig))
    # print(type(hmac_md5(SigSecret,sig)))

    datas = {"app_id": 'b1044830052f359d',
             "timestamp": '2019-9-25 2:35:56',
             "version": '1.0',
             "client": 'android',
             "client_version": '4.0.1',
             "device_id": '123123',
             "method": 'user.register',
             "biz_content": '{"phone":"18657738815","password":"e10adc3949ba59abbe56e057f20f883e"}',
             }

    SigSecret = '204414295c2f3fbc5818f604793f1ba2'
    print(new_hmac_md5(SigSecret, datas))


