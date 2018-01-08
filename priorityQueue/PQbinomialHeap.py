from list.LinkedList import ListaCollegata
from queue.Queue import CodaArrayList_deque as queue


class BinomialHeapNode:
    """Rappresenta un nodo di una BinomialHeap."""

    def __init__(self, e, k):
        self.elem = e
        self.key = k
        self.father = None
        self.sons = ListaCollegata()

    def swap(self, otherNode):
        """Scambia i valori di elem e key tra due nodi."""
        self.elem, otherNode.elem = otherNode.elem, self.elem
        self.key, otherNode.key = otherNode.key, self.key

    def addSon(self, son):
        """Aggiungi un figlio all'albero."""
        son.father = self
        self.sons.addAsLast(son)

class BinomialHeap:
    def __init__(self, e, k):
        self.root = BinomialHeapNode(e, k)

    def merge(self, otherHeap):
        """Unisci i due alberi sotto la radice di chiave minima."""
        thisRoot = self.root
        otherRoot = otherHeap.root

        if thisRoot.key <= otherRoot.key:
            otherRoot.father = thisRoot
            thisRoot.addSon(otherRoot)
            return self
        else:
            thisRoot.father = otherRoot
            otherRoot.addSon(thisRoot)
            return otherHeap

    def getHeapSons(self):
        """Ottieni la lista dei figli."""
        res = ListaCollegata()
        curr = self.root.sons.getFirstRecord()
        while curr != None:
            nHeap = BinomialHeap(None, None)
            nHeap.root = curr.elem
            nHeap.root.father = None
            res.addAsLast(nHeap)
            curr = curr.next
        return res

    def stampa(self):
        """BFS"""
        q = queue()
        #Attenzione verra' inserito 'None' come padre della radice.
        q.enqueue((None, self.root))
        while not q.isEmpty():
            father, curr = q.dequeue()
            print(father, '-->', curr.key)
            if not curr.sons.isEmpty():
                f = curr.sons.getFirstRecord()
                while f != None:
                    q.enqueue((curr.key, f.elem))
                    f = f.next


class PQbinomialHeap:
    """Implementa una coda con priorita' tramite binomial heap.

    Questa versione ha un limite di alberi fissato.
    """

    MAXSIZE = 32  #albero di dimensione maggiore sara' B31

    def __init__(self):
        self.heap = PQbinomialHeap.MAXSIZE * [None]
        for i in range(len(self.heap)):
            self.heap[i]=[None, None, None]  #TODO: perche' 3 alberi per lista?


    def rebuild(self):
        """Ristruttura la foresta di alberi binomiali.

        Verra' ripristinata la proprieta' di unicita'.
        """
        for i in range(len(self.heap)):
            if self.heap[i][1] == None and self.heap[i][2] == None:
                continue
            if self.heap[i][1] != None and self.heap[i][2] != None:
                # merge ultimi 2
                merged = self.heap[i][1].merge(self.heap[i][2])
                self.heap[i][1] = None
                self.heap[i][2] = None
            else:  # merge i (soli) primi due
                merged = self.heap[i][0].merge(self.heap[i][1])
                self.heap[i][0] = None
                self.heap[i][1] = None

            if self.heap[i + 1][0] == None:
                self.heap[i + 1][0] = merged
            elif self.heap[i + 1][1] == None:
                if i == len(self.heap) - 1:  #CONDIZIONE D'USCITA
                    raise MemoryError('Errore: e\' stato raggiunto il limite\
                        massimo di questa priority queue')
                self.heap[i + 1][1] = merged
            else:  #TODO: perche' non inserire la condizione d'uscita qui?
                self.heap[i + 1][2] = merged

    def isEmpty(self):
        for i in range(len(self.heap)):
            if self.heap[i][0] != None:
                return False
        return True

    def insert(self, e, k):
        """Aggiunge un B0, poi ristruttura."""
        nHeap = BinomialHeap(e, k)
        root = nHeap.root
        if self.heap[0][0] == None:
            self.heap[0][0] = nHeap
        else:
            self.heap[0][1] = nHeap
            self.rebuild()
        return root

    def findMinIndex(self):
        """Restituisce l'indice dell'heap la cui radice ha chiave minima."""
        minKeyIndex = -1  #valore di default per indicare errore
        if self.isEmpty():
            return minKeyIndex
        # Trova la posizione del primo heap non vuoto.
        startIndex = 0
        for i in range(PQbinomialHeap.MAXSIZE):
            if self.heap[i][0] != None:
                startIndex = minKeyIndex = i
                break
        # Trova l'indice del heap con radice a chiave minima.
        for i in range(startIndex + 1, PQbinomialHeap.MAXSIZE):
            if self.heap[i][0] != None and\
                self.heap[i][0].root.key < self.heap[minKeyIndex][0].root.key:
                    minKeyIndex = i
        return minKeyIndex

    def findMin(self):
        """Restituisce la radice dell'heap con chiave minima."""
        if self.isEmpty():
            return None
        return self.heap[self.findMinIndex()][0].root.elem

    def deleteMin(self):
        if self.isEmpty():
            return
        index = self.findMinIndex()
        nuovi = self.heap[index][0].getHeapSons()  # Prendi i figli del B-index
        # self.heap[index][0].stampa()
        self.heap[index][0] = None  # Taglia il B_index 
        count = 0
        curr = nuovi.getFirstRecord()  # Assumi che i figli siano heap B_0, ...
                                       # B_index-1 ordinati 
        while curr != None:
            # print(count,curr)
            if self.heap[count][0] == None:
                self.heap[count][0] = curr.elem
            else:
                self.heap[count][1] = curr.elem
            count += 1
            curr = curr.next

        self.rebuild()

    def stampa(self):
        for i in range(len(self.heap)):
            if self.heap[i][0] is not None:
                print("B_" + str(i))
                self.heap[i][0].stampa()


def main():
    pq = PQbinomialHeap()
    if pq.isEmpty():
        print("Empty queue")

    e = 4.0
    k = 2.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.stampa()
    print("findMin():", pq.findMin())

    e = 2.0
    k = 1.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.stampa()
    print("findMin():", pq.findMin())

    e = 8.0
    k = 4.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.stampa()
    print("findMin():", pq.findMin())

    e = 10.0
    k = 5.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.stampa()
    print("findMin():", pq.findMin())

    e = 6.0
    k = 3.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.stampa()
    print("findMin():", pq.findMin())

    print("deleteMin()")
    pq.deleteMin()
    pq.stampa()
    print("findMin():", pq.findMin())

    e = 12.0
    k = 6.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    e = 14.0
    k = 7.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    e = 16.0
    k = 8.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)

    print("deleteMin()")
    pq.deleteMin()
    pq.stampa()

    e = 4.0
    k = 2.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    e = 2.0
    k = 1.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.stampa()

if __name__ == "__main__":
    main()

