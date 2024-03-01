from PyQt6.QtWidgets import (
    QApplication,
    QToolBar,
    QMainWindow,
    QFontComboBox,
    QTextEdit, QMessageBox, QSpinBox, QFileDialog, 
)
from PyQt6.QtGui import QAction, QIcon, QFont, QTextCharFormat
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
        self.boldCheck = 0
        self.italicCheck = 0
        # toolbar.addAction(newFile)
        self.addToolBar(self.toolbar)
        self.showMaximized()
        
        newFile.triggered.connect(self.newFileFunc)
        openFile.triggered.connect(self.openFileExplorer)
        # self.fontStyle.activated.connect(self.setFontSize())
        save.triggered.connect(self.saveFile)
        bold.triggered.connect(self.setBold)
        italic.triggered.connect(self.setItalic)
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
        dialog = QFileDialog.getOpenFileName(filter="HTML (*.html)")
        print(dialog)  # Wydrukowanie ścieżki do pliku
        if dialog:  # Sprawdzenie, czy użytkownik wybrał plik
            with open(dialog[0], 'r') as file:
                content = file.read()  # Odczytanie zawartości pliku
                self.textArea.setText(content)
    def saveFile(self):
        text = self.textArea.toHtml()
        print(text)
    def getSelectedText(self):
        selected_text = self.textArea.textCursor().selectedText()
        if selected_text:
            return selected_text
    def setBold(self):
        if self.boldCheck == 0:
            text = self.textArea.textCursor()
            text_format = QTextCharFormat()
            text_format.setFontWeight(700)  # Ustawienie pogrubienia tekstu
            text.mergeCharFormat(text_format)
            self.boldCheck = 1
        elif self.boldCheck == 1:
            text = self.textArea.textCursor()
            text_format = QTextCharFormat()
            text_format.setFontWeight(400)  # Ustawienie pogrubienia tekstu
            text.mergeCharFormat(text_format)
            self.boldCheck = 0
            
        
    def setItalic(self):
        if self.italicCheck == 0:
            text = self.textArea.textCursor()
            text_format = QTextCharFormat()
            text_format.setFontItalic(True)
            text.mergeCharFormat(text_format)
            self.italicCheck = 1
        elif self.italicCheck == 1:
            text = self.textArea.textCursor()
            text_format = QTextCharFormat()
            text_format.setFontItalic(False)
            text.mergeCharFormat(text_format)
            self.italicCheck = 0
        
        
        
app = QApplication(sys.argv)
logowanie = MainWindow()
sys.exit(app.exec())
