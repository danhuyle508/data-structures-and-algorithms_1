class BinaryTree(object):
    def __init__(self):
        self.root = None

    def fizz_buzz_tree(self, current_node):
        """
        returns a list of nodes in order node,left,right
        """
        tree_list =[]
        if current_node.data == self.root.data:
            if int(str(current_node.data)) % 3 == 0:
                if int(str(current_nodet.data)) % 5 == 0:
                    current_node.data = 'FizzBuzz'
                else:
                   current_node.data = 'Fizz'  
            elif int(str(current_node.data)) % 5 == 0:
                current_node.data = 'Buzz'     

        tree_list.append(current_node.data)  
        if current_node.left:
            if int(str(current_node.left.data)) % 3 == 0:
                if int(str(current_node.left.data)) % 5 == 0:
                    current_node.left.data = 'FizzBuzz'
                else:
                   current_node.left.data = 'Fizz'  
            elif int(str(current_node.left.data)) % 5 == 0:
                current_node.left.data = 'Buzz'          
            tree_list += self.fizz_buzz_tree(current_node.left)   
        if current_node.right:
            if int(str(current_node.right.data)) % 3 == 0:
                if int(str(current_node.right.data)) % 5 == 0:
                    current_node.right.data = 'FizzBuzz'
                else:
                   current_node.right.data = 'Fizz'  
            elif int(str(current_node.right.data)) % 5 == 0:
                current_node.right.data = 'Buzz' 
            tree_list += self.fizz_buzz_tree(current_node.right)
        return tree_list        

class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None

    def add(self,value):
        """
        add a root to the tree
        """
        try:
            if not self.root:
                self.root = Node(value)
            else:
                self.add_child(value,self.root)
        except:
            return 'Unable to insert Node'   

    def add_child(self, value,current):
        """
        adds a child to the tree  
        """
        if value > current.data:
            if not current.right:
                current.right = Node(value)
            else:
                self.add_child(value, current.right)
        elif value < current.data:
            if not current.left:
                current.left = Node(value)
            else:
                self.add_child(value, current.left)
class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data