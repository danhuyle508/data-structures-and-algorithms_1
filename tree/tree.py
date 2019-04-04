class BinaryTree(object):
    def __init__(self):
        self.root = None

    def inorder(self, current_node):
        """
        returns a list of nodes in order left,node,right
        """
        tree_list =[]
        if current_node.left:
            tree_list += self.inorder(current_node.left)
        tree_list.append(current_node.value)     
        if current_node.right:
            tree_list += self.inorder(current_node.right)
            
        return tree_list  

    def postorder(self, current_node):
        """
        returns a list of nodes in order left, right, node
        """
        tree_list =[]
        if current_node.left:
            tree_list += self.inorder(current_node.left)   
        if current_node.right:
            tree_list += self.inorder(current_node.right)
        tree_list.append(current_node.value)      
        return tree_list  
        
    def preorder(self, current_node):
        """
        returns a list of nodes in order node,left,right
        """
        tree_list =[]
        tree_list.append(current_node.value)  
        if current_node.left:
            tree_list += self.preorder(current_node.left)   
        if current_node.right:
            tree_list += self.preorder(current_node.right)
        return tree_list      

class Queue():

    head = None
    tail = None

    def enqueue(self, val):
        
        new_node = QNode(val)

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
            return temp.value
        else:
            None

    def peek_queue(self):
        if self.head:
            return self.head.value
        else:
            return None                     

class QNode():
    def __init__(self, value):
        self.value = value 
        self._next = None  


class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None

    def add(self,value):
        """
        add a root to the tree
        """
        if not self.root:
            self.root = Node(value)
        else:
            self.add_child(value,self.root)

    def add_child(self, value,current):
        """
        adds a child to the tree  
        """
        if value > current.value:
            if not current.right:
                current.right = Node(value)
            else:
                self.add_child(value, current.right)
        elif value < current.value:
            if not current.left:
                current.left = Node(value)
            else:
                self.add_child(value, current.left)

    def contains(self, value, current = None):
        """
        search for a value
        """
        if not current:
            current = self.root 
        if current.value == value:
            return True   
        if not self.root:
            return False    
        elif value < current.value:
            if current.left:
                return self.contains(value,current.left)
            else:
                return False
        elif value > current.value:
            if current.right:
                return self.contains(value,current.right)
            else: 
                return False   
    def find_maximum_value(self, current_node):
        """
        get the maximun value
        """
        max = 0
        tree_array = self.preorder(current_node)  
        print(tree_array)    
        for i in range(len(tree_array)):
            if tree_array[i] > max:
                max = tree_array[i]
        return max        

    def breadth_first_traversal(self,current_node):
        """
        a method that traverses in the breadth first approach
        """
        print_list =[]
        queue = Queue()
        queue.enqueue(current_node)
        print_list.append(current_node.value)
        while queue.peek_queue():
            # import pdb; pdb.set_trace()
            current_node = queue.dequeue()
            if current_node:
                print(current_node.value)

                if current_node.left:
                    queue.enqueue(current_node.left)
                    print_list.append(current_node.left.value)
                if current_node.right:
                    queue.enqueue(current_node.right)
                    print_list.append(current_node.right.value)
        return print_list

    def traverse_breath_first(self):
        def _traverse(node):
            if not node:
                return
            queue = Queue()
            queue.enqueue(node)
            while queue.peek_queue():
                node = queue.dequeue()
                if node:
                    yield node.value
                    if node.left:
                        queue.enqueue(node.left)
                        yield from _traverse(node.left)
                    if node.right:
                        queue.enqueue(node.right)
                        yield from _traverse(node.right)

    def traverse_in_order(self):
            
            def _traverse(node):
                if not node:
                    return
                yield from _traverse(node.left)
                yield node.value
                yield from _traverse(node.right)

            return _traverse(self.root) 

    def traverse_pre_order(self):
            
            def _traverse(node):
                if not node:
                    return
                yield node.value                
                yield from _traverse(node.left)
                yield from _traverse(node.right)

            return _traverse(self.root)          

    def traverse_post_order(self):
            
            def _traverse(node):
                if not node:
                    return
                yield from _traverse(node.right)
                yield node.value                
                yield from _traverse(node.left)

            return _traverse(self.root)          

class Node():
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value