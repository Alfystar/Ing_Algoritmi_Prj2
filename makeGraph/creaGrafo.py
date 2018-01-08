from random import randint as rInt

from graph.Graph_AdjacencyList import *
# from priorityQueue.PQbinomialHeap import PQbinomialHeap
from stack.Stack import PilaArrayList as stack


def mkGraph(elem, son, mod="rand"):
    """
    :param mod: modalita: "rand", "star", "linear", "fractal"
    :param elem: numero massimo di elementi da aggiungere
    :param son: numero di figli, nel caso random il massimo possibile
    :return: grafico sotto forma di lista di adiacenza
    """
    newGr = GraphAdjacencyList()
    firstNode = newGr.addNode(rInt(-10, 10))  # nodo con valore casuale
    sk = stack()
    sk.push(firstNode)
    if mod == "rand":
        randomGraph(newGr, sk, elem, son)

    elif mod == "star":
        starGraph(newGr, sk, elem)

    elif mod == "linear":
        linearGraph(newGr, sk, elem)

    del sk  # eliminiamo la pila modificata in uno dei metodi
    return newGr


def randomGraph(G, pila, elemLimit, sonLimit):
    """
    :param G: grafo
    :param pila:
    :param elemLimit:
    :param sonLimit:
    :return:
    """
    count = 1
    while (count <= elemLimit-1):
        if (not pila.isEmpty()): node = pila.pop()  # prendo nodo già inserito
        for k in range(rInt(0, sonLimit)):  # gli aggiungo un numero casuale di figli
            son = G.addNode(rInt(-10, 10))
            notOriented(G, node, son)
            pila.push(son)
            count += 1  # tengo traccia dell'aumento dei nodi


def starGraph(G, pila, elemLimit):
    """
    :param G:
    :param pila:
    :param elemLimit:
    :return:
    """
    node = pila.pop()
    for k in range(elemLimit-1):
        son = G.addNode(rInt(-10, 10))
        notOriented(G, node, son)


def linearGraph(G, pila, elemLimit):
    """

    :param G:
    :param pila:
    :param elemLimit:
    :return:
    """
    count = 1
    while (count <= elemLimit-1):
        node = pila.pop()  # prendo nodo già inserito
        son = G.addNode(rInt(-10, 10))
        notOriented(G, node, son)
        pila.push(son)
        count += 1  # tengo traccia dell'aumento dei nodi

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
    i = mkGraph(10, 2, "rand")
    i.print()
    print('')
    j = mkGraph(10, 2, "star")
    j.print()
    print('')
    k = mkGraph(10, 2, "linear")
    k.print()
