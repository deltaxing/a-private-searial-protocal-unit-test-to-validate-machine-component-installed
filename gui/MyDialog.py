import sys
import random
from typing import List
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QMessageBox, QPushButton


class MyDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        # self.addButton("显示正常",self.ButtonRole.AcceptRole)
        # self.addButton("错误",self.ButtonRole.RejectRole)
        # self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("电梯显示屏显示了 大大大 字符",
                                     alignment=QtCore.Qt.AlignCenter)
        self.button.setWindowRole

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        # self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


def show(title:str,text:str,buttons:List[str]):
    app = QtWidgets.QApplication([])
    msgBox = QMessageBox()
    msgBox.setWindowTitle(title)
    msgBox.setInformativeText("<p style=font-size:50px>{}</p>".format(text))
    qtButtons = []
    for button in buttons:        
        qtButtons.append(msgBox.addButton(button, QMessageBox.YesRole))
    msgBox.setStyleSheet("QMessageBox {background-color: yellow;width:400px}")
    msgBox.exec()
    
    return buttons[ qtButtons.index(msgBox.clickedButton()) ]
    

    if msgBox.clickedButton() == connectButton:
        print(11)
    elif msgBox.clickedButton() == abortButton:
        print(22)
    # return QtWidgets.QMessageBox.information(app, "测试动画", text="请查看 电梯显示屏 是否 显示了 A",
#                                          button0= QtWidgets.QMessageBox.Ok,
#                                          button1 = QtWidgets.QMessageBox.Cancel,
#                                          defaultButton=QtWidgets.QMessageBox.Ok)
# sys.exit(app.exec())
