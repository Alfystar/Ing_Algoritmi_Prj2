import random
from graph.graph.Graph_AdjacencyList import *

def mkGraph(type, elem):
    newGr = GraphAdjacencyList()
    newGr.addNode(random.randint(-10,10))   #nodo con valore casuale
    return newGr