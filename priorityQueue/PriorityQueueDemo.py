#!/usr/bin/env python
#encoding: utf-8
from PQ_Dheap import PQ_DHeap
from PQbinaryHeap import PQbinaryHeap
from PQbinomialHeap import PQbinomialHeap
from time import time
from random import randrange
from random import random

def testPQ1(pqType, collection, d=None):
    """Definisce il test da svolgere sulle code con priorita'.

    Collection sara' una lista del tipo:[ (elem,key), ...].
    """
    if pqType == 'PQbinary':
        pq = PQbinaryHeap()
        print("Testing", pqType)
    elif pqType == 'PQbinomial':
        pq = PQbinomialHeap()
        print("Testing", pqType)
    elif pqType == 'PQ_Dheap' and d is not None:  #deve essere definito 'd'
        pq = PQ_DHeap(d)
        print("Testing", pqType, "with d=", d)
    else:
        return

    size = len(collection)
    start = time()
    for item in collection:
        pq.insert(item[0], item[1])
    elapsed = time() - start
    print ("\tTempo medio insert: \t\t\t\t%4.10f" % (elapsed / size))
    start = time()
    while not pq.isEmpty():
        pq.deleteMin()
    elapsed = time() - start
    print ("\tTempo medio deleteMin: \t\t\t\t%4.10f" % (elapsed / size))


if __name__ == "__main__":
    collSize = 2000
    rand = True  #abilito l'inserimento di valori presi in maniera random

    collection = []
    for i in range(collSize):
        if rand:
            k = randrange(0, collSize)
        else:
            k = i
        collection.append([2 * k, k])
    #Test per tutti i tipi di code con priorita' e varianti su D-heap
    testPQ1('PQbinary', collection)
    testPQ1('PQbinomial', collection)
    #testPQ1('PQ_Dheap', collection, 2)
    #testPQ1('PQ_Dheap', collection, 4)
    #testPQ1('PQ_Dheap', collection, 8)
    #testPQ1('PQ_Dheap', collection, 16)
    #testPQ1('PQ_Dheap', collection, 32)
    #testPQ1('PQ_Dheap', collection, 64)
