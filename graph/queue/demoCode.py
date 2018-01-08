from Queue import CodaListaCollegata
from Queue import CodaArrayList
from Queue import CodaArrayList_deque

from time import time

#global functions
def enqueueTest(q,n=50000):
    start = time()
    for i in range(n):
        q.enqueue(i)
    elapsed = time() - start
    print("Required time:", elapsed, "seconds.")

def dequeueTest(q,n=50000):
    start = time()
    for i in range(n): #@UnusedVariable
        q.dequeue()
    elapsed = time() - start
    print("Required time:", elapsed, "seconds.")
    
# Se eseguiamo direttamente questo modulo, ossia NON lo importiamo in un altro.
if __name__ == "__main__":
    print("\tEnqueueing elements")
    print("CodaListaCollegata")
    ql=CodaListaCollegata()
    enqueueTest(ql)
    print("CodaArrayList")
    qal=CodaArrayList()
    enqueueTest(qal)
    print("CodaArrayList_deque")
    qald=CodaArrayList_deque()
    enqueueTest(qald)
    
    print("\tDequeueing elements")
    print("CodaListaCollegata")
    dequeueTest(ql)
    print("CodaArrayList")
    dequeueTest(qal)
    print("CodaArrayList_deque")
    dequeueTest(qald)
    