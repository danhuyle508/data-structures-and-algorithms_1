from fizz_buzz_tree import BinarySearchTree, BinaryTree

def test_fizz_buzz_tree():
    my_tree = BinarySearchTree()

    my_tree.add(10)
    my_tree.add(4)
    my_tree.add(15) 
    assert my_tree.fizz_buzz_tree(my_tree.root) == ['Buzz',4,'FizzBuzz']

def test_fizz_buzz_tree_two():
    my_tree = BinarySearchTree()

    my_tree.add(10)
    my_tree.add(4)
    my_tree.add(15) 
    my_tree.add(30)
    assert my_tree.fizz_buzz_tree(my_tree.root) == ['Buzz',4,'FizzBuzz','FizzBuzz']
def test_fizz_buzz_tree_three():
    my_tree = BinarySearchTree()

    my_tree.add(10)
    my_tree.add(4)
    my_tree.add(15) 
    my_tree.add(30)
    my_tree.add(11)
    assert my_tree.fizz_buzz_tree(my_tree.root) == ['Buzz',4,'FizzBuzz',11,'FizzBuzz']