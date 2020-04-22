#coding: UTF-8
import paho.mqtt.client as mqtt
import time
 
user = "userKNP"                    # 用户名
pwd = "F3gIebb0lBFoiuqa"                       # 密码
endpoint =  "mqtt.eclipse.org"        # 连接地址 "mqtt.eclipse.org"   
port = 1883                       # 1883为服务端口号，如果是安全认证，端口号需要修改为1884
topic = "testtopic/1"            # 发布消息主题

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))  # 打印连接状态
    client.subscribe(topic)  # 填写订阅的主题
 
 
def on_message(client, userdata, msg):
    print(msg.topic+" " + ":" + str(msg.payload))  # 打印接受的消息
 
 
client_id = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))   # 以当前时间作为client_id
client = mqtt.Client(client_id)    # ClientId不能重复，所以使用当前时间
client.username_pw_set(user, pwd) # 设置连接用户和密码，必须设置，否则会返回Connected with result code 4
client.on_connect = on_connect
client.on_message = on_message
client.connect(endpoint, port, 60)   # port=1883为服务端口号，如果是安全认证，端口号需要修改为1884
client.loop_forever()
