from PyQt5 import QtGui
from Undirected_Graph import Vertex, Graph 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import re
import networkx as nx
import matplotlib.pyplot as plt

def drawGraph(vertices, edges, path):
    G=nx.Graph()
    G.add_nodes_from(vertices)
    G.add_edges_from(edges)
    print(G.nodes())
    color_map = []
    for node in G:
        if node in path:
            color_map.append('green')
        else:
            color_map.append('red')
    nx.draw(G,with_labels = True, node_color=color_map)    
    plt.savefig("path_graph1.png")
    plt.show()  



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

        self.show()
    
    


    def getGraphs(self):
        g = Graph()
        vertices = self.inputVertex.toPlainText().split(",")
        for vertex in vertices:
            g.addVertex(Vertex (vertex))
        edges = self.inputEdges.toPlainText()
        edgesSorted = re.findall(r'\(.*?\)', edges)
        i=0
        edgesDrawing = []
        for edge in edgesSorted:
            edge = edge.replace('(','')
            edge = edge.replace(')','')
            edgesSorted[i] = edge
            edgesDrawing.append((edge[:1], edge[1:]))
            g.addEdge(edge[:1], edge[1:])
        g.printGraph()
        lowestDegree, lowestVertex = g.lowestDegree()
        sumDegree = g.sumDegree()
        graphDegree = g.graphDegree()
        self.labelLowestDegree.setText("El grado del vertice " + lowestVertex + " es el menor con un grado: " +str(lowestDegree))
        self.labelDegreeSum.setText("Suma de los grados: "+str(sumDegree))
        self.labelGraphDegree.setText("El grado del grafo: "+ str(graphDegree))
        x = g.shortestPath('A','C')
        drawGraph(vertices,edgesDrawing,x)
        

App = QApplication(sys.argv)
window = Window()

sys.exit(App.exec())