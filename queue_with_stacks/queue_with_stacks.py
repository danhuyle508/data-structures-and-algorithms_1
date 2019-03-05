class Stack():

    head = None

    def push(self, val):
        new_node = Node(val)
        new_node._next = self.head
        self.head = new_node

    def peek_stack(self):
        if self.head == None:
            return False
        else:    
            return self.head.value

    def pop(self):   
        temp = self.head
        self.head = self.head._next    
        return self.head

class Queue():
    stack_1 = Stack()
    stack_2 = Stack()

    def enqueue(self, val):
        self.stack_1.push(val)

    def dequeue(self):
        if not self.stack_2.peek_stack():
            while self.stack_1.peek_stack():
                data = self.stack_1.head.value
                self.stack_1.pop()
                self.stack_2.push(data)
            self.stack_2.pop()
            return self.stack_2.head.value                
        else:
            while self.stack_2.peek_stack():
                data = self.stack_2.head.value
                self.stack_2.pop()
                self.stack_1.push(data) 
                       
            self.stack_1.pop()
            return self.stack_1.head.value

    def show(self):
        if self.stack_2.head == None: 
            return self.stack_1.head.value
        if self.stack_1.head == None:
            return self.stack_2.head.value

class Node():
    def __init__(self, value):
        self.value = value 
        self._next = None       