class LinkedList():
    
    head = None

    def insert(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head

            while current._next:
                current = current._next
            current._next = Node(value)

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current._next    
        return False

    def print(self):
        if self.head:
            output = ''
            current =self.head
            while current:
                output += current.value + ','
                current = current._next

            return output  
        return -1
      
class Node():
    def __init__(self, value):
        self.value = value 
        self._next = None       