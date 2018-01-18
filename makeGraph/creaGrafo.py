from random import randint as rInt

# from memory_profiler import profile
if __name__ == '__main__':
    from graph.Graph_AdjacencyList import *
    from stack.Stack import PilaArrayList as stack
    from queue.Queue import CodaArrayList_deque as queue
else:
    from graph.Graph_AdjacencyList import *
    from stack.Stack import PilaArrayList as stack
    from queue.Queue import CodaArrayList_deque as queue


def mkGraph(elem, mod="rand", son=5):
    """
    Chiama le funzioni che creano il grafo; di default mod="rand" e son=5.

    :param elem: numero massimo di elementi da aggiungere al grafo
    :param mod: modalità: "rand", "star", "linear", "fractal", "sfilacciatoRand", "sfilacciato"
    :param son: numero massimo di figli per nodo, al massimo per rand, fissato per fractal
    :return: grafico sotto forma di lista di adiacenza
    """
    newGr = GraphAdjacencyList()
    firstNode = newGr.addNode(rInt(-10, 10))  # nodo con valore casuale

    if mod == "asterisco":
        asterisk(newGr, firstNode, elem, son)

    if mod == "sfilacciatoRand":
        frayedThreadRand(newGr, firstNode, elem, son)

    if mod == "sfilacciato":
        frayedThread(newGr, firstNode, elem, son)

    if mod == "star":
        starGraph(newGr, firstNode, elem)

    if mod == "linear":
        linearGraph(newGr, firstNode, elem)

    if mod == "fractal":
        fractalGraph(newGr, firstNode, elem, son)

    if mod == "rand":
        randomGraph(newGr, elem)

    return newGr


def asterisk(G, fN, elemLimit, sonLimit):
    """
    Creazione di un grafico simile a lineare, ma a partire da un nodo centrale fa partire un numero sonLimit di rami,
    sempre con un numero globale di elemLimit nodi; la forma variera' tra linear (sL = 2) e star (sL = n-1); per
    questi casi, preferire gli algoritmi appositamente creati (meno istruzioni --> piu' rapidi).

    :param G: grafo contenente fN
    :param fN: è il fistNode creato in mkGraph
    :param elemLimit: numero massimo di elementi da aggiungere al grafo, è lo stesso di mkGraph
    :param sonLimit: numero rami dipanati dal nodo centrale, è lo stesso di mkGraph
    :return:
    """
    node = fN
    count = 1

    coda = queue()

    # abbozziamo i rami per definire la forma del grafo
    for k in range(sonLimit):
        if sonLimit <= (count - 1):
            print("ERROR: not enough elements chosen")
            return
        son = G.addNode(rInt(-10, 10))
        notOriented(G, node, son)
        coda.enqueue(son)
        count += 1

    # sviluppiamo i rami dei grafi
    while (count <= elemLimit - 1):
        if (not coda.isEmpty()):
            node = coda.dequeue()  # prendo nodo già inserito
        son = G.addNode(rInt(-10, 10))
        notOriented(G, node, son)
        coda.enqueue(son)
        count += 1  # tengo traccia dell'aumento dei nodi
    # del coda  # eliminiamo la coda


def frayedThread(G, fN, elemLimit, sonLimit):
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
    # pila = stack()
    # pila.push(fN)
    node = fN
    count = 1
    while (count <= elemLimit - 1):
        for k in range(sonLimit + 1):  # aggiungo un numero definito di figli foglia, e l'ultimo che sarà il nuovo nodo
            if (count > elemLimit - 1):
                break
            son = G.addNode(rInt(-10, 10))
            notOriented(G, node, son)
            count += 1
        node = son  # prendo l'ulimo nodo aggiunto e su di esso ripeto il procedimento


# @profile(precision=6)
def frayedThreadRand(G, fN, elemLimit, sonLimit):
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


# @profile(precision=6)
def starGraph(G, fN, elemLimit):
    """
    Genera tanti nodi che, con la funzione notOriented, saranno collegati a firstNode.

    :param G: grafo contenente fN
    :param fN: è il fistNode creato in mkGraph
    :param elemLimit: numero massimo di elementi da aggiungere al grafo, è lo stesso di mkGraph
    :return:
    """
    node = fN
    for k in range(elemLimit - 1):
        son = G.addNode(rInt(-10, 10))
        notOriented(G, node, son)


# @profile(precision=6)
def linearGraph(G, fN, elemLimit):
    """
    Genera un grafo lineare.

    :param G: grafo contenente fN
    :param fN: è il firstNode creato in mkGraph
    :param elemLimit: numero massimo di elementi da aggiungere al grafo, è lo stesso di mkGraph
    :return:
    """
    node = fN
    for k in range(elemLimit - 1):
        # prendo nodo già inserito
        son = G.addNode(rInt(-10, 10))
        notOriented(G, node, son)
        node = son


# @profile(precision=6)
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
    while (count <= elemLimit - 1):
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


# @profile(precision=6)
def randomGraph(G, elemLimit):
    """
    Genera un grafo in maniera random. Il comando "del l" finale serve a deallocare lo spazio precedentemente occupato
    dalla lista l.

    :param G: grafo contenente fN
    :param elemLimit: numero massimo di elementi da aggiungere al grafo, è lo stesso di mkGraph
    :return:
    """

    count = 1
    # oldNode = fN
    while (count <= elemLimit - 1):
        newNode = G.addNode(rInt(-10, 10))
        l = G.getNodes()
        oldNode = l[rInt(0, len(l) - 1)]
        while (oldNode == newNode):
            oldNode = l[rInt(0, len(l) - 1)]
        notOriented(G, newNode, oldNode)
        count += 1
    del l


def grafoEsempio():
    fig1 = GraphAdjacencyList()
    n0 = fig1.addNode(rInt(-10, 10))  # nodo con valore casuale
    n1 = fig1.addNode(rInt(-10, 10))  # nodo con valore casuale
    n2 = fig1.addNode(rInt(-10, 10))  # nodo con valore casuale
    n3 = fig1.addNode(rInt(-10, 10))  # nodo con valore casuale
    n4 = fig1.addNode(rInt(-10, 10))  # nodo con valore casuale
    n5 = fig1.addNode(rInt(-10, 10))  # nodo con valore casuale
    n6 = fig1.addNode(rInt(-10, 10))  # nodo con valore casuale
    n7 = fig1.addNode(rInt(-10, 10))  # nodo con valore casuale
    n8 = fig1.addNode(rInt(-10, 10))  # nodo con valore casuale
    n9 = fig1.addNode(rInt(-10, 10))  # nodo con valore casuale
    n10 = fig1.addNode(rInt(-10, 10))  # nodo con valore casuale
    notOriented(fig1, n8, n4)
    notOriented(fig1, n7, n4)
    notOriented(fig1, n9, n4)
    notOriented(fig1, n1, n4)
    notOriented(fig1, n5, n1)
    notOriented(fig1, n0, n1)
    notOriented(fig1, n0, n2)
    notOriented(fig1, n0, n3)
    notOriented(fig1, n6, n3)
    notOriented(fig1, n6, n10)
    return fig1

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
    print("\trandom")
    g1 = mkGraph(20, "rand", 5)
    g1.print()
    print("\n\tstar")
    g2 = mkGraph(20, "star")
    g2.print()
    print("\n\tlinear")
    g3 = mkGraph(20, "linear")
    g3.print()
    print("\n\tfractal")
    g4 = mkGraph(20, "fractal", 3)
    g4.print()
    print("\n\tsfilacciato Random")
    g5 = mkGraph(20, "sfilacciatoRand")
    g5.print()
    print("\n\tsfilacciato Deterministico")
    g6 = mkGraph(20, "sfilacciato", 3)
    g6.print()
    print("\n\tasterisco")
    g7 = mkGraph(20, "asterisco", 5)
    g7.print()
