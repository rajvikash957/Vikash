import sys
from area import *
from PyQt5 import QtWidgets, QtGui, QtCore

import sqlite3
con = sqlite3.connect('newgwater')

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues) 

   

  def insertvalues(self):
         
     with con:
    
        cur = con.cursor()
        cstd = str(self.ui.lineEdit.text())
        acode = str(self.ui.lineEdit_3.text())
        aname = str(self.ui.lineEdit_4.text())
        ccode = str(self.ui.lineEdit_5.text())
        cntry = str(self.ui.lineEdit_6.text())	
        astd = str(self.ui.lineEdit_2.text())
        state = str(self.ui.lineEdit_7.text())
        city = str(self.ui.lineEdit_8.text())
        cur.execute('INSERT INTO area VALUES(?,?,?,?,?,?,?,?)',(acode,aname,ccode,cntry,cstd,astd,state,city))
        con.commit()
        

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
