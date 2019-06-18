import os
import configparser   #导入configparser库，用于读取配置文件
#用os模块来读取
curpath=os.path.dirname(os.path.abspath(__file__))
cfgpath=os.path.join(curpath,"conf.ini")  #读取到本机的配置文件

# 创建管理对象
config=configparser.ConfigParser()
# 并读取ini文件
config.read(cfgpath,encoding='utf-8-sig')

#key取值 针对不同section
mysql_info=config.get("test_db","mysql_info")
app_host=config.get("host","app_host")
cms_host=config.get("host","cms_host")
datas1=config.get("delear_info","datas1")
datas2= config.get("user_info",'datas2')
cms_headers=config.get("cms_headers",'headers')
print(mysql_info+'\n',app_host+'\n',cms_host+'\n',datas1+'\n',datas2+'\n',cms_headers+'\n')


# from Config import config
# print(config.host)