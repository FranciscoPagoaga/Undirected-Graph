from Undirected_Graph import Vertex, Graph 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen
import sys
import re
    
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

        self.labelVertex = QtWidgets.QLabel(self)
        self.labelVertex.setText("Enter Vertex:")
        self.labelVertex.move(50,20)

        self.inputVertex = QtWidgets.QTextEdit(self)
        self.inputVertex.setPlaceholderText("Ex: A,B,C,D,E")
        self.inputVertex.setMaximumWidth(500)
        self.inputVertex.setFixedWidth(500)
        self.inputVertex.move(50,50)

        self.labelEdges = QtWidgets.QLabel(self)
        self.labelEdges.setText("Enter Edges")
        self.labelEdges.move(50,80)

        self.inputEdges = QtWidgets.QTextEdit(self)
        self.inputEdges.setPlaceholderText("Ex: (AB),(AC),(BC)")
        self.inputEdges.setMaximumWidth(500)
        self.inputEdges.setFixedWidth(500)
        self.inputEdges.move(50,110)

        self.submitButton = QtWidgets.QPushButton(self)
        self.submitButton.setText("Get Undirected Graph")
        self.submitButton.setMaximumWidth(200)
        self.submitButton.setFixedWidth(190)
        self.submitButton.move(50,160)
        self.submitButton.clicked.connect(self.getGraphs)

        self.labelLowestDegree = QtWidgets.QLabel(self)
        self.labelLowestDegree.move(50,200)
        self.labelLowestDegree.setMaximumWidth(500)
        self.labelLowestDegree.setFixedWidth(500)
        
        self.labelDegreeSum = QtWidgets.QLabel(self)
        self.labelDegreeSum.move(50,220)
        self.labelDegreeSum.setMaximumWidth(500)
        self.labelDegreeSum.setFixedWidth(500)

        self.labelGraphDegree = QtWidgets.QLabel(self)
        self.labelGraphDegree.move(50,240)
        self.labelGraphDegree.setMaximumWidth(500)
        self.labelGraphDegree.setFixedWidth(500)
# (AC)(AD)(BC)(BD)
        self.show()

    def paintEvent(self, event):
        pen= QPen()
        pen.setWidth(5)
        painter = QPainter(self)
        painter.setPen(pen)
        painter.drawRect(50,300,700,450)
    
    def getGraphs(self):
        g = Graph()
        vertices = self.inputVertex.toPlainText().split(",")
        for vertex in vertices:
            g.addVertex(Vertex (vertex))
        edges = self.inputEdges.toPlainText()
        edgesSorted = re.findall(r'\(.*?\)', edges)
        for edge in edgesSorted:
            edge = edge.replace('(','')
            edge = edge.replace(')','')
            g.addEdge(edge[:1], edge[1:])
        g.printGraph()
        lowestDegree, lowestVertex = g.lowestDegree()
        sumDegree = g.sumDegree()
        graphDegree = g.graphDegree()
        self.labelLowestDegree.setText("El grado del vertice " + lowestVertex + " es el menor con un grado: " +str(lowestDegree))
        self.labelDegreeSum.setText("Suma de los grados: "+str(sumDegree))
        self.labelGraphDegree.setText("El grado del grafo: "+ str(graphDegree))


        
        
        
        

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