import cProfile
from medofGraph.medGraph import mostNodes
from makeGraph.creaGrafo import mkGraph

def main ():
    g = mkGraph(5000, "rand", 1000)
    #cProfile.run('analisiGrafo(g)','testPy')
    listaMedi=analisiGrafo(g)
    print("Nodi medi per piu' volte:")
    for elem in listaMedi:
        print("\tNodo {} medio per {} volte.".format(elem[0].id, elem[1]))


def analisiGrafo(G):
    listaNodi = mostNodes(G)
    return listaNodi


if __name__ == '__main__':
    main()