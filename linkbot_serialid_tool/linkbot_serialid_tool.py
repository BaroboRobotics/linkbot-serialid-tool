#!/usr/bin/env python3

__version__ = "0.0.1"

from PyQt4 import QtCore, QtGui

try:
    from linkbot_serialid_tool.dialog import Ui_Dialog
except:
    from dialog import Ui_Dialog

import linkbot
import sys
import time

class StartQT4(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.buttonBox.accepted.connect(self.accepted)
        self.ui.buttonBox.clicked.connect(self.buttonBoxClicked)
        self.ui.getId_pushButton.clicked.connect(self.getCurrentId)
        self.ui.selectAll_pushButton.clicked.connect(
            self.ui.serialId_lineEdit.selectAll)

    def accepted(self):
        try:
            self.programCurrentSerialId()
            sys.exit(0)
        except Exception as e:
            QtGui.QMessageBox.warning(self, "Error: ", str(e))

    def buttonBoxClicked(self, button):
        role = self.ui.buttonBox.buttonRole(button)
        try:
            if role == self.ui.buttonBox.RejectRole:
                sys.exit(0)
            elif role == self.ui.buttonBox.ResetRole:
                self.ui.serialId_lineEdit.setText('')
            elif role == self.ui.buttonBox.ApplyRole:
                self.programCurrentSerialId()
        except Exception as e:
            QtGui.QMessageBox.warning(self, "Error: ", str(e))

    def programCurrentSerialId(self):
        l = linkbot.Linkbot()
        newId = self.ui.serialId_lineEdit.text().upper()
        if len(newId) != 4:
            raise Exception("Serial IDs must be 4 characters long.")
        l._setSerialId(newId)
        l.setBuzzerFrequency(440)
        time.sleep(0.5)
        l.setBuzzerFrequency(0)

    def getCurrentId(self):
        try:
            l = linkbot.Linkbot()
            QtGui.QMessageBox.information(self, "Serial ID", "Serial ID: " + l.getSerialId())
        except Exception as e:
            QtGui.QMessageBox.warning(
                self,
                "Warning", 
                "Could not get the Linkbot's serial ID. Is the Linkbot plugged "
                "in?\n\n" + str(e))

def main():
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
