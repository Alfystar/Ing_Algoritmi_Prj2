from medofGraph.medGraph import mostNodes
from makeGraph.creaGrafo import mkGraph
import sys

#@profile
def main ():
    cmd=sys.argv
    if(cmd[1]=="rand"):
        if(len(cmd)!=5):
            print("!!!!ERROR!!! correct sintax for RandomV1 is:\n<Modalità><OutputPrint 1/0><nElem><nMaxSon>")
            exit(-1)
        g = mkGraph(int(cmd[3]), "rand", int(cmd[4]))





    listaMedi=analisiGrafo(g)
    if(bool(int(cmq[1])))
    print("Nodi medi per piu' volte:")
    for elem in listaMedi:
        print("\tNodo {} medio per {} volte.".format(elem[0].id, elem[1]))
    del g

#@profile
def analisiGrafo(G):
    listaNodi = mostNodes(G)
    return listaNodi


if __name__ == '__main__':
    main()
