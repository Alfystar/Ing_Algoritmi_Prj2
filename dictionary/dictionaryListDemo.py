from dictionaryOrderedArrayList import DictionaryOrderedArrayList
from dictionaryUnorderedLinkedList import DictionaryUnorderedLinkedList
from time import time


def test(steps):
    dict1 = DictionaryOrderedArrayList()
    dict2 = DictionaryUnorderedLinkedList()
    
    print("Test di DictionaryOrderedArrayList (tempo medio per ogni operazione, calcolato su {} chiamate):\n".format(steps))
    
    start = time()
    for i in range(steps):
        dict1.insert(2 * i, i)
    elapsed = time() - start
    print("Tempo medio insert:", elapsed / steps)
    
    start = time()
    for i in range(steps):
        dict1.binarySearch(2 * i)
    elapsed = time() - start
    print("Tempo medio search a buon fine:", elapsed / steps)
    
    start = time()
    for i in range(steps):
        dict1.binarySearch(2 * i + 1)
    elapsed = time() - start
    print("Tempo medio search di elementi non presenti:", elapsed / steps)
    
    start = time()
    for i in range(steps):
        dict1.delete(2 * i)
    elapsed = time() - start
    print("Tempo medio delete:", elapsed / steps)
    

    print("\nTest di DictionaryUnorderedLinkedList (tempo medio per ogni operazione, calcolato su {} chiamate):\n".format(steps))
    
    start = time()
    for i in range(steps):
        dict2.insert(2 * i, i)
    elapsed = time() - start
    print("Tempo medio insert:", elapsed / steps)
    
    start = time()
    for i in range(steps):
        dict2.search(2 * i)
    elapsed = time() - start
    print("Tempo medio search a buon fine:", elapsed / steps)
    
    start = time()
    for i in range(steps):
        dict2.search(2 * i + 1)
    elapsed = time() - start
    print("Tempo medio search di elementi non presenti:", elapsed / steps)
    
    start = time()
    for i in range(steps):
        dict2.delete(2 * i)
    elapsed = time() - start
    print("Tempo medio delete:", elapsed / steps)

if __name__ == "__main__":
    test(2000)
