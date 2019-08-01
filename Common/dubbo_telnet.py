import dubbo_telnet

def coondoubble_data(Host,Port,interface,method,param):
    # try:
        # 初始化dubbo对象
        conn = dubbo_telnet.connect(Host, Port)
        # 设置telnet连接超时时间
        conn.set_connect_timeout(10)
        # 设置dubbo服务返回响应的编码
        conn.set_encoding('utf-8')
        conn.invoke(interface, method, param)
        command = 'invoke %s.%s(%s)'%(interface,method,param)
        return  conn.do(command)
    # except:
    #     return  Exception
if __name__=="__main__":
    Host = '192.168.3.142'  # Doubble服务器IP
    Port = 20983  # Doubble服务端口
    interface = 'com.ifuel.cec.manager.client.service.PartnersService'  # 接口
    method = 'queryPartnersByOperatorId'  # 方法
    param = '{"operatorId": "745467123"}'  # 参数
    data=coondoubble_data(Host,Port,interface,method,param)
    print(data)