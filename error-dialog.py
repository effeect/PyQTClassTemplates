"""Generates a error dialog that can occur if conditions are met"""

from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import QMessageBox

class errorDialog:
    def __init__(self,windowTitle,message, additional, console):
        self.message = message
        self.windowTitle = windowTitle
        self.additional = additional
        self.console = console

    def showDialog(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)

        self.msg.setText(self.message)
        self.msg.setInformativeText(self.additional)
        self.msg.setWindowTitle(self.windowTitle)
        self.msg.setDetailedText(self.console)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.retval = self.msg.exec_()
