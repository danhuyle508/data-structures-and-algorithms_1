from tree import BinarySearchTree, BinaryTree

import pytest

def test_class():
    assert BinarySearchTree

def test_traverse():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')

    items = list(tree.traverse_in_order())

    assert items == ['apples','bananas','cucumbers']

@pytest.mark.skip('pending')
def test_traverse_for_loop():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')

    items = []

    for item in tree.traverse_in_order():
        items.append(item)

    assert items == ['apples','bananas','cucumbers']

def test_traverse_for_loop_pre_order():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')

    items = []

    for item in tree.traverse_pre_order():
        items.append(item)

    assert items == ['bananas','apples','cucumbers']

def test_traverse_for_loop_post_order():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')

    items = []

    for item in tree.traverse_post_order():
        items.append(item)

    assert items == ['cucumbers','bananas','apples']
def test_traverse_for_loop_breaht_first():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')
    tree.add('peaches')
    tree.add('kiwi')
    tree.add('orange')


    items = []

    for item in tree.traverse_breath_first():
        items.append(item)

    assert items == ['bananas','apples','cucumbers','peaches','kiwi','orange']
