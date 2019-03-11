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
        tree_list.append(current_node.data)     
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
        tree_list.append(current_node.data)      
        return tree_list  
        
    def preorder(self, current_node):
        """
        returns a list of nodes in order node,left,right
        """
        tree_list =[]
        tree_list.append(current_node.data)  
        if current_node.left:
            tree_list += self.inorder(current_node.left)   
        if current_node.right:
            tree_list += self.inorder(current_node.right)
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

    def contains(self, value, current = None):
        """
        search for a value
        """
        if not current:
            current = self.root 
        if current.data == value:
            return True   
        if not self.root:
            return False    
        elif value < current.data:
            if current.left:
                return self.contains(value,current.left)
            else:
                return False
        elif value > current.data:
            if current.right:
                return self.contains(value,current.right)
            else: 
                return False            

class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data