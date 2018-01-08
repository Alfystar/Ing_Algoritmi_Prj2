class Pila:
    """ Not strictly necessary. It is just an example to show how you could simulate interfaces behavior in Python (and related stuff!).
    """
    def push(self,elem):
        raise NotImplementedError("You should have implemented this method!")
    def pop(self):
        raise NotImplementedError("You should have implemented this method!")
    def top(self):
        raise NotImplementedError("You should have implemented this method!")
    def isEmpty(self):
        raise NotImplementedError("You should have implemented this method!")

#pila implementata tramite una lista built-in.
class PilaArrayList(Pila):
    
    def __init__(self):
        self.s = []
    #Override
    def push(self, elem):
        self.s.append(elem)
    #Override
    def pop(self):
        if len(self.s) == 0:
            return None
        return self.s.pop()
    #Override
    def top(self):
        if len(self.s) == 0:
            return None
        return self.s[-1]
    #Override
    def isEmpty(self):
        return len(self.s) == 0

    def stampa(self):
        print("Elements in the collection (ordered):")
        print(self.s)