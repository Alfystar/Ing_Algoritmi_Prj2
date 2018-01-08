from stack.Stack import PilaArrayList as Stack
from queue.Queue import CodaArrayList_deque as Queue
from heap.HeapMax import HeapMax
import math
import random


def selectionSort(l):
    """
    Sort the given Python list in ascending order.
    The key idea is that at the k-th step, you put the the right element in position k.
    ----
    Time Complexity:  O(n^2), Omega(n^2)
    Space Complexity: O(1)
    :param l: the list to sort.
    :return: void.
    """
    for k in range(len(l) - 1):
        minPos = k
        for j in range(k + 1, len(l)):
            if l[j] < l[minPos]:
                minPos = j
        l[minPos], l[k] = l[k], l[minPos]   # Swapping, leveraging multiple assignment


def insertionSortDown(l):
    """
    Sort the given Python list in ascending order.
    Scan the list from the index k=1 to the end; assume the list is ordered before index k;
    at the k-th step, put the k-th element to the right position among the previous ones (from 0 to k-1).
    ----
    Time Complexity:  O(n^2), Omega(n)
    Space Complexity: O(1)
    :param l: the list to sort.
    :return: void.
    """
    for k in range(1, len(l)):
        if __debug__:
            print ("scanning position {}".format(k))

        val = l[k]
        for pos in range(k):
            if l[pos] > val:
                if __debug__:
                    print ("\t{}>{}".format(l[pos], val))
                break
        else:  #Entro in questo else, se nel for non ho trovato un elemento l[pos] che sia maggiore di val
            pos = k #This value for pos is just a flag to remember that from 0 to k, the list is already ordered
            if __debug__:
                print ("From 0 to {}, everything is already ordered.".format(k))

        if pos < k: #pos==k if no pos<k exists s.t. l[pos]>val. In this case, we have to do nothing, and continue from k+1.
            for j in range(k, pos, -1):
                l[j] = l[j - 1]
            l[pos] = val
            if __debug__:
                print ("Shift to right and set l[{}]={}: ".format(pos, l[pos]) + str(l[:k + 1]))


def insertionSortUp(l):
    """
    Sort the given Python list in ascending order.
    Like insertionSortDown, but processing elements from right to left.
    ----
    Time Complexity:  O(n^2), Omega(n)
    Space Complexity: O(1)
    :param l: the list to sort.
    :return: void.
    """
    for k in range(1, len(l)):
        if __debug__:
            print ("scanning position {}".format(k))

        val = l[k]
        for pos in range(k - 1, -1, -1):
            if __debug__:
                print ("pos=", pos)
            if l[pos] <= val:
                if __debug__:
                    print ("\t{}<={}".format(l[pos], val))
                break
        else:
            pos = -1  #Thus val is the minimum value in the first k positions.

        if pos < k - 1:
            for j in range(k, pos + 1, -1):
                l[j] = l[j - 1]
            l[pos + 1] = val
            if __debug__:
                print ("Shift to right and set l[{}]={}: ".format(pos + 1, l[pos + 1]) + str(l[:k + 1]))
        else:
            if __debug__:
                print ("From 0 to {}, everything is already ordered.".format(k))


def bubbleSort(l):
    """
    Iteratively process all the list, swapping elements in the wrong positions. 
    Once no swappings are necessary, the list is ordered.
    ----
    Time Complexity:  O(n^2), Omega(n)
    Space Complexity: O(1)
    :param l: the list to sort.
    :return: void.
    """
    swapped = True
    while swapped:
        swapped = False
        if __debug__:
            print (l)
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True
                if __debug__:
                    print ("Swap {} with {}".format(l[j + 1], l[j]))

##
# MergeSort
##
def mergeSort(l):
    """
    Sort the given Python list in ascending order.

    ----
    Time Complexity:  O(n*log(n)), Omega(n*log(n))
    Space Complexity: O(n)
    :param l: the list to sort.
    :return: void.
    """
    recursiveMergeSort(l, 0, len(l) - 1)


def recursiveMergeSort(l, left, right):
    """

    :param l: the list to sort.
    :param left: the left-most position.
    :param right: the right-most position.
    :return: void.
    """
    if __debug__:
        print ("recursiveMergeSort({},{})".format(left, right))

    if left >= right:
        return

    mid = int((left + right) / 2)
    if __debug__:
        print ("\tselected mid=", mid)

    recursiveMergeSort(l, left, mid)
    recursiveMergeSort(l, mid + 1, right)
    mergePartitions(l, left, mid, right)


def mergePartitions(l, left, mid, right):
    """

    :param l: the list to sort.
    :param left: the left-most position.
    :param mid: the middle position.
    :param right: the right-most position.
    :return: void.
    """
    if __debug__:
        print ("merge({},{},{})".format(left, mid, right))

    idLeft = left
    idRight = mid + 1
    tempList = []

    if __debug__:
        print ("\tleft:  {}\n\tright: {}\n\ttemp:  {}\n".format(str(l[idLeft:mid + 1]), str(l[idRight:right + 1]), str(tempList)))

    while True :
        if l[idLeft] < l[idRight]:
            tempList.append(l[idLeft])
            idLeft += 1
            if __debug__:
                print ("\tleft:  {}\n\tright: {}\n\ttemp:  {}\n".format(str(l[idLeft:mid + 1]), \
                                                        str(l[idRight:right + 1]), str(tempList)))

            if idLeft > mid: #first subsequence ended. Thus lets copy the remaining elements from the right partition.
                for v in l[idRight:right + 1]:
                    tempList.append(v)

                if __debug__:
                    print ("\tleft:  {}\n\tright: []\n\ttemp:  {}\n".format(str(l[idLeft:mid + 1]), str(tempList)))
                break #termitates the while loop
        else:   #Symmetric
            tempList.append(l[idRight])
            idRight += 1
            if __debug__:
                print ("\tleft:  {}\n\tright: {}\n\ttemp:  {}\n".format(str(l[idLeft:mid + 1]), str(l[idRight:right + 1]), str(tempList)))

            if idRight > right: #second subsequence ended. Thus lets copy the remaining elements from the left partition.
                for v in l[idLeft:mid + 1]:
                    tempList.append(v)

                if __debug__:
                    print ("\tleft:  []\n\tright: {}\n\ttemp:  {}\n".format(str(l[idRight:right + 1]), str(tempList)))
                break #termitates the while loop

    #Update the list with the computed ordered elements
    for i in range(left, right + 1):
        l[i] = tempList[i - left]

    if __debug__:
        print ("Updated list:", l[left:right + 1])
##
# End of MergeSort
##

##
# QuickSort - RECURSIVE, deterministic and non-deterministic
##
def quickSort(l, det = False):
    """
    Sort the given Python list in ascending order.

    ----
    Time Complexity:  O(n^2), Omega(n*log(n))
    Space Complexity: O(log(n))
    :param l: the list to sort.
    :param det: determinism.
    :return: void.
    """
    recursiveQuickSort(l, 0, len(l) - 1, det)

def recursiveQuickSort(l, left, right, det = False):
    """

    :param l: the list to sort.
    :param left: the left-most position.
    :param right: the right-most position.
    :param det: determinism.
    :return: void.
    """
    if __debug__:
        print ("recursiveQuickSort({},{})".format(left, right))

    if left >= right:
        return

    mid = partition(l, left, right, det)
    recursiveQuickSort(l, left, mid - 1, det)
    recursiveQuickSort(l, mid + 1, right, det)

    if __debug__:
        print ("- "*left + str(l[left:right + 1]) + " -"*(len(l) - right - 1))

def partition(l, left, right, det = False):
    """

    :param l: the list to sort.
    :param left: the left-most position.
    :param right: the right-most position.
    :param det: determinism.
    :return: void.
    """
    inf = left
    sup = right + 1

    if not det:
        mid = random.randint(left, right)
        l[left], l[mid] = l[mid], l[left] #scambio il perno con il primo elemento dell'intervallo considerato

    mid = left #If deterministic, it is set to the first element. Otherwise, since we swapped the randomically chosen median with the left element, we set mid to left.

    if __debug__:
        print ("Selected median:", l[mid])

    while True:
        inf += 1
        while inf <= right and l[inf] <= l[left]:
            inf += 1

        sup -= 1
        while l[sup] > l[left]:
            sup -= 1

        if inf < sup:
            l[inf], l[sup] = l[sup], l[inf]
        else:
            break

    l[left], l[sup] = l[sup], l[left]

    if __debug__:
        print ("- "*left + str(l[left:right + 1]) + " -"*(len(l) - right - 1))

    return sup
##
# End of QuickSort - RECURSIVE, deterministic and non-deterministic
##

##
# QuickSort - ITERATIVE, deterministic and non-deterministic
##
def quickSortIter(l, det = False):
    """
    Sort the given Python list in ascending order.

    ----
    Time Complexity:  O(n^2), Omega(n*log(n))
    Space Complexity: O(log(n))
    :param l: the list to sort.
    :param det: determinism.
    :return: void.
    """
    iterativeQuickSort(l, 0, len(l) - 1, det)

def iterativeQuickSort(l, left, right, det = False):
    """

    :param l: the list to sort.
    :param left: the left-most position.
    :param right: the right-most position.
    :param det: determinism.
    :return: void.
    """
    theStack = Stack()
    theStack.push(left)
    theStack.push(right)
    while not theStack.isEmpty():
        right = theStack.pop()
        left = theStack.pop()

        if __debug__:
            print ("quickSortIter-step({},{})".format(left, right))

        if right <= left:
            continue

        mid = partition(l, left, right, det)

        theStack.push(left)
        theStack.push(mid - 1)

        theStack.push(mid + 1)
        theStack.push(right)
##
# End of QuickSort - ITERATIVE, deterministic and non-deterministic
##

def heapSort(l):
    """
    L'heapSort segue la tecnica del selectionSort, ma utilizza una struttura dati piu' efficiente per l'estrazione del massimo: gli Heap.
    Si ricorda che un hep e' un albero binario che gode delle seguenti proprieta':
     - e' completo fino al penultimo livello
     - nei nodi dell'albero sono memorizzati gli elementi della collezione
     - chiave(padre(v)) > chiave(v) per ogni nodo v
    ----
    Time Complexity: O(n*log(n)), Omega(n*log(n)
    Space Complexity: O(1)
    """
    heap = HeapMax(l);

    if __debug__:
        print ("HEAPIFY")
    heap.heapify(); #costruisce l'heap
    if __debug__:
        print (heap.heap)

    if __debug__:
        print ("SORTING")
    while not heap.isEmpty():  #finchè l'heap non è vuoto cancella il massimo, ordinando così gli elementi in modo crescente
        if __debug__:
            print ("deleteMax()")
        heap.deleteMax() #ATTENZIONE: per come implementata la deleteMax, nessun elemento viene realmente cancellato dalla lista passata in
                        # argomento a HeapMax, ma spostato in fondo. Otteniamo un ordinamento crescente.
        if __debug__:
            print (heap.heap)

def radixSort(listOfIntegers, k, b):
    """
    Ordina interi da 1 a k usando bucket sort sulle cifre in base b
    Si ricorda che si fa uso della proprietà di stabilità del bucketsort nelle varie iterazioni!
    ----
    Time Complexity: O(n*k), O(n) se k=O(n^c) per c costante, Omega(n*k)
    Space Complexity: O(n+k)
    """
    cifrek = int(math.ceil(math.log(k + 1, b)))
    if __debug__:
        print ("radixSort(k={},b={}) cifrek={})".format(k, b, cifrek))

    for t in range(1, cifrek + 1):
        bucket = []
        for i in range(0, b): #@UnusedVariable
            bucket.append(Queue())
        for j in range(0, len(listOfIntegers)):
            cifratj = listOfIntegers[j] % math.pow(b, t) # leggiamo la t-esima cifra di A[j]
            cifratj = int(cifratj / math.pow(b, t - 1))
            bucket[cifratj].enqueue(listOfIntegers[j]) #aggiungiamo listOfIntegers[j] nel bucket corretto

        j = 0
        for e in bucket:
            while not e.isEmpty():
                listOfIntegers[j] = e.dequeue()
                j += 1
        if __debug__:
            print (listOfIntegers)


if __name__ == "__main__":
    l = [4, 1234, 34, 566, 8, 2, 5346, 8, 3, 263, 7, 8, 3, 7, 57, 2, 43, 87, 845, 42]
    print(l)

    selectionSort(l)
    #insertionSortUp(l)
    #bubbleSort(l)
    #mergeSort(l)
    #quickSort(l,True)
    #quickSort(l) #Random
    #quickSortIter(l, True)
    #quickSortIter(l) #Random
    #heapSort(l)
    #radixSort(l, 10000, 10)

    #output should be: 2,2,3,3,4,7,7,8,8,8,34,42,43,57,87,263,566,845,1234,5346]
    print(l)