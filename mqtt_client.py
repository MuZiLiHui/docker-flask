#coding: UTF-8
import time
import paho.mqtt.client as mqtt
import datetime
 
 
def on_publish(msg, rc):   # 成功发布消息的操作
    if rc == 0:
        print("publish success, msg = " + msg)
 
 
def on_connect(client, userdata, flags, rc):   # 连接后的操作 0为成功
    print("Connection returned " + str(rc))
 
 
user = "userKNP"                    # 用户名
pwd = "F3gIebb0lBFoiuqa"                       # 密码
endpoint =  "mqtt.eclipse.org"            # 连接地址 "broker.mqttdashboard.com" 
port =  1883                      # 1883为服务端口号，如果是安全认证，端口号需要修改为1884 31338
topic = "testtopic/1"            # 发布消息主题
 
client_id = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
client = mqtt.Client(client_id)    # ClientId不能重复，所以使用当前时间
client.username_pw_set(user, pwd)  # 设置用户名，密码
client.connect(endpoint, port, 60)  # 连接服务 keepalive=60
client.on_connect = on_connect  # 连接后的操作
client.loop_start()
time.sleep(2)
count = 0
 
while count < 500:  # 发布五条消息
    count = count + 1
    msg = str(datetime.datetime.now())
    rc, mid = client.publish(topic, payload=msg, qos=1)  # qos
    on_publish(msg, rc)
    time.sleep(2)
