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

    def merge(self, list_2):
        
        curr_1 = self.head
        curr_2 = list_2.head
        new_head = curr_1

        while curr_1._next or curr_2._next:
            temp_1 = curr_1._next
            temp_2 = curr_2._next
            curr_1._next = curr_2
            new_head._next = curr_1
            curr_1 = temp_1
            curr_2 = temp_2         

        return new_head

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

