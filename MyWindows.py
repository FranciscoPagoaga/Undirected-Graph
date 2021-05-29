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

edgesPath = ""
verticesPath = ""


def drawGraph(vertices, edges):
    G = nx.Graph()
    plt.close()
    G.add_nodes_from(vertices)
    G.add_edges_from(edges)
    nx.draw(G,with_labels = True)    
    plt.savefig("path_graph1.png")
    plt.show()  

def drawPath(path=[]):
    G = nx.Graph()
    G.add_nodes_from(verticesPath)
    G.add_edges_from(edgesPath)
    plt.close()
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


        self.labelPath = QtWidgets.QLabel(self)
        self.labelPath.setText("Enter Path:")
        self.labelPath.move(50,280)
        self.labelPath.setVisible(False)

        self.inputPath = QtWidgets.QTextEdit(self)
        self.inputPath.setPlaceholderText("Ex: A,B")
        self.inputPath.setMaximumWidth(500)
        self.inputPath.setFixedWidth(500)
        self.inputPath.move(50,310)
        self.inputPath.setVisible(False)

        self.submitPath = QtWidgets.QPushButton(self)
        self.submitPath.setText("Get Path")
        self.submitPath.setMaximumWidth(200)
        self.submitPath.setFixedWidth(190)
        self.submitPath.move(50,350)
        self.submitPath.setVisible(False)
        self.submitPath.clicked.connect(self.getPath)

        self.show()
    
    


    def getGraphs(self):
        vertices = self.inputVertex.toPlainText().split(",")
        for vertex in vertices:
            g.addVertex(Vertex (vertex))
        edges = self.inputEdges.toPlainText()
        edgesSorted = re.findall(r'\(.*?\)', edges)
        edgesDrawing = []
        isValid = True
        for edge in edgesSorted:
            edge = edge.replace('(','')
            edge = edge.replace(')','')
            if(edge[:1] in vertices and edge[1:] in vertices):
                edgesDrawing.append((edge[:1], edge[1:]))
                g.addEdge(edge[:1], edge[1:])
            else:
                isValid = False
        if(isValid):
            lowestDegree, lowestVertex = g.lowestDegree()
            sumDegree = g.sumDegree()
            graphDegree = g.graphDegree()
            drawGraph(vertices,edgesDrawing)
            global edgesPath
            edgesPath = edgesDrawing
            global verticesPath 
            verticesPath = vertices
            self.labelLowestDegree.setText("El grado del vertice " + lowestVertex + " es el menor con un grado: " +str(lowestDegree))
            self.labelDegreeSum.setText("Suma de los grados: "+str(sumDegree))
            self.labelGraphDegree.setText("El grado del grafo: "+ str(graphDegree))
            g.printGraph()
            self.labelPath.setVisible(True)
            self.inputPath.setVisible(True)
            self.submitPath.setVisible(True)
            

    
    def getPath(self):
        input = self.inputPath.toPlainText().split(",")
        if(len(input)==2):
            path = g.shortestPath(input[0],input[1])
            drawPath(path)              
          

if __name__ == '__main__':
    G=nx.Graph()
    g = Graph()
    
    App = QApplication(sys.argv)
    window = Window()

    sys.exit(App.exec())