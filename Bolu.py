import sys
# import rsa
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QMessageBox,QLineEdit,QLabel,QTextEdit
def showondisplay():
    freshlytextentered = entertext.toPlainText()
    displaytext.setText(freshlytextentered)

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(900,900)
    w.setWindowTitle("Ghost Text")


    displaytext = QTextEdit(w)
    displaytext.resize(800,300)
    displaytext.move(50,50)
    displaytext.setReadOnly(True)
    displaytext.setStyleSheet ("background-color: black; color: white")


    entertext = QTextEdit(w)
    entertext . resize(800,300)
    entertext . move(50,550)
    entertext . setReadOnly(False)
    entertext . setStyleSheet ("background-color: white; color: black")
    entertext . setPlaceholderText("Enter text Here")
    entertext . textChanged.connect(showondisplay)



    w.show()
    sys.exit(app.exec_())
