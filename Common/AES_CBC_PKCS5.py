#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 18:09
# @Author  : taojian
# @Site    : 
# @File    : AES_CBC_PKCS5.py
# @Software: PyCharm

from Crypto.Cipher import AES
import base64

def pkcs5padding(text):
    '''
    填充模式采用PKCS5Padding方式
    :param text:
    :return:
    '''
    bs = AES.block_size
    length = len(text)
    bytes_length = len(bytes(text, encoding='utf-8'))
    padding_size = length if(bytes_length == length) else bytes_length
    padding = bs - padding_size % bs
    padding_text = chr(padding) * padding
    return text + padding_text

def encrypt(DataSecret,content):
    '''
    AES加密
    :param key: key为消息秘匙
    :param content: contest为加密内容
    :return:
    '''
    # 消息秘钥初始化向量(DataSecretIV):
    DataSecretIV='117239bf13a40cd0'
    key_bytes = bytes(DataSecret, encoding='utf-8')
    iv = bytes(DataSecretIV, encoding='utf-8')
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    content_padding = pkcs5padding(content)
    # 目前AES-128 足够目前使用(CBC加密)
    encrypt_bytes = cipher.encrypt(bytes(content_padding, encoding='utf-8'))
    # base64加密
    result = str(base64.b64encode(encrypt_bytes), encoding='utf-8').replace('\n', '')
    return result
def pkcs5unpadding(text):
    '''
    填充模式采用PKCS5Padding方式
    :param text:
    :return:
    '''

    length = len(text)
    unpadding = ord(text[length-1])
    return text[0:length-unpadding]

def decrypt(key, content):
    '''
    AES 128位加密，加密模式采用CBC
    :param key: key为消息秘匙
    :param content: content为解密内容
    :return:
    '''
    # 消息秘钥初始化向量(DataSecretIV):

    DataSecretIV='117239bf13a40cd0'
    key_bytes = bytes(key, encoding='utf-8')
    iv = bytes(DataSecretIV, encoding='utf-8')
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    encrypt_bytes = base64.b64decode(content)
    decrypt_bytes = cipher.decrypt(encrypt_bytes)
    result = str(decrypt_bytes, encoding='utf-8')
    result = pkcs5unpadding(result)
    return result

DataSecret = 'bed30540c54dda5d'
#加密
text ='{"OperatorID":"MA35PU38X","OperatorSecret":"08083ebe79bc48a9"}'
data = encrypt(DataSecret,text)
print(data)
#解密
# untext='h0N5kfvVWFAi6mu31Ebna+Rf6pYNxXwsXQkaYx0y3R1U2rh9GAI/Po/jsVS+1OfglhTKiTwkthiDAUpaUgOvvQw18nt36laKO/mTgnth57oIad16CVHFgtTIyHa/1Y0K6j/hdCza3fdkfZhNmuYbLyOwAmkzDLB4gm5eIddj7uWfsyMCSaCcmgcImvDfzguq'
# undata=decrypt(DataSecret,untext)
# a=eval(undata)['AccessToken']
# b={"token":""}
# b['token']=a
# print(b)
