from random import randint as rInt
#from memory_profiler import profile
if __name__ == '__main__':
    from graph.Graph_AdjacencyList import *
    from stack.Stack import PilaArrayList as stack
    from queue.Queue import CodaArrayList_deque as queue
else:
    from graph.Graph_AdjacencyList import *
    from stack.Stack import PilaArrayList as stack
    from queue.Queue import CodaArrayList_deque as queue


def mkGraph(elem, mod="rand", son = 5):
    """
    Chiama le funzioni che creano il grafo; di default mod="rand" e son=5.

    :param elem: numero massimo di elementi da aggiungere al grafo
    :param mod: modalità: "rand", "star", "linear", "fractal"
    :param son: numero massimo di figli per nodo, al massimo per rand, fissato per fractal
    :return: grafico sotto forma di lista di adiacenza
    """
    newGr = GraphAdjacencyList()
    firstNode = newGr.addNode(rInt(-10, 10))  #nodo con valore casuale

    if mod == "rand":
        randomGraph(newGr, firstNode, elem, son)

    elif mod == "star":
        starGraph(newGr, firstNode, elem)

    elif mod == "linear":
        linearGraph(newGr, firstNode, elem)

    elif mod == "fractal":
        fractalGraph(newGr, firstNode, elem, son)

    elif mod == "rand2":
        randomGraph2(newGr,elem)

    return newGr

#@profile(precision=6)
def randomGraph(G, fN, elemLimit, sonLimit):
    """
    Crea una pila che all'inizio contiene solo fN, e gli collega altri nodi in numero variabile. Questi saranno poi
    i punti di partenza per generarne altri, finchè non viene raggiunto elemLimit. Il comando "del pila" serve per
    deallocare lo spazio precedentemente occupato dalla pila.

    :param G: grafo contenente fN
    :param fN: è il fistNode creato in mkGraph
    :param elemLimit: numero massimo di elementi da aggiungere al grafo, è lo stesso di mkGraph
    :param sonLimit: numero massimo di figli per nodo, è lo stesso di mkGraph
    :return:
    """
    pila = stack()
    pila.push(fN)

    count = 1
    while (count <= elemLimit-1):
        if (not pila.isEmpty()):
            node = pila.pop()  # prendo nodo già inserito
        for k in range(rInt(0, sonLimit)):  # gli aggiungo un numero casuale di figli
            if (count > elemLimit-1):
                break
            son = G.addNode(rInt(-10, 10))
            notOriented(G, node, son)
            pila.push(son)
            count += 1  # tengo traccia dell'aumento dei nodi
    del pila  # eliminiamo la pila

#@profile(precision=6)
def starGraph(G, fN, elemLimit):
    """
    Genera tanti nodi che, con la funzione notOriented, saranno collegati a firstNode.

    :param G: grafo contenente fN
    :param fN: è il fistNode creato in mkGraph
    :param elemLimit: numero massimo di elementi da aggiungere al grafo, è lo stesso di mkGraph
    :return:
    """
    node = fN
    for k in range(elemLimit-1):
        son = G.addNode(rInt(-10, 10))
        notOriented(G, node, son)

#@profile(precision=6)
def linearGraph(G, fN, elemLimit):
    """
    Genera un grafo lineare.

    :param G: grafo contenente fN
    :param fN: è il firstNode creato in mkGraph
    :param elemLimit: numero massimo di elementi da aggiungere al grafo, è lo stesso di mkGraph
    :return:
    """
    node = fN
    for k in range(elemLimit-1):
         # prendo nodo già inserito
        son = G.addNode(rInt(-10, 10))
        notOriented(G, node, son)
        node = son

#@profile(precision=6)
def fractalGraph(G, fN, elemLimit, sonLimit):
    """
    Crea una coda che inizialmente contiene solo fN, e poi aggiunge i figli nel numero stabilito da sonLimit ad
    ogni nodo, come per un d-Heap. Se elemLimit-count (gli elementi rimanenti da inserire nel grafo) è minore di
    sonLimit, allora l'inserimento dei nodi nel grafo si ferma all'iterazione precedente.

    :param G: grafo contenente fN
    :param fN: è il firstNode creato in mkGraph
    :param elemLimit: numero massimo di elementi da aggiungere al grafo, è lo stesso di mkGraph
    :param sonLimit: numero massimo di figli per nodo, è lo stesso di mkGraph
    :return:
    """
    coda = queue()
    coda.enqueue(fN)

    count = 1
    while (count <= elemLimit-1): #and (elemLimit-count >= sonLimit):
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

#@profile(precision=6)
def randomGraph2(G,elemLimit):
    """
    Genera un grafo in maniera random. Il comando "del l" finale serve a deallocare lo spazio precedentemente occupato
    dalla lista l.

    :param G: grafo contenente fN
    :param elemLimit: numero massimo di elementi da aggiungere al grafo, è lo stesso di mkGraph
    :return:
    """

    count = 1
    #oldNode = fN
    while (count <= elemLimit - 1):
        newNode = G.addNode(rInt(-10, 10))
        l = G.getNodes()
        oldNode = l[rInt(0, len(l) - 1)]
        while (oldNode == newNode):
            oldNode = l[rInt(0, len(l) - 1)]
        notOriented(G, newNode, oldNode)
        count += 1
    del l

def notOriented(g, n1, n2):
    """
    Crea due archi per collegare n1 ed n2 tramite liste di adiacenza.

    :param g: grafo
    :param n1: nodo 1
    :param n2: nodo 2
    :return: null
    """
    g.insertEdge(n1.id, n2.id)
    g.insertEdge(n2.id, n1.id)

if __name__ == '__main__':
    print("random v1")
    g1 = mkGraph(20, "rand", 5)
    g1.print()
    print("star")
    g2 = mkGraph(20, "star")
    g2.print()
    print("linear")
    g3 = mkGraph(20, "linear")
    g3.print()
    print("fractal")
    g4 = mkGraph(20, "fractal", 3)
    g4.print()
    print("random v2")
    g5 = mkGraph(20, "rand2")
    g5.print()
