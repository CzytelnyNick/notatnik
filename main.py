from PyQt6.QtWidgets import (
    QApplication,
    QToolBar,
    QMainWindow,
    QWidget,
    QMessageBox,
    QPushButton,
    QLabel,
    QFileDialog, QVBoxLayout, QFontDialog, QFontComboBox
)
from PyQt6 import QtCore, uic, QtSvg, QtGui
from PyQt6.QtGui import QPixmap, QAction, QIcon, QFont, QFontDatabase
import sys
import subprocess


class Login(QMainWindow):
    def __init__(self):
        super().__init__()


        toolbar = QToolBar()
        # font = QFontDialog.getFont()
        # print(font)
        newFile = QAction(QIcon("images//file.png"), "New File", self)
        openFile = QAction(QIcon("images//open.png"), "New File", self)
        undo = QAction(QIcon("images//undo.png"), "New File", self)
        redo = QAction(QIcon("images//redo.png"), "New File", self)
        cut = QAction(QIcon("images//cut.png"), "New File", self)
        copy = QAction(QIcon("images//copy.png"), "New File", self)
        paste = QAction(QIcon("images//paste.png"), "New File", self)
        newFile = QAction(QIcon("images//file.png"), "New File", self)
        newFile = QAction(QIcon("images//file.png"), "New File", self)
        toolbar.addAction(newFile)
        toolbar.addAction(openFile)
        toolbar.addAction(undo)
        toolbar.addAction(redo)
        toolbar.addAction(cut)
        toolbar.addAction(copy)
        toolbar.addAction(paste)
        toolbar.addSeparator()
        test = QFontComboBox()
        
        toolbar.addWidget(test)
        # toolbar.addAction(newFile)
        # toolbar.addAction(newFile)
        self.addToolBar(toolbar)
        self.showMaximized()


        self.show()

    def openFileExplorer(self):
        global dialog
        dialog = QFileDialog.getOpenFileName(directory="C:\\Users\\4TP2\\Desktop\\python\\designer\\galeria")
        print(dialog[0])
        dialog = dialog[0]


app = QApplication(sys.argv)
logowanie = Login()
sys.exit(app.exec())
