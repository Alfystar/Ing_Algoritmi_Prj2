from random import randint as rInt

from graph.Graph_AdjacencyList import *
# from priorityQueue.PQbinomialHeap import PQbinomialHeap
from stack.Stack import PilaArrayList as stack


def mkGraph(mod, elem, son):
    """
    :param mod: modalita: "rand",
    :param elem: numero massimo di elementi da aggiungere
    :param son: numero di figli, nel caso random il massimo possibile
    :return: grafico sotto forma di lista di adiacenza
    """
    newGr = GraphAdjacencyList()
    firstNode = newGr.addNode(rInt(-10, 10))  # nodo con valore casuale
    sk = stack()
    sk.push(firstNode)
    sk.stampa()
    if mod=="rand":
        return randomGrap(newGr,sk,elem,son)


def randomGrap(G,pila,elemMax,sonMax):
    """
    :param G: grafo
    :param pila:
    :param elemMax:
    :param sonMax:
    :return:
    """
    count = 0
    while (count <= elemMax):
        node = pila.pop()  # prendo nodo già inserito
        for k in range(rInt(0, sonMax)):  # gli aggiungo un numero casuale di figli
            sonMax = G.addNode(rInt(-10, 10))
            notOriented(newGr, node, sonMax)
            pila.push(sonMax)
            count += 1  # tengo traccia dell'aumento dei nodi
    del pila  # cancello oggetto per far sovrascrivere memoria, la pila non è più necessaria
    return G



def notOriented(g,n1,n2):
    """
    :param g: grafo
    :param n1: nodo 1
    :param n2: nodo 2
    :return: null
    """
    g.insertEdge(n1.id, n2.id)
    g.insertEdge(n2.id, n1.id)


if __name__ == '__main__':
    mkGraph(0, 0)
