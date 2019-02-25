class LinkedList():
    
    head = None

    def insert(self, value):
        """
        a function to insert into the list
        """
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head

            while current._next:
                current = current._next
            current._next = Node(value)

    def append(self, insert_value):
        """
        a funciton to insert to the end of a list
        """
        current = self.head
        node = Node(insert_value)
        while current._next:
            current = current._next
        current._next = node

    def insert_before (self, given_value, insert_value):
        """
        a function in insert before any existing node
        """
        node = Node(insert_value)  
        if self.head.value == given_value:
            node._next = self.head
            self.head = node
        else:
            current = self.head 
            while current._next.value != given_value:
                current = current._next     
            node._next = current._next
            current._next = node

    def insert_after (self, given_value, insert_value):
        """
        a funcitioin to insert after any node
        """
        current = self.head
        node = Node(insert_value)
        while current.value != given_value:
            current = current._next
        node._next = current._next
        current._next = node    

    def includes(self, value):
        """
        a function to find if a value exists in the list
        """
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current._next    
        return False

    def print(self):
        """
        a print function to print out the complete list
        """
        if self.head:
            output = ''
            current = self.head
            while current:
                output += current.value + ','
                current = current._next

            return output  
        return -1
      
class Node():
    def __init__(self, value):
        self.value = value 
        self._next = None       