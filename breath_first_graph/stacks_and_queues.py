class Stack():

    head = None

    def push(self, val):
        new_node = Node(val)
        new_node._next = self.head
        self.head = new_node

    def peek_stack(self):
        if self.head:
            return self.head.value
        else:
            return 'No value.'    

    def pop(self):
        temp = self.head
        self.head = self.head._next    

class Queue():

    head = None
    tail = None

    def enqueue(self, val):
        
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail._next = new_node 
            self.tail = self.tail._next   

    def dequeue(self):
        if self.head:
            temp = self.head
            self.head = self.head._next
        else:
            'Empty Queue.'

    def peek_queue(self):
        if self.head:
            return self.head.value
        else:
            return 'No Value.'      

class Node():
    def __init__(self, value):
        self.value = value 
        self._next = None   