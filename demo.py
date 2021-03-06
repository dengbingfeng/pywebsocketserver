# -*- coding: utf8 -*-
import sys
from pywebsocketserver.server import SocketServer
from pywebsocketserver.baseio import BaseIO

class MyIO(BaseIO):
    def onData(self,uid,text):
        self.sendData(uid,"我收到了你的消息：%s"%(text,))
    def onConnect(self,uid):
        self.sendData(uid,"一条中文")

try:
    port = sys.argv[1]
except:
    port = 81

port = int(port)
myIo = MyIO()
SocketServer(port,myIo).run()    
