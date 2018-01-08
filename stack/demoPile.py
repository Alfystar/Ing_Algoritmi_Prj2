from Stack import PilaListaCollegata
from Stack import PilaArrayList_dummy
from Stack import PilaArrayList

from time import time

#global functions
def pushTest(s,n=50000):
    start = time()
    for i in range(n):
        s.push(i)
    elapsed = time() - start
    print("Required time:", elapsed, "seconds.")

def popTest(s,n=50000):
    start = time()
    for i in range(n): #@UnusedVariable
        s.pop()
    elapsed = time() - start
    print("Required time:", elapsed, "seconds.")
    
# Se eseguiamo direttamente questo modulo, ossia NON lo importiamo in un altro.
if __name__ == "__main__":
    print("\tPushing elements")
    print("PilaListaCollegata")
    sl=PilaListaCollegata()
    pushTest(sl)
    print("PilaArrayList_dummy")
    sald=PilaArrayList_dummy()
    pushTest(sald)
    print("PilaArrayList")
    sal=PilaArrayList()
    pushTest(sal)
    
    print("\tPopping elements")
    print("PilaListaCollegata")
    popTest(sl)
    print("PilaArrayList_dummy")
    popTest(sald)
    print("PilaArrayList")
    popTest(sal)
    