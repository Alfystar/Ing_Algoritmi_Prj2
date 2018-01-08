class Record:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

    def __str__(self):
        return self.elem


class ListaCollegata:
    
    def __init__(self):
        self.first = None
        self.last = None
        
    def isEmpty(self):
        return self.first is None
    
    def getFirst(self):
        return None if self.first is None else self.first.elem

    def getLast(self):
        return None if self.last is None else self.last.elem
        
    def addAsLast(self, elem):
        rec = Record(elem)
        if self.first is None:
            self.first = self.last = rec
        else:
            self.last.next = rec
            self.last = rec

    def addAsFirst(self, elem):
        rec = Record(elem)
        if self.first is None:
            self.first = self.last = rec
        else:
            rec.next = self.first
            self.first = rec
    
    def popFirst(self):
        if self.first is None:
            return None
        else:
            res = self.first.elem
            self.first = self.first.next
            if self.first is None:
                self.last = None
            return res

    def getFirstRecord(self):
        return self.first

    def getLastRecord(self):
        return self.last

    def __len__(self):
        size = 0
        curr = self.first
        while curr is not None:
            size += 1
            curr = curr.next
        return size
        
    def __str__(self):
        s = "["
        current = self.first
        while current is not None:
            if len(s) > 1:
                s += ", "
            s += str(current.elem)
            current = current.next
        s += "]"
        return s


if __name__=="__main__":
    l = ListaCollegata()
    print(l)
    
    print("addAsFirst(2)")
    l.addAsFirst(2)
    print("addAsFirst(3)")
    l.addAsFirst(3)
    print("addAsLast(4)")
    l.addAsLast(4)    
    print(l)
    print(len(l))
    
    print("getFirst():", l.getFirst())

    print("getLast():", l.getLast())

    print("popFirst():", l.popFirst())
    print(l)
