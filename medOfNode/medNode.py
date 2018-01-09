from makeGraph.creaGrafo import mkGraph

debug = False


def medNode(G, node):
    sonLevel = G.getAdjList(node.id)  # lista contenente i figli
    if (debug): print("figli nel primo passo:{}".format(sonLevel))
    count = 0
    while (len(sonLevel) >= 2):  # procedo finche almeno 2 rami del nodo origine hanno dei figli
        count += pathsCountLevel(sonLevel)  # ottengo le coppie per questo livello(
        if (debug): print("percorsi trovati:{}".format(count))
        sonNewLevel = []
        for branch in sonLevel:  # per ogni ramo(i discendenti dei primi figli)
            sonBranch = []
            if (debug): print("ramo analizzato:{}".format(branch))
            for n in branch:  # per ogni nodo dentro i rami
                if (debug): print("\tnodo analizzato:{}".format(n))
                sonBranch.extend(hisSon(G, n[1], n[0]))  # i figli dei nodi meno il loro padre
            if (len(sonBranch) != 0): sonNewLevel.append(sonBranch)
        if (debug): print("il nuovo livello che verrà aggiunto sarà:\n{}".format(sonNewLevel))
        if (debug): print(("dimensione livello:{}".format(len(sonNewLevel))))
        sonLevel = sonNewLevel
    if (debug): print("numero percorsi finali:{}".format(count))
    return count


def hisSon(G, nodeDadId, nodeId):
    """
    Funzione che ritorna tutti i filgli di un nodo sapendo chi era suo padre
    e quindi evitando di riprenderlo
    :param G: grafo
    :param nodeDad: padre del nodo di cui sapere figli
    :param node: nodo per i quali siamo interessati ad avere i figli
    :return: ramo, con dentro i nodi e loro padre: [[idNodi figli,idNodo padre],altri son....]  nella lista è escluso il padre
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
