# coding: utf-8 

from HeapMax import HeapMax
from __init__ import printSwitch
from strutture.Stack import PilaArrayList as Stack  # Local renaming. Sometimes useful! :)
import math
import random
from strutture.Queue import CodaArrayList_deque as Queue


def selectionSort(l):
    """ It sorts the given Python list in ascending order.
        The key idea is that at the k-th step, you put the the right element in position k.
        O(n^2)
    """
    for k in range(len(l) - 1):

        min_pos = k
        for j in range(k + 1, len(l)):
            if l[j] < l[min_pos]:
                min_pos = j

        l[min_pos], l[k] = l[k], l[min_pos]  # multiple assignment to avoid tmp var


def insertionSortDown(l):
    """ It sorts the given Python list in ascending order.
           Scan the list from the index k=1 to the end; assume the list is ordered before index k;
           at the k-th step, put the k-th element to the right position among the previous ones (from 0 to k-1).
           O(n^2)
       """
    for k in range(1, len(l)):

        if printSwitch.dumpOperations:
            print("scanning position {}".format(k))

        val = l[k]
        for pos in range(k):
            if l[pos] > val:

                if printSwitch.dumpOperations:
                    print("\t{}>{}".format(l[pos], val))
                break

        else:  # if I don't find that l[pos] > val
            pos = k  # This value for pos is just a flag to remember that from 0 to k, the list is already ordered
            if printSwitch.dumpOperations:
                print("From 0 to {}, everything is already ordered.".format(k))

        if pos < k:  # pos==k if no pos<k exists s.t. l[pos]>val. Do nothing, and continue from k+1.
            for j in range(k, pos, -1):
                l[j] = l[j - 1]
            l[pos] = val
            if printSwitch.dumpOperations:
                print("Shift to right and set l[{}]={}: ".format(pos, l[pos]) + str(l[:k + 1]))


def insertionSortUp(l):
    """ It sorts the given Python list in ascending order.
        Like insertionSortDown, but processing elements from right to left.
        O(n^2)
    """
    for k in range(1, len(l)):
        if printSwitch.dumpOperations:
            print("scanning position {}".format(k))

        val = l[k]
        for pos in range(k - 1, -1, -1):

            if printSwitch.dumpOperations:
                print("pos=", pos)

            if l[pos] <= val:
                if printSwitch.dumpOperations:
                    print("\t{}<={}".format(l[pos], val))
                break
        else:
            pos = -1  # Thus val is the minimum value in the first k positions.

        if pos < k - 1:

            for j in range(k, pos + 1, -1):
                l[j] = l[j - 1]
            l[pos + 1] = val

            if printSwitch.dumpOperations:
                print("Shift to right and set l[{}]={}: ".format(pos + 1, l[pos + 1]) + str(l[:k + 1]))
        else:
            if printSwitch.dumpOperations:
                print("From 0 to {}, everything is already ordered.".format(k))

def bubbleSort(l):
    """ Iteratively process all the list, swapping elements in the wrong positions. Once no swappings are necessary, the list is ordered.
    O(n^2)
    """
    swapped = True
    while swapped:
        swapped = False

        if printSwitch.dumpOperations:
            print(l)

        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True

                if printSwitch.dumpOperations:
                    print("Swap {} with {}".format(l[j + 1], l[j]))


# MergeSort

def mergeSort(l):
    recursiveMergeSort(l, 0, len(l) - 1)


def recursiveMergeSort(l, left, right):
    if printSwitch.dumpOperations:
        print("recursiveMergeSort({},{})".format(left, right))

    if left >= right:
        return

    mid = int((left + right) / 2)

    if printSwitch.dumpOperations:
        print("\tselected mid=", mid)

    recursiveMergeSort(l, left, mid)
    recursiveMergeSort(l, mid + 1, right)
    mergePartitions(l, left, mid, right)


def mergePartitions(l, left, mid, right):
    if printSwitch.dumpOperations:
        print("merge({},{},{})".format(left, mid, right))

    idLeft = left
    idRight = mid + 1
    tempList = []

    if printSwitch.dumpOperations:
        print("\tleft:  {}\n\tright: {}\n\ttemp:  {}\n".format(str(l[idLeft:mid + 1]), str(l[idRight:right + 1]),
                                                               str(tempList)))

    while True:
        if l[idLeft] < l[idRight]:
            tempList.append(l[idLeft])
            idLeft += 1
            if printSwitch.dumpOperations:
                print("\tleft:  {}\n\tright: {}\n\ttemp:  {}\n".format(str(l[idLeft:mid + 1]), \
                                                                       str(l[idRight:right + 1]), str(tempList)))

            if idLeft > mid:  # first subsequence ended. Thus lets copy the remaining elements from the right partition.
                for v in l[idRight:right + 1]:
                    tempList.append(v)

                if printSwitch.dumpOperations:
                    print("\tleft:  {}\n\tright: []\n\ttemp:  {}\n".format(str(l[idLeft:mid + 1]), str(tempList)))
                break  # termitates the while loop

        else:  # Symmetric
            tempList.append(l[idRight])
            idRight += 1
            if printSwitch.dumpOperations:
                print(
                    "\tleft:  {}\n\tright: {}\n\ttemp:  {}\n".format(str(l[idLeft:mid + 1]), str(l[idRight:right + 1]),
                                                                     str(tempList)))

            if idRight > right:  # second subsequence ended. Thus lets copy the remaining elements from the left partition.
                for v in l[idLeft:mid + 1]:
                    tempList.append(v)

                if printSwitch.dumpOperations:
                    print("\tleft:  []\n\tright: {}\n\ttemp:  {}\n".format(str(l[idRight:right + 1]), str(tempList)))
                break  # termitates the while loop

    # Update the list with the computed ordered elements
    for i in range(left, right + 1):
        l[i] = tempList[i - left]

    if printSwitch.dumpOperations:
        print("Updated list:", l[left:right + 1])


# End of MergeSort

# QuickSort - RECURSIVE, deterministic and non-deterministic

def quickSort(l, det=False):
    recursiveQuickSort(l, 0, len(l) - 1, det)


def recursiveQuickSort(l, left, right, det=False):
    if printSwitch.dumpOperations:
        print("recursiveQuickSort({},{})".format(left, right))

    if left >= right:
        return

    mid = partition(l, left, right, det)
    recursiveQuickSort(l, left, mid - 1, det)
    recursiveQuickSort(l, mid + 1, right, det)

    if printSwitch.dumpOperations:
        print("- " * left + str(l[left:right + 1]) + " -" * (len(l) - right - 1))


def partition(l, left, right, det=False):
    inf = left
    sup = right + 1

    if not det:
        mid = random.randint(left, right)
        l[left], l[mid] = l[mid], l[left]  # exchange first elem with the randomically chosen one

    mid = left # the median is the first elem of the array

    if printSwitch.dumpOperations:
        print("Selected median:", l[mid])

    while True:
        inf += 1
        while inf <= right and l[inf] <= l[mid]:
            inf += 1

        sup -= 1
        while l[sup] > l[mid]:
            sup -= 1

        if inf < sup:
            l[inf], l[sup] = l[sup], l[inf]
        else:
            break

    l[mid], l[sup] = l[sup], l[mid]

    if printSwitch.dumpOperations:
        print("- " * left + str(l[left:right + 1]) + " -" * (len(l) - right - 1))

    return sup


# End of QuickSort - RECURSIVE, deterministic and non-deterministic

# QuickSort - ITERATIVE, deterministic and non-deterministic

def quickSortIter(l, det=False):
    iterativeQuickSort(l, 0, len(l) - 1, det)


def iterativeQuickSort(l, left, right, det=False):
    theStack = Stack()
    theStack.push(left)
    theStack.push(right)
    while not theStack.isEmpty():
        right = theStack.pop()
        left = theStack.pop()

        if printSwitch.dumpOperations:
            print("quickSortIter-step({},{})".format(left, right))

        if right <= left:
            continue

        mid = partition(l, left, right, det)

        theStack.push(left)
        theStack.push(mid - 1)

        theStack.push(mid + 1)
        theStack.push(right)


# End of QuickSort - ITERATIVE, deterministic and non-deterministic

def heapSort(l):
    """ L'heapSort segue la tecnica del selectionSort, ma utilizza una struttura dati piu' efficiente per l'estrazione del massimo: gli Heap.
        Si ricorda che un hep e' un albero binario che gode delle seguenti proprieta':
        - e' completo fino al penultimo livello
        - nei nodi dell'albero sono memorizzati gli elementi della collezione
        - chiave(padre(v)) > chiave(v) per ogni nodo v
    """
    heap = HeapMax(l);

    if printSwitch.dumpOperations:
        print("HEAPIFY")
    heap.heapify();  # costruisce l'heap
    if printSwitch.dumpOperations:
        print(heap.heap)

    if printSwitch.dumpOperations:
        print("SORTING")

    while not heap.isEmpty():  # finchè l'heap non è vuoto cancella il massimo, ordinando così gli elementi in modo crescente
        if printSwitch.dumpOperations:
            print("deleteMax()")
        heap.deleteMax()  # ATTENZIONE: per come implementata la deleteMax, nessun elemento viene realmente cancellato dalla lista passata in
        # argomento a HeapMax, ma spostato in fondo. Otteniamo un ordinamento crescente.
        if printSwitch.dumpOperations:
            print(heap.heap)


def radixSort(listOfIntegers, k, b):
    """ Ordina interi da 1 a k usando bucket sort sulle cifre in base b
        Si ricorda che si fa uso della proprieta' di stabilita del bucketsort nelle varie iterazioni!
        O(n) se k=O(n^c) per c costante.
    """
    cifrek = int(math.ceil(math.log(k + 1, b)))
    if printSwitch.dumpOperations:
        print("radixSort(k={},b={}) cifrek={})".format(k, b, cifrek))

    for t in range(1, cifrek + 1):
        bucket = []
        for i in range(0, b):  # @UnusedVariable
            bucket.append(Queue())

        for j in range(0, len(listOfIntegers)):
            cifratj = listOfIntegers[j] % math.pow(b, t)  # leggiamo la t-esima cifra di A[j]
            cifratj = int(cifratj / math.pow(b, t - 1))
            bucket[cifratj].enqueue(listOfIntegers[j])  # aggiungiamo listOfIntegers[j] nel bucket corretto

        j = 0
        for e in bucket:
            while not e.isEmpty():
                listOfIntegers[j] = e.dequeue()
                j += 1
        if printSwitch.dumpOperations:
            print(listOfIntegers)


if __name__ == "__main__":
    l = [4, 1234, 34, 566, 8, 2, 5346, 8, 3, 263, 7, 8, 3, 7, 57, 2, 43, 87, 845, 42]
    print(l)

    # selectionSort(l)
    # insertionSortDown(l)
    # bubbleSort(l)
    # mergeSort(l)
    # quickSort(l)
    # quickSort(l) #Random
    # quickSortIter(l, True)
    # quickSortIter(l) #Random
    heapSort(l)
    # radixSort(l, 10000, 10)

    # output should be: 2,2,3,3,4,7,7,8,8,8,34,42,43,57,87,263,566,845,1234,5346]
    print(l)
