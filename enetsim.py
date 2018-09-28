# coding:utf-8
'''
PC：设备实体:=>默认接口，设备MAC地址|处理包函数(OS层)
设备：接口实体:=>设备名，{接口名:接口类}字典|处理接口函数(硬件)
接口：接口名，对方接口实体指针，接口父设备实体指针
'''
from Queue import Queue, Empty
from threading import *
import time

class Engine:
	def __init__(self):
		"""初始化事件管理器"""
		# 事件对象列表
		self.__eventQueue = Queue()
		# 事件管理开关
		self.__active = False
		# 事件处理主线程
		self.__thread = Thread(target = self.__Run)
		# 事件响应函数表
		self.__handlers = {}
	
	def __Run(self):
		"""引擎运行时 RUNTIME"""
		while self.__active == True:
			try:
				# 获取事件间隔时间设置
				event = self.__eventQueue.get(block = True, timeout = 0.2)
				self.__EventProcess(event)
			except Empty:
				pass
	
	def __EventProcess(self, event):
		'''处理事件'''
		# 检查是否存在对该事件进行监听的处理函数
		if event.type_ in self.__handlers:
			# 若存在，则按顺序将事件传递给处理函数执行
			for handler in self.__handlers[event.type_]:
				handler(event)

	def Start(self):
		'''启动'''
		# 将事件管理器设为启动
		self.__active = True
		# 启动事件处理线程
		self.__thread.start()

	def Stop(self):
		"""停止"""
		# 将事件管理器设为停止
		self.__active = False
		# 等待事件处理线程退出
		self.__thread.join()

	def AddEventListener(self, type_, handler):
		"""绑定事件和监听器处理函数"""
		# 尝试获取该事件类型对应的处理函数列表，若无则创建
		try:
			handlerList = self.__handlers[type_]
		except KeyError:
			handlerList = []

		self.__handlers[type_] = handlerList
		# 若要注册的处理器不在该事件的处理器列表中，则注册该事件
		if handler not in handlerList:
			handlerList.append(handler)

	def SendEvent(self, event):
		"""发送事件，向事件队列中存入事件"""
		self.__eventQueue.put(event)


class Event:
	def __init__(self, type_=None):
		self.type_ = type_      # 事件类型
		self.dict = {}          # 字典用于保存具体的事件数据

def output(event):
	print(u"内容：%s"%event.dict["aaa"])

def inpot():
	ee = Event("e_aaa")
	ee.dict["aaa"] = "aaaaaaaaaaaaaaaaaaaaaaaa"
	e.SendEvent(ee)

if __name__ == '__main__':
	e = Engine()
	e.AddEventListener("e_aaa", output)
	e.Start()
	timer = Timer(2, inpot)
	timer.start()