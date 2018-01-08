import Sorting
import random
from time import time


def sortingTest(sortingFunc, inputList, secondPar = None, thirdPar = None):
    """
    Run the given sorting function on the given list.
    :param sortingFunc: the sorting function.
    :param inputList: the input list.
    :param secondPar: optional second parameter.
    :param thirdPar: optional third parameter.
    :return: the elapsed time.
    """
    l = list(inputList) # Copy the list.

    start = time()      # Record start time for elapsed time calculation.

    if secondPar != None and thirdPar != None: # Sorting needing 2nd and 3rd parameter
        sortingFunc(l, secondPar, thirdPar)
    elif secondPar != None: # Sorting needing the 2nd parameter
        sortingFunc(l, secondPar)
    else: # Sorting needing only the list
        sortingFunc(l)

    end = time() # Record end time for elapsed time calculation.

    return end - start


if __name__ == "__main__":
    inputType = 1              # 1 ascending, -1 descending, 0 random
    elems     = 5000           # number of elements
    inputList = [None] * elems # List initialization

    if inputType == 1:
        for i in range(0, elems): inputList[i] = i
    elif inputType == -1:
        for i in range(0, elems): inputList[i] = elems - i
    elif inputType == 0:
        for i in range(0, elems): inputList[i] = random.randint(0, elems)
    else:
        raise Exception("You used an invalid inputType parameter!")

    # SelectionSort
    runningTime = sortingTest(Sorting.selectionSort, inputList)
    print("selectionSort required {} seconds.".format(runningTime))

    # InsertionSortUp
    runningTime = sortingTest(Sorting.insertionSortUp, inputList)
    print("insertionSortUp required {} seconds.".format(runningTime))

    # InsertionSortDown
    runningTime = sortingTest(Sorting.insertionSortDown, inputList)
    print("insertionSortDown required {} seconds.".format(runningTime))

    # BubbleSort
    runningTime = sortingTest(Sorting.bubbleSort, inputList)
    print("bubbleSort required {} seconds.".format(runningTime))

    # quickSortIter (Deterministic)
    runningTime = sortingTest(Sorting.quickSortIter, inputList, True)
    print( "quickSortIter-Det required {} seconds.".format(runningTime))

    # quickSortIter (Non Deterministic)
    runningTime = sortingTest(Sorting.quickSortIter, inputList)
    print( "quickSortIter-NonDet required {} seconds.".format(runningTime) )

    # quickSort (Deterministic)
    runningTime = sortingTest(Sorting.quickSort, inputList, True)
    print( "quickSort(Rec)-Det required {} seconds.".format(runningTime))

    # quickSort (Non Deterministic)
    runningTime = sortingTest(Sorting.quickSort, inputList)
    print( "quickSort(Rec)-NonDet required {} seconds.".format(runningTime))

    # mergeSort
    runningTime = sortingTest(Sorting.mergeSort, inputList)
    print( "mergeSort required {} seconds.".format(runningTime))

    # heapSort
    runningTime = sortingTest(Sorting.heapSort, inputList)
    print( "heapSort required {} seconds.".format(runningTime))

    for base in [400, 100, 10, 2]:
        # radixSort (base: 400,100,10,2)
        runningTime = sortingTest(Sorting.radixSort, inputList, elems, base)
        print("radixSort({},{}) required {} seconds.".format(elems, base, runningTime))