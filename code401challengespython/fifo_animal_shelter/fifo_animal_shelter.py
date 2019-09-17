class Queue():

    head = None
    tail = None

    def enqueue(self, val):
    
        new_animal = Node(val)

        if not self.head:
            self.head = new_animal
            self.tail = new_animal
        else:
            self.tail._next = new_animal
            self.tail = self.tail._next  
    def dequeue(self,pet):
        curr = self.head
        prev = None
        import pdb; pdb.set_trace()
        if curr.value['type'] == pet:
            temp = curr
            curr = curr._next
            return temp.value['name']
        
        while curr.value['type'] != pet:
            prev = curr
            curr = curr._next  

        temp = curr
        prev._next = curr._next
        curr = prev

        return temp.value['name']
  

class Node():
    def __init__(self, value):
        self.value = value 
        self._next = None         