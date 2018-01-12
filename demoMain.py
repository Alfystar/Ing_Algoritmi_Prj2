from medofGraph.medGraph import mostNodes
from makeGraph.creaGrafo import mkGraph
import sys
import time
#from memory_profiler import profile

#@profile(precision=8)
def main ():
    cmd=sys.argv
    if(len(cmd)==1):
        helpPrint()
        exit(-1)
    if (cmd[1] == "h" or cmd[1]=="help"):
        helpPrint()
        exit(-1)
    if (cmd[1] == "rand"):
        if (len(cmd) < 5):
            print("!!!!ERROR!!! correct sintax for RandomV1 is:\n<Modalità><OutputPrint 1/0><nElem><nMaxSon>")
            exit(-1)
        g = mkGraph(int(cmd[3]), "rand", int(cmd[4]))
    if (cmd[1] == "fractal"):
        if (len(cmd) < 5):
            print("!!!!ERROR!!! correct sintax for Fractal is:\n<Modalità><OutputPrint 1/0><nElem><d-son>")
            print("\nLa corretta sintassi è:")
            helpPrint()
            exit(-1)
        g = mkGraph(int(cmd[3]), "fractal", int(cmd[4]))
    if (cmd[1] == "star"):
        if (len(cmd) < 4):
            print("!!!!ERROR!!! correct sintax for Star is:\n<Modalità><OutputPrint 1/0><nElem>")
            exit(-1)
        g = mkGraph(int(cmd[3]), "star")
    if (cmd[1] == "linear"):
        if (len(cmd) < 4):
            print("!!!!ERROR!!! correct sintax for Linear is:\n<Modalità><OutputPrint 1/0><nElem>")
            exit(-1)
        g = mkGraph(int(cmd[3]), "linear")
    if (cmd[1] == "rand2"):
        if (len(cmd) < 4):
            print("!!!!ERROR!!! correct sintax for RandomV2 is:\n<Modalità><OutputPrint 1/0><nElem>")
            exit(-1)
        g = mkGraph(int(cmd[3]), "rand2")

    t=time.time()
    listaMedi=mostNodes(g)
    elapsed=time.time()-t
    if(bool(int(cmd[2]))):
        print("Nella forma {} i nodi medi di più percorsi sono:".format(cmd[1]))
        for elem in listaMedi:
            print("\tNodo {} medio per {} volte.".format(elem[0].id, elem[1]))
    del g
    print("{},{}".format(int(cmd[3]),elapsed))  #output per creare grafici

def helpPrint():
    print("Le possibili modalità di uso sono:")
    print(("Filo Sfilacciato:\t\t\trand <OutputPrint 1/0> <nElem> <nMaxSon>"))
    print(("Lineare:\t\t\t\tlinear <OutputPrint 1/0> <nElem> "))
    print(("Frattale o D-heap:\t\t\tfractal <OutputPrint 1/0> <nElem> <d-son>"))
    print(("Stella:\t\t\t\t\tstar <OutputPrint 1/0> <nElem>"))
    print(("Random Puro:\t\t\t\trand2 <OutputPrint 1/0> <nElem>"))
    print("\n\nIn caso di dubbi chiamare la funzione senza parametri, o con h, o con help")


if __name__ == '__main__':
    main()
