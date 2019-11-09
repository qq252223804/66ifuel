import json,os

# datas={"app_id": 'b1044830052f359d',
#       "timestamp": '2019-9-25 2:35:56',
#       "version": '1.0',
#       "client": 'android',
#       "client_version": '4.0.1',
#       "device_id": '123123',
#       "access_token": '',
#       "method": 'user.register',
#       "biz_content": '{"phone":"18657738815","password":"e10adc3949ba59abbe56e057f20f883e"}',
#       }
#
# if __name__ == '__main__':
#     a=dict(sorted(datas.items(),key=lambda x:x[0],reverse=False))
#     # print(a)
#     # str_key='='.join(a)
#     # print(str_key)
#     str1=[]
#     for i,u in zip(a.keys(),a.values()):
#         str1.append(i+"="+u)
#     # print(str1)
#     str_night='&'.join(str1)
#     print(str_night)
#
#     datas.update({"sign":1})
#     print(datas)
#
#
