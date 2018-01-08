from random import randint as rInt

from graph.Graph_AdjacencyList import *
# from priorityQueue.PQbinomialHeap import PQbinomialHeap
from stack.Stack import PilaArrayList as stack


def mkGraph(mod, elem):
    """
    :param mod: modalita: 0-> random
    :param elem: numero massimodi elementi da aggiungere
    :return: grafico sotto forma di lista di adiacenza
    """
    newGr = GraphAdjacencyList()
    firstNode = newGr.addNode(rInt(-10, 10))  # nodo con valore casuale
    sk = stack()
    sk.push(firstNode.id)
    sk.stampa()
    return newGr


if __name__ == '__main__':
    mkGraph(0, 0)
