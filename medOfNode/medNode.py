from makeGraph.creaGrafo import mkGraph
from memory_profiler import profile

debug = False  # debug è una variabile inizializzata a False per non far comparire tutti i print successivi
#fp=open('memory_profiler.log','w+')

#@profile(stream=fp)
#@profile(precision=4)
def medNode(G, node):
    """
    Funzione che, dato un nodo, calcola per quante coppie esso è medio nel grafo cui appartiene.

    NB: Il numero di rami del primo livello non può mai aumentare, ma solo ridursi nei successivi passaggi.
    :param G: grafo
    :param node: nodo
    :return: numero di volte che node è medio in G

    """
    sonLevel = G.getAdjList(node.id)  # lista contenente i figli di un certo livello
    if (debug): print("figli nel primo passo:{}".format(sonLevel))
    medOfPaths = 0

    # finchè almeno 2 rami del nodo d'origine hanno figli, conto le coppie possibili per questo livello
    while (len(sonLevel) >= 2):
        medOfPaths += pathsCountLevel(sonLevel)
        if (debug): print("\tpercorsi trovati:{}".format(medOfPaths))

        sonNewLevel = []
        for branch in sonLevel:  # per ogni ramo(quindi per il nuovo livello) creo una lista vuota
            sonBranch = []
            if (debug): print("\t\tramo analizzato:{}".format(branch))

            # per ogni nodo dentro i rami, metto nella lista i figli del nuovo livello, ed elimino il padre
            for n in branch:
                if (debug): print("\t\tnodo analizzato:{}".format(n))
                sonBranch.extend(hisSon(G, n[1], n[0]))

            # tengo solo le liste non vuote, cioè i figli del nuovo livello.
            # elimino i rami composti da foglie.
            if (len(sonBranch) != 0): sonNewLevel.append(sonBranch)
            del sonBranch
        if (debug): print("\til nuovo livello che verrà aggiunto sarà:\n{}".format(sonNewLevel))
        if (debug): print(("\tdimensione livello:{}".format(len(sonNewLevel))))

        sonLevel = sonNewLevel
        del sonNewLevel
    if (debug): print("numero percorsi finali:{}".format(medOfPaths))
    return medOfPaths


def hisSon(G, nodeDadId, nodeId):
    """
    Funzione che ritorna tutti i figli di un nodo, sapendo chi era suo padre. In questo modo si evita di tornare sul
    nodo padre.

    :param G: grafo
    :param nodeDadId: padre del nodo di cui vogliamo conoscere i figli
    :param node: nodo di cui vogliamo conoscere i figli
    :return: una lista di liste di nodi appartenenti al livello successivo di nodeId, che conserva nodeId come padre:
            [[idNodi figli,idNodo padre],altri son....]  nella lista è escluso nodeDadId.
    """
    son = G.getAdj(nodeId, nodeDadId)
    return son


def pathsCountLevel(sonLevel):
    """
    Funzione che calcola i cammini possibili ad un certo livello che passano per il nodo originale NODE, moltiplicando
    la lunghezza delle sottoliste secondo la formula:
    len(ramo[k])*((somma di tutti i nodi di un livello)-len(ramo[k])).

    :param sonLevel: è un livello rappresentato con lista di liste, dove ogni lista contiene un ramo, e nessuna lista è vuota
    :return: cammini possibili al livello sonLevel
    """
    if (debug): print("conta dei percorsi tra:{}".format(sonLevel))
    path = 0
    allNode = 0

    # per ogni ramo conto il numero di nodi presenti in sonLevel; dunque ottengo il numero totale di nodi a quel livello
    for branch in sonLevel:
        if (debug): print("\tramo:{}".format(branch))
        allNode += len(branch)

    if (debug): print("\tnodi totali presenti:{}".format(allNode))

    # applico la formula per calcolare i cammini possibili al livello sonLevel
    for branch in sonLevel:
        if (debug): print("\tramo:{}".format(branch))
        path += len(branch) * (allNode - len(branch))
        allNode -= len(branch)
    if (debug): print("\tpercorsi contati:{}".format(path))

    return path


if __name__ == '__main__':
    if (debug): print("funzione per trovare quante volte il nodo n è medio in G")
    i = mkGraph(5000, "rand", 10)
    listNode = i.getNodes()
    i.print()
    print(
        "il nodo '{}' è medio {} volte di un percorsi minimi nel grafo".format(listNode[0].id, medNode(i, listNode[0])))
