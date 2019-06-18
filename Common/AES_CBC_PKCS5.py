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
    bs = AES.block_size
    length = len(text)
    bytes_length = len(bytes(text, encoding='utf-8'))
    padding_size = length if(bytes_length == length) else bytes_length
    padding = bs - padding_size % bs
    padding_text = chr(padding) * padding
    return text + padding_text

def encrypt(key, content):
    key_bytes = bytes(key, encoding='utf-8')
    iv = key_bytes
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    content_padding = pkcs5padding(content)
    encrypt_bytes = cipher.encrypt(bytes(content_padding, encoding='utf-8'))
    result = str(base64.b64encode(encrypt_bytes), encoding='utf-8').replace('\n', '')
    return result

key = '1234567890abcdef'
text = '{"OperatorID":"12345ABCD","OperatorSecret":"1234567890abcdef"}'

sign = encrypt(key,text)
print(sign)