from PyQt6.QtWidgets import (
    QApplication,
    QToolBar,
    QMainWindow,
    QFontComboBox,
    QTextEdit, QMessageBox, QSpinBox, QFileDialog
)
from PyQt6.QtGui import QAction, QIcon
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.toolbar = QToolBar()
        newFile = QAction(QIcon("images//file.png"), "New File", self)
        openFile = QAction(QIcon("images//open.png"), "Open File", self)
        undo = QAction(QIcon("images//undo.png"), "Undo", self)
        redo = QAction(QIcon("images//redo.png"), "Redo", self)
        cut = QAction(QIcon("images//cut.png"), "Cut", self)
        copy = QAction(QIcon("images//copy.png"), "Copy", self)
        paste = QAction(QIcon("images//paste.png"), "Paste", self)
        italic = QAction(QIcon("images//i.png"), "Italic", self)
        bold = QAction(QIcon("images//b.png"), "Bold", self)
        underline = QAction(QIcon("images//u.png"), "Underline", self)
        save = QAction(QIcon("images//save.png"), "Save", self)
        self.toolbar.addAction(newFile)
        self.toolbar.addAction(openFile)
        self.toolbar.addAction(save)
        self.toolbar.addAction(undo)
        self.toolbar.addAction(redo)
        self.toolbar.addAction(cut)
        self.toolbar.addAction(copy)
        self.toolbar.addAction(paste)
        self.toolbar.addSeparator()
        self.fontStyle = QFontComboBox()
        self.fontSize = QSpinBox()
        self.fontSize.setValue(30)
        self.fontSize.setFixedWidth(40)

        self.toolbar.addWidget(self.fontStyle)
        self.toolbar.addWidget(self.fontSize)
        self.toolbar.addSeparator()
        self.toolbar.addAction(bold)
        self.toolbar.addAction(italic)
        self.toolbar.addAction(underline)
        self.textArea = QTextEdit()
        # toolbar.addAction(newFile)
        self.setCentralWidget(self.textArea)

        # toolbar.addAction(newFile)
        self.addToolBar(self.toolbar)
        self.showMaximized()
        
        newFile.triggered.connect(self.newFileFunc)
        openFile.triggered.connect(self.openFileExplorer)
        # self.fontStyle.activated.connect(self.setFontSize())

        self.show()

    def clearFunc(self):
        self.textArea.setText("")
    def newFileFunc(self):
        # print("AA")


        msgBox = QMessageBox()
        msgBox.setText("Czy napewno chcesz usunąć całą zawartość")

        msgBox.setIcon(QMessageBox.Icon.Warning)
        msgBox.setStandardButtons(
                               QMessageBox.StandardButton.Ok |
                               QMessageBox.StandardButton.Cancel)

        msgBox.setDefaultButton(QMessageBox.StandardButton.Cancel)
        ret = msgBox.exec()
        if ret == 1024:
            self.clearFunc()
    def setFontSize(self):
        # self.textArea.setFont()
        print(self.fontStyle.currentFont())
    def openFileExplorer(self):
        global dialog
        dialog = QFileDialog.getOpenFileName(filter="HTML (*.html)")
        print(dialog[0])
        dialog = dialog[0]

app = QApplication(sys.argv)
logowanie = MainWindow()
sys.exit(app.exec())
