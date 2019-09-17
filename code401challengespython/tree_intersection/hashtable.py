from linked_list import LinkedList
class HashTable():

    def __init__(self):
        self.table = [None] * 1024

    def add(self,key,value):
        """
        add a key value pair to table
        """

        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = LinkedList()
        self.table[index].insert((key,value))

        return self.table[index].head.value[1]

    def hash(self, key):
        """
        takes in an arbitrary key and returns an index in the collection.
        """
        sum = 0
        acii_value = list(str(key))
        for i in range(len(acii_value)):
            sum += ord(acii_value[i])

        multiply_by_prime = sum * 199

        safe_index = multiply_by_prime // len(self.table)

        return safe_index

    def get(self, key):
        """
        get the value of a key value pair.
        """
        index =self.hash(key)
        if self.table[index] is None:
            return None
        current_node =self.table[index].head    
        while current_node:
            if current_node.value[0] == key:
                return current_node.value[1]
            else:
                current_node = current_node._next
        return  None          
    def contains(self, key):
        """
        find if a key exists in the hash table
        """
        index =self.hash(key)
        if self.table[index] is None:
            return False
        current_node =self.table[index].head    
        while current_node:
            if current_node.value[0] == key:
                return True
            else:
                current_node = current_node._next
        return  False