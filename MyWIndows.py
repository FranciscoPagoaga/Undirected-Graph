from Undirected_Graph import Vertex, Graph 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen
import sys
    
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.title = "Grafo No Dirigido"

        self.top = 700

        self.left = 200

        self.width = 800

        self.height = 800

        self.InitWindow()
    
    def InitWindow(self):
        self.setWindowTitle(self.title)

        self.setGeometry(self.top, self.left, self.width, self.height)

        labelEdges = QtWidgets.QLabel(self)
        labelEdges.setText("Enter Edges:")
        labelEdges.move(50,20)

        inputEdges = QtWidgets.QTextEdit(self)
        inputEdges.setPlaceholderText("Ex: A,B,C,D,E")
        inputEdges.setMaximumWidth(500)
        inputEdges.setFixedWidth(500)
        inputEdges.move(50,50)

        labelVertex = QtWidgets.QLabel(self)
        labelVertex.setText("Enter Vertex")
        labelVertex.move(50,80)

        inputEdges = QtWidgets.QTextEdit(self)
        inputEdges.setPlaceholderText("Ex: (A,B),(A,C),(B,C)")
        inputEdges.setMaximumWidth(500)
        inputEdges.setFixedWidth(500)
        inputEdges.move(50,110)

        submitButton = QtWidgets.QPushButton(self)
        submitButton.setText("Get Undirected Graph")
        submitButton.setMaximumWidth(200)
        submitButton.setFixedWidth(190)
        submitButton.move(50,160)



        self.show()

    def paintEvent(self, event):
            pen= QPen()
            pen.setWidth(5)
            painter = QPainter(self)
            painter.setPen(pen)
            painter.drawRect(50,300,700,450)

# def window():
#     app = QApplication(sys.argv)
#     win = QMainWindow()
#     win.setGeometry(700,200,800,800)
#     win.setWindowTitle("Grafo No Dirigido")

#     labelEdges = QtWidgets.QLabel(win)
#     labelEdges.setText("Enter Edges:")
#     labelEdges.move(50,20)

#     inputEdges = QtWidgets.QTextEdit(win)
#     inputEdges.setPlaceholderText("Ex: A,B,C,D,E")
#     inputEdges.setMaximumWidth(500)
#     inputEdges.setFixedWidth(500)
#     inputEdges.move(50,50)

#     labelVertex = QtWidgets.QLabel(win)
#     labelVertex.setText("Enter Vertex")
#     labelVertex.move(50,80)

#     inputEdges = QtWidgets.QTextEdit(win)
#     inputEdges.setPlaceholderText("Ex: (A,B),(A,C),(B,C)")
#     inputEdges.setMaximumWidth(500)
#     inputEdges.setFixedWidth(500)
#     inputEdges.move(50,110)

#     submitButton = QtWidgets.QPushButton(win)
#     submitButton.setText("Get Undirected Graph")
#     submitButton.setMaximumWidth(200)
#     submitButton.setFixedWidth(190)
#     submitButton.move(50,160)

#     pen= QPen()
#     pen.setWidth(10)
#     painter = QPainter(win)
#     painter.setPen(pen)
#     painter.drawEllipse(300,300,100,100)

#     win.show()
#     sys.exit(app.exec_())

App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())