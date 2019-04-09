from stacks_and_queues import Queue
class Graph():

    def __init__(self):
        self._table ={}

    def add_vertex(self, value):
        """
        add value to graph
        """
        vertex = Vertex(value)
        self._table[value]= []

        return vertex

    def add_edge(self,item_1,item_2,weight=0):
        self._table[item_1.value].append((item_2.value, weight))
        self._table[item_2.value].append((item_1.value, weight))

    def get_nodes(self):
        print =[]
        for i in self._table.keys():  
            print.append(i)
        return print    
    def get_neighbors(self, item):
        print = []
        for i in self._table[item.value]:
            print.append(i)
        return print 
        
    def size(self):
        count = 0
        for i in self._table.keys():  
            count += 1
        if count == 0:
            return 'Empty'    
        return count
    def breadth_first(self, item,seen=None):
        if seen is None:
            seen = set()
        seen.add(item)
        for i in self._table[item] - seen:
            breadth_first(i, seen)
        return seen    

class Vertex():

    def __init__(self,value):
        self.value = value
