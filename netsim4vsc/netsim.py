'''
OSI七层模型(只仿真3层)：l1=> link, l2=> MAC, l3=> IP
'''
class Engine(object):
	def __init__(self):
		# 初始化
		self.packet = None

	def pullout(self):
		# 从拉出一个包
		return self.packet

	def pushin_run(self, packet):
		# 压入一个包给引擎处理直到收到结束信号
		self.run()

	def flush_draw(self):
		# 刷新画面
		pass

e = Engine()
running = True
while running:
	TMPpacket = e.pullout()
	e.pushin_run(TMPpacket)
	e.flush_draw()
	time.sleep(0.02)

class device(object):
	def __init__(self):
		pass

	def port_fa0(self):
		pass
	
	def process(self):
		pass

def link(start_port, end_port, name):
	pass

n1 = device()
n2 = device()
link(n1.port_fa0, n2.port_fa0, "thefirstline")