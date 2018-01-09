from random import randint as rInt

from graph.Graph_AdjacencyList import *
from queue.Queue import CodaArrayList_deque as queue
# from priorityQueue.PQbinomialHeap import PQbinomialHeap
from stack.Stack import PilaArrayList as stack


def mkGraph(elem, mod="rand", son=None):
    """
    :param mod: modalita: "rand", "star", "linear", "fractal"
    :param elem: numero massimo di elementi da aggiungere
    :param son: numero di figli, nel caso random il massimo possibile
    :return: grafico sotto forma di lista di adiacenza
    """
    newGr = GraphAdjacencyList()
    firstNode = newGr.addNode(rInt(-10, 10))  # nodo con valore casuale

    if mod == "rand":
        randomGraph(newGr, firstNode, elem, son)

    elif mod == "star":
        starGraph(newGr, firstNode, elem)

    elif mod == "linear":
        linearGraph(newGr, firstNode, elem)

    elif mod == "fractal":
        fractalGraph(newGr, firstNode, elem, son)

    return newGr


def randomGraph(G, fN, elemLimit, sonLimit):
    """
    :param G: grafo
    :param fN: firstNode
    :param elemLimit:
    :param sonLimit:
    :return:
    """
    pila = stack()
    pila.push(fN)

    count = 1
    while (count <= elemLimit - 1):
        if (not pila.isEmpty()):
            node = pila.pop()  # prendo nodo già inserito
        for k in range(rInt(0, sonLimit)):  # gli aggiungo un numero casuale di figli
            if (count > elemLimit - 1):
                break
            son = G.addNode(rInt(-10, 10))
            notOriented(G, node, son)
            pila.push(son)
            count += 1  # tengo traccia dell'aumento dei nodi
    del pila  # eliminiamo la pila


def starGraph(G, fN, elemLimit):
    """
    :param G:
    :param fN: firstNode
    :param elemLimit:
    :return:
    """
    node = fN
    for k in range(elemLimit - 1):
        son = G.addNode(rInt(-10, 10))
        notOriented(G, node, son)


def linearGraph(G, fN, elemLimit):
    """
    :param G:
    :param fN: firstNode
    :param elemLimit:
    :return:
    """
    node = fN
    for k in range(elemLimit - 1):
        # prendo nodo già inserito
        son = G.addNode(rInt(-10, 10))
        notOriented(G, node, son)
        node = son


def fractalGraph(G, fN, elemLimit, sonLimit):
    """
    :param G: grafo
    :param fN: firstNode
    :param elemLimit:
    :param sonLimit:
    :return:
    """
    coda = queue()
    coda.enqueue(fN)

    count = 1
    while (count <= elemLimit - 1) and (elemLimit - count >= sonLimit):
        if (not coda.isEmpty()):
            node = coda.dequeue()  # prendo nodo già inserito
        for k in range(sonLimit):  # gli aggiungo un numero definito di figli
            if (count > elemLimit - 1):
                break
            son = G.addNode(rInt(-10, 10))
            notOriented(G, node, son)
            coda.enqueue(son)
            count += 1  # tengo traccia dell'aumento dei nodi
    del coda  # eliminiamo la coda


def notOriented(g, n1, n2):
    """
    :param g: grafo
    :param n1: nodo 1
    :param n2: nodo 2
    :return: null
    """
    g.insertEdge(n1.id, n2.id)
    g.insertEdge(n2.id, n1.id)


if __name__ == '__main__':
    g1 = mkGraph(20, "rand", 5)
    g1.print()
    print('')
    g2 = mkGraph(20, "star")
    g2.print()
    print('')
    g3 = mkGraph(20, "linear")
    g3.print()
    print('')
    g4 = mkGraph(22, "fractal", 3)
    g4.print()
