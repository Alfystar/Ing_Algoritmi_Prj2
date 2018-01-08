#!/usr/bin/env python
# encoding: utf-8

class DHeapNode:
    """Singolo nodo di un DHeap."""

    def __init__(self, e, k, i):
        self.elem = e
        self.key = k
        self.index = i  # indice nella PQ: distanza dal nodo radice


class PQ_DHeap:
    """Coda con priorita' implementata tramite DHeap.

    Rappresentazione compatta: tutti i nodi verranno salvati in un'unica lista.
    I figli del nodo i-esimo hanno indice d*i + {1, 2, ... , d}.
    """

    def __init__(self, d):
        self.d = d
        self.heap = []                      # lista di DHeapNode
        self.length = 0

    def minSon(self, node):
        index = self.heap.index(node)
        minSon = None
        minKey = float('inf')               # qualsiasi elemento avra' valore inferiore
        for s in range(1, self.d + 1):      # iterazione sui figli del nodo
            sindex = self.d * index + s     # indice del figlio s-esimo
            if sindex > self.length - 1:    # fuori dal limite della lista
                break                       # return minSon
            son = self.heap[sindex]
            if son.key < minKey:
                minKey = son.key
                minSon = son
        return minSon

    def swap(self, node1, node2):
        self.heap[node1.index] = node2
        self.heap[node2.index] = node1
        node1.index, node2.index = node2.index, node1.index

    def moveUp(self, son):
        if son.index <= 0:
            return
        father = self.heap[(son.index - 1) // self.d]
        while son.index > 0 and son.key < father.key:
            self.swap(son, father)
            father = self.heap[(son.index - 1) // self.d]  # padre del padre

    def moveDown(self, father):
        son = self.minSon(father)
        while son != None and son.key < father.key:
            self.swap(father, son)
            son = self.minSon(father)  # figlio(minore) del figlio

    def isEmpty(self):
        if self.length == 0:
            return True
        return False

    def findMin(self):
        if self.isEmpty():
            return None
        return self.heap[0].elem

    def insert(self, e, k):
        n = DHeapNode(e, k, self.length)
        if self.length < len(self.heap):
            self.heap[self.length] = n
        else:
            self.heap.append(n)
        self.length += 1
        self.moveUp(n)
        return n

    def deleteMin(self):
        if self.length == 0:
            return
        first = self.heap[0]
        last = self.heap[self.length - 1]
        self.swap(first, last)
        self.length -= 1
        self.moveDown(last)  # last ha indice di first!
        # del self.heap[self.length]

    def decreaseKey(self, node, nKey):
        node.key = nKey
        self.moveUp(node)

    def stampa(self):
        s = ""
        for i in range(self.length):
            n = self.heap[i]
            s += "[{},{}] ".format(n.elem, n.key)
        print(s)


def main():
    pq = PQ_DHeap(4)
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
    pq.stampa()

    e = 14.0
    k = 7.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.stampa()

    e = 16.0
    k = 8.0
    print("insert({},{})".format(e, k))
    pq.insert(e, k)
    pq.stampa()

    print("deleteMin()")
    pq.deleteMin()
    pq.stampa()


if __name__ == "__main__":
    main()
