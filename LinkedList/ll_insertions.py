 class LinkedList()

    head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = head
            if head._next == None:
                head._next = value
            else:
                while current._next:
                    current = current._next
                current._next = value      
class Node():
    def __init__(self, value):
        self.value = value 
        self._next = None       