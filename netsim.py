#coding:utf-8
import time

class Interface():
	def __init__(self, master, name):
		# 一个接口应该有滞留点与连接点, 读与写属性
		self.remain_packet = None
		self.linkto = None

		self.name = name
		self.master = master
	
	def link(self, node):
		# 连接到下一个接口
		self.linkto = node
		
	def write(self, packet):
		# 写滞留包
		self.remain_packet = packet
		
	def nextframe(self):
		# 下一帧，转移滞留包
		linkto = self.linkto
		print(self.master+"->"+linkto.master+" "*4+self.remain_packet)
		linkto.remain_packet = self.remain_packet
		self.remain_packet = None

class device():
	def __init__(self, name):
		# 设备硬件接口
		self.name = name
		self.interface_list = {}
		
	def interface_new(self):
		# 生成名字，加入接口数组，返回新接口<interface>对象
		name = "eth"+str(len(self.interface_list)+1)
		interface_new = Interface(self.name, name)
		self.interface_list[name] = interface_new
		return interface_new
		
	def interface_process(self, interface):
		# 处理接口与接口的包
		if interface.remain_packet == "hello???":
			interface.write("I'mOK")
		elif interface.remain_packet == "I'mOK":
			interface.write("hello???")
		else:
			return 0
		interface.nextframe()
		
	def nextframe(self):
		# 遍历滞留接口，如存在包，则使用接口下一帧
		for interface in self.interface_list:
			f = self.interface_list[interface]
			if f:
				self.interface_process(f)

def link(f1, f2, name=""):
	# 设备->接口 调用实现层
	f1.link(f2)
	f2.link(f1)

n1 = device("n1")
n2 = device("n2")
f1 = n1.interface_new()
f2 = n2.interface_new()
link(f1, f2, "thefristline")

f1.write("hello???")
# a_packet
alive = True
while alive:
	n1.nextframe()
	n2.nextframe()
	time.sleep(0.1)