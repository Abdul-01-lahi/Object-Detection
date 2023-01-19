# import sys 
# from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
# if __name__=="__main__":
#     app = QApplication(sys.argv)
#     w = QWidget ()
#     w.resize(300,300)
#     w.setWindowTitle("Interview Wizard")
#     w.show()
#     sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QGridLayout, QDialog,QPushButton)
import math

class QuadraticSolver(QDialog):
    def __init__(self):
        super().__init__()

        # create the user interface
        self.create_ui()

    def create_ui(self):
        self.setWindowTitle("Quadratic Equation Solver")

        # create the labels
        a_label = QLabel("a:")
        b_label = QLabel("b:")
        c_label = QLabel("c:")
        x1_label = QLabel("x1:")
        x2_label = QLabel("x2:")

        # create the line edits
        self.a_edit = QLineEdit()
        self.b_edit = QLineEdit()
        self.c_edit = QLineEdit()
        self.x1_edit = QLineEdit()
        self.x2_edit = QLineEdit()

        # set the read only property for the answer fields
        self.x1_edit.setReadOnly(True)
        self.x2_edit.setReadOnly(True)

        # create the calculate button
        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate)

        # create the layout
        layout = QGridLayout()
        layout.addWidget(a_label, 0, 0)
        layout.addWidget(self.a_edit, 0, 1)
        layout.addWidget(b_label, 1, 0)
        layout.addWidget(self.b_edit, 1, 1)
        layout.addWidget(c_label, 2, 0)
        layout.addWidget(self.c_edit, 2, 1)
        layout.addWidget(x1_label, 3, 0)
        layout.addWidget(self.x1_edit, 3, 1)
        layout.addWidget(x2_label, 4, 0)
        layout.addWidget(self.x2_edit, 4, 1)
        layout.addWidget(calculate_button, 5, 0, 1, 2)

        self.setLayout(layout)
    def calculate(self):
        a = float(self.a_edit.text())
        b = float(self.b_edit.text())
        c = float(self.c_edit.text())

        # calculate the roots of the quadratic equation
        discriminant = b**2 - 4*a*c
        if discriminant >= 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            self.x1_edit.setText(str(x1))
            self.x2_edit.setText(str(x2))
        else:
            self.x1_edit.setText("Imaginary")
            self.x2_edit.setText("Imaginary")

       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    solver = QuadraticSolver()
    solver.show()
    sys.exit(app.exec_())

