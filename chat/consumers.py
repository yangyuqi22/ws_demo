from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json


class ChatConsumer(WebsocketConsumer):  # 继承WebsocketConsumer
   def websocket_connect(self, message):
       print("有人进行了连接")
       # 有客户端向后端发送 WebSocket 连接的请求时，自动触发(握手)
       self.accept()
       #将这个客户端的连接放在redis
       group_id=self.scope['url_route']['kwargs'].get("group")
       # 将这个客户端加入到一个组中，组名是
       async_to_sync(self.channel_layer.group_add)(group_id,self.channel_name)

   def websocket_receive(self, message):
       # 浏览器基于 WebSocket 向后端发送数据，自动触发接收消息
       print("收到消息：", message)
       channel_name = self.channel_name
       print("Received message from channel:", channel_name)
       # 向所有连接的客户端发送消息,让他们去执行group.message的方法
       group_id=self.scope['url_route']['kwargs'].get("group")
       async_to_sync(self.channel_layer.group_send)(group_id,{"type":"group.message","text":message["text"]})

   def group_message(self,event):
       message = event["text"]
       # 向所有连接的客户端发送消息,让他们去执行group.message的方法
       self.send(message)
       

   def websocket_disconnect(self, message):
       # 客户端向服务端断开连接时，自动触发
       group_id=self.scope['url_route']['kwargs'].get("group")
       async_to_sync(self.channel_layer.group_discard)(group_id,self.channel_name)
       raise StopConsumer()
