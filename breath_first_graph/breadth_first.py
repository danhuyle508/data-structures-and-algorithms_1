from stacks_and_queues import Queue, Stack
class Graph():

    def __init__(self):
        self.graph = {}

    def add_vertex(self, value):
        """
        add value to graph
        """
        vertex = Vertex(value)
        self.graph[value]= vertex
        return vertex

    def add_edge(self,item_1,item_2,weight=0):
        item_1.list.append((item_2, weight))
        item_2.list.append((item_1, weight))

    def get_nodes(self):
        print =[]
        for i in self.graph.keys():  
            print.append(i)
        return print    
    def get_neighbors(self, item):
        print = []
        for i in self.graph[item.value]:
            print.append(i)
        return print 
        
    def size(self):

        count = 0
        for i in self.graph.keys():  
            count += 1
        if count == 0:
            return 'Empty'    
        return count

    def breadth_first(self, item):
        queue = Queue()
        queue.enqueue(item)
        seen =[]

        while queue.peek_queue():
            current = queue.dequeue()
            if current.visited == False:
                seen.append(current.value)
                current.visited = True
                for i in current.list:
                    if not i[0].visited:
                        queue.enqueue(i[0])
        return seen

    def depth_first(self,node):
        stack = Stack()
        stack.push(node)
        seen =[]
        while stack.peek_stack() is not None:
            current = stack.pop()
            if current.visited == False:
                seen.append(current.value)
                current.visited = True
                for i in current.list:
                    stack.push(i[0])
                if current.visited is False:
                    stack.pop()    
        return seen
class Vertex():

    def __init__(self,value):
        self.value = value
        self.list = []
        self.visited = False