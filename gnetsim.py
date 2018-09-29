#coding:utf-8
'''
thanks 感谢
坐标移动算法：https://stackoverflow.com/a/12221360
'''
from PySide import QtCore, QtGui
import sys

def log(string):
	#print(string)
	pass


class Node(QtGui.QLabel):
	def __init__(self, parent, types, pos, name=None):
		super(Node, self).__init__(parent)
		self.parent = parent
		self.name = name
		self.previousPosition = QtCore.QPoint()
		self.move(pos)
		
		image = QtGui.QImage("./icon/%s.png"%types)
		self.setPixmap(QtGui.QPixmap.fromImage(image))
		self.resize(image.width(), image.height())

	def mousePressEvent(self, event):
		self.__mousePressPos = None
		self.__mouseMovePos = None
		if event.button() == QtCore.Qt.LeftButton:
			self.__mousePressPos = event.globalPos()
			self.__mouseMovePos = event.globalPos()
			self.raise_()
			log("pl")

	def mouseMoveEvent(self, event):
		if event.buttons() == QtCore.Qt.LeftButton:
			# adjust offset from clicked point to origin of widget
			currPos = self.mapToGlobal(self.pos())
			globalPos = event.globalPos()
			diff = globalPos - self.__mouseMovePos
			newPos = self.mapFromGlobal(currPos + diff)
			self.move(newPos)
			
			self.__mouseMovePos = globalPos
			log("ml")

	def mouseReleaseEvent(self, event):
		if self.__mousePressPos is not None:
			moved = event.globalPos() - self.__mousePressPos 
			if moved.manhattanLength() > 3:
				event.ignore()
				#return
			log("r")

	def contextMenuEvent(self, event):
		menu = QtGui.QMenu(self)
		menu.addAction(QtGui.QAction("&Add Link", self, triggered=self.parent.update))
		menu.addAction(QtGui.QAction("&Del Link", self))
		menu.exec_(event.globalPos())

class View(QtGui.QGraphicsView):
	def __init__(self, parent=None):
		super(View, self).__init__(parent)
		self.items = []

	def mousePressEvent(self, event):
		#TODO#TODO#TODO#TODO#TODO#TODO
		if event.buttons() == QtCore.Qt.RightButton:
			pass
		if event.button() == QtCore.Qt.LeftButton:
			pass

	def contextMenuEvent(self, event):
		menu = QtGui.QMenu(self)
		menu.addAction(QtGui.QAction("&Add Pc", self, triggered=lambda:self.additems("Pc", event.pos())))
		menu.addAction(QtGui.QAction("&Add Router", self, triggered=lambda:self.additems("Router", event.pos())))
		menu.exec_(event.globalPos())

	def additems(self, types, pos):
		n = Node(self, types, pos)
		n.show()
		self.items.append(n)

class Root(QtGui.QWidget):
	def __init__(self):
		super(Root, self).__init__()
		self.layout = QtGui.QVBoxLayout()
		self.setLayout(self.layout)
		
		self.view = View(self)
		self.button = QtGui.QPushButton(parent=self)
		
		self.layout.addWidget(self.view)
		self.layout.addWidget(self.button)


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	root = Root()
	root.resize(800, 600)
	root.show()
	sys.exit(app.exec_())
