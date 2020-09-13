from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from guieInitCode import Ui_MainWindow
import time
from datetime import datetime
import re

class Hasher(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.pressed.connect(self.button_pressed)

	def fnd(self, sum):
		rezult = 0
		i = 2
		while True:
			if sum%i == 0:
				if sum/i == 1:
					rezult +=i
					break
				else:
					sum/=i
					#print(i,end =' ')
					rezult +=i
					i=2
			else:
				i+=1
		return rezult			

	def email_p(self, email):
		print(email)
		try:
			if(int(email)%1 == 0):
				print('numbers')
				return 0
		except ValueError:
			pass		
		reg = re.compile('[^a-zA-Z ]')
		email = reg.sub('', email).lower()
		print(email)
		sum = 0
		for letter in email:
			sum+=ord(letter)-96
		return sum

	def output(self,rez):
		self.rezult.setText(str(rez))

	def start(self,email):
		sum = self.email_p(email)
		if sum == 0: 
			self.output(sum)
			return	
		rez = self.fnd(sum)
		while rez != self.fnd(rez):
			rez = self.fnd(rez)
		
		self.output(rez)	
		print(rez)

	def button_pressed(self):
		email = self.lineEdit.text()
		if(len(email)!=0):
			self.start(email)


app = QtWidgets.QApplication([])
window = Hasher()
window.show()
app.exec_()



