from tree import BinarySearchTree, BinaryTree

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