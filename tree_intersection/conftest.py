from tree import BinarySearchTree
import pytest
import os

@pytest.fixture()
def tree1():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(1)
    tree.add(7)
    tree.add(15)
    tree.add(11)
    tree.add(17)

    return tree

@pytest.fixture()
def tree2():
    tree = BinarySearchTree()
    tree.add(11)
    tree.add(6)
    tree.add(2)
    tree.add(7)
    tree.add(18)
    tree.add(12)
    tree.add(45)

    return tree 

@pytest.fixture()
def tree3():
    tree = BinarySearchTree()
    tree.add(14)
    tree.add(30)
    tree.add(3)
    tree.add(9)
    tree.add(18)
    tree.add(13)
    tree.add(45)
    tree.add(12)

    return tree    