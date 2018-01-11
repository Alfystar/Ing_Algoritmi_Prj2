from medofGraph.medGraph import mostNodes
from makeGraph.creaGrafo import mkGraph
from memory_profiler import profile
import time

debug=True

@profile(precision=20)
def filoSfilacciato(elem,son):
    g = mkGraph(elem, "rand", son)
    listaMedi = mostNodes(g)
    if (debug):
        print("Nodi medi per piu' volte:")
        for elem in listaMedi:
            print("\tNodo {} medio per {} volte.".format(elem[0].id, elem[1]))


@profile(precision=20)
def frattale(elem,son):
    g = mkGraph(elem, "fractal", son)
    listaMedi = mostNodes(g)
    if (debug):
        print("Nodi medi per piu' volte:")
        for elem in listaMedi:
            print("\tNodo {} medio per {} volte.".format(elem[0].id, elem[1]))


if __name__ == '__main__':
    filoSfilacciato(500,5)
    time.sleep(0.1)
    frattale(1500,5)
    time.sleep(0.1)