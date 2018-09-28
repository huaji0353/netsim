#coding:utf-8
'''
thanks 感谢
坐标移动算法：https://stackoverflow.com/a/12221360
'''
from PySide import QtCore, QtGui
import sys

def log(string):
	#log(string)
	pass


class RTmemu(QtGui.QMenu):
	def __init__(self, parent):
		super(RTmemu, self).__init__(parent)
	
class Node(QtGui.QLabel):
	def __init__(self, parent, name, pos, pic):
		super(Node, self).__init__(parent)
		self.parent = parent
		self.name = name
		self.previousPosition = QtCore.QPoint()
		self.move(pos)
		
		image = pic
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
		elif event.button() == QtCore.Qt.RightButton:
			print(self.name)
			#TODO

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
				return
			log("r")

class Root(QtGui.QWidget):
	def __init__(self, parent=None):
		super(Root, self).__init__(parent)
		self.items = []

	def mousePressEvent(self, event):
		if event.buttons() == QtCore.Qt.RightButton:
			self.additems("Router")
		if event.button() == QtCore.Qt.LeftButton:
			self.additems("Pc")
			#TODO

	def additems(self, types):
		n = Node(self, types, QtCore.QPoint(10, 10), QtGui.QImage("./icon/%s.png"%types))
		n.show()
		self.items.append(n)

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	root = Root()
	root.resize(800, 600)
	root.show()
	sys.exit(app.exec_())
