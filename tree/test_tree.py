from tree import BinarySearchTree, BinaryTree

def test_find_maximum_value_one():
    my_tree = BinarySearchTree()

    my_tree.add(10)
    my_tree.add(4)
    my_tree.add(15) 
    my_tree.add(25)
    my_tree.add(7)
    my_tree.add(1)
    my_tree.add(13)
    assert my_tree.find_maximum_value(my_tree.root) == 25 

def test_find_maximum_value_two():
    my_tree = BinarySearchTree()

    my_tree.add(10)
    my_tree.add(4)
    my_tree.add(15) 
    my_tree.add(25)
    my_tree.add(7)
    my_tree.add(1)
    my_tree.add(55)
    assert my_tree.find_maximum_value(my_tree.root) == 55    

def test_breadth_first_traversal_one():
    my_tree = BinarySearchTree()

    my_tree.add(10)
    my_tree.add(4)
    my_tree.add(15) 
    my_tree.add(25)
    my_tree.add(7)
    my_tree.add(1)
    my_tree.add(13)    
    assert my_tree.breadth_first_traversal(my_tree.root) == [10,4,15,1,7,13,25]

def test_breadth_first_traversal_two():
    my_tree = BinarySearchTree()

    my_tree.add(10)
    my_tree.add(4)
    my_tree.add(15) 
    my_tree.add(25)
    my_tree.add(7)
    my_tree.add(1)
    my_tree.add(13)
    my_tree.add(11)
    my_tree.add(17)    
    assert my_tree.breadth_first_traversal(my_tree.root) == [10,4,15,1,7,13,25,11,17]

def test_breadth_first_traversal_three():
    my_tree = BinarySearchTree()

    my_tree.add(10)
    my_tree.add(4)
    my_tree.add(15) 
    my_tree.add(25)
    my_tree.add(7)
    my_tree.add(1)
    my_tree.add(13)
    my_tree.add(11)
    my_tree.add(17)
    my_tree.add(6)    
    assert my_tree.breadth_first_traversal(my_tree.root) == [10,4,15,1,7,13,25,6,11,17]

def test_inorder():
    my_tree = BinarySearchTree()

    my_tree.add(10)
    my_tree.add(4)
    my_tree.add(15) 
    assert my_tree.inorder(my_tree.root) == [4,10,15]
def test_preorder():
    my_tree = BinarySearchTree()

    my_tree.add(10)
    my_tree.add(4)
    my_tree.add(15) 
    assert my_tree.preorder(my_tree.root) == [10,4,15]   

def test_postorder():
    my_tree = BinarySearchTree()

    my_tree.add(10)
    my_tree.add(4)
    my_tree.add(15) 
    assert my_tree.postorder(my_tree.root) == [4,15,10]     

def test_add_one():
    my_tree = BinarySearchTree()

    my_tree.add(10)
    assert my_tree.root.data == 10

def test_add_two():
    my_tree = BinarySearchTree()

    my_tree.add(10)
    my_tree.add(4)
    assert my_tree.root.left.data == 4    

def test_add_three():
    my_tree = BinarySearchTree()

    my_tree.add(10)
    my_tree.add(4)
    my_tree.add(15)
    assert my_tree.root.right.data == 15

def test_contains_one():
    my_tree = BinarySearchTree()

    my_tree.add(10)
    my_tree.add(4)
    my_tree.add(15)  
    assert my_tree.contains(10) == True 

def test_contains_two():
    my_tree = BinarySearchTree()

    my_tree.add(10)
    my_tree.add(4)
    my_tree.add(15)  
    assert my_tree.contains(1) == False
def test_contains_three():
    my_tree = BinarySearchTree()

    my_tree.add(10)
    my_tree.add(4)
    my_tree.add(15)  
    assert my_tree.contains(15) == True