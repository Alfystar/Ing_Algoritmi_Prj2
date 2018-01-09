from makeGraph.creaGrafo import mkGraph

debug = False #debug è una variabile inizializzata a False per non far comparire tutti i print successivi


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
    count = 0

    #finchè almeno 2 rami del nodo d'origine hanno figli, conto le coppie possibili per questo livello
    while (len(sonLevel) >= 2):
        count += pathsCountLevel(sonLevel)
        if (debug): print("\tpercorsi trovati:{}".format(count))

        sonNewLevel = []
        for branch in sonLevel:  # per ogni ramo(quindi per il nuovo livello) creo una lista vuota
            sonBranch = []
            if (debug): print("\t\tramo analizzato:{}".format(branch))

            #per ogni nodo dentro i rami, metto nella lista i figli del nuovo livello, ed elimino il padre
            for n in branch:
                if (debug): print("\t\tnodo analizzato:{}".format(n))
                sonBranch.extend(hisSon(G, n[1], n[0]))

            # tengo solo le liste non vuote, cioè i figli del nuovo livello.
            #elimino i rami composti da foglie.
            if (len(sonBranch) != 0): sonNewLevel.append(sonBranch)
        if (debug): print("\til nuovo livello che verrà aggiunto sarà:\n{}".format(sonNewLevel))
        if (debug): print(("\tdimensione livello:{}".format(len(sonNewLevel))))

        sonLevel = sonNewLevel
    if (debug): print("numero percorsi finali:{}".format(count))
    return count


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
    funzione che calcola per un certo livello quanti cammini non doppi si possono fare
    che passano per il nodo originale NODE
    :param sonLevel: lista di lista dove ogni lista contiene ramo discendenti dei primi figli di NODE, NESSUNA LISTA VUOTA
    :return: numero di percorsi
    """
    if (debug): print("conta dei percorsi tra:{}".format(sonLevel))
    count = 0
    allNode = 0
    for branch in sonLevel:  # per ogni ramo
        if (debug): print("\tramo:{}".format(branch))
        allNode += len(branch)

    if (debug): print("\tnodi totali presenti:{}".format(allNode))

    for branch in sonLevel:
        if (debug): print("\tramo:{}".format(branch))
        count += len(branch) * (allNode - len(branch))
        allNode -= len(branch)
    if (debug): print("\tpercorsi contati:{}".format(count))
    return count


if __name__ == '__main__':
    if (debug): print("funzione per trovare quante volte il nodo n è medio in G")
    i = mkGraph(7, "fractal", 2)
    listNode = i.getNodes()
    i.print()
    print(
        "il nodo '{}' è medio {} volte di un percorsi minimi nel grafo".format(listNode[0].id, medNode(i, listNode[0])))
