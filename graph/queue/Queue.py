from collections import deque
from list.LinkedList import ListaCollegata

class CodaListaCollegata(ListaCollegata):    
    """ Implementation of a FIFO queue using a linked list.
    """
    
    def enqueue(self, elem):
        self.addAsLast(elem)
    
    def dequeue(self):
        return self.popFirst()

class CodaArrayList():
    """ Implementation of a FIFO queue using a Python's list built-in type, i.e., lists based on array implementation.
    """
    
    def __init__(self):
        self.q = []
        
    def enqueue(self, elem):
        self.q.append(elem)
    
    def dequeue(self):
        if len(self.q) == 0:
            return None
        return self.q.pop(0)
    
    def getFirst(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[0]
    
    def isEmpty(self):
        return len(self.q) == 0
    
    def stampa(self):
        print("Elements in the collection (ordered):")
        print(self.q)

class CodaArrayList_deque(CodaArrayList):
    """ Faster implementation of a FIFO using the type deque, optimized also for removing elements at the beginning of the collection.
    """
    def __init__(self):
        self.q = deque()
    
    #Override
    def dequeue(self):
        if len(self.q) == 0:
            return None
        return self.q.popleft()

#global functions
def testQueue(q):
    for i in range(10):
        q.enqueue(i)
    q.stampa()
    
    print("First:", q.getFirst())
    print("Dequeue:", q.dequeue())
    print("First:", q.getFirst())
    print("Dequeue:", q.dequeue())
    print("First:", q.getFirst())
    
    q.stampa()

# Se eseguiamo direttamente questo modulo, ossia NON lo importiamo in un altro.
if __name__ == "__main__":
    print("CodaListaCollegata")
    q = CodaListaCollegata()
    testQueue(q)
    
    print("CodaArrayList")
    q = CodaArrayList()
    testQueue(q)
    
    print("CodaArrayList_deque")
    q = CodaArrayList_deque()
    testQueue(q)
