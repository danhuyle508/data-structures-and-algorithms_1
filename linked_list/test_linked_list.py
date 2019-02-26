from linked_list import LinkedList

def test_exists():
    assert LinkedList
    
def test_instantiation():
    """
    Can successfully instantiate an empty linked list
    """
    assert LinkedList()

def test_insert_one():
    """
    Can properly insert into the linked list
    The head property will properly point to the first node in the linked list

    """
    fruits = LinkedList()
    fruits.insert('apples') 
    expected = 'apples'
    actual = fruits.head.value
    assert actual == expected

def test_insert_two():
    """
    Can properly insert multiple nodes into the linked list
    """
    fruits = LinkedList()
    fruits.insert('apples') 
    fruits.insert('orange')

    assert fruits.head.value == 'apples'

    assert fruits.head._next.value == 'orange'

def test_insert_three():
    fruits = LinkedList()
    fruits.insert('apples') 
    fruits.insert('orange')
    fruits.insert('tomato')

    assert fruits.head.value == 'apples'
    assert fruits.head._next.value == 'orange'
    assert fruits.head._next._next.value == 'tomato'

def test_includes():
    """
    Will return true when finding a value within the linked list that exists
    """
    fruits = LinkedList()
    fruits.insert('apples') 
    fruits.insert('orange')
    fruits.insert('tomato')

    assert fruits.includes('orange')
def test_not_includes():
    """
    Will return false when searching for a value in the linked list that does not exist
    """
    fruits = LinkedList()
    fruits.insert('apples') 
    fruits.insert('orange')
    fruits.insert('tomato')

    assert not fruits.includes('cat')    

def test_print():
    """
    Can properly return a collection of all the values that exist in the linked list
    """
    fruits = LinkedList()
    fruits.insert('apples') 
    fruits.insert('orange')
    fruits.insert('tomato')

    assert fruits.print() == 'apples,orange,tomato,'
    
def test_print_edg_case():
    fruits = LinkedList()
    
    assert fruits.print() == -1

def test_append():    
    """
    Can successfully add a node to the end of the linked list
    """
    fruits = LinkedList()
    fruits.insert('apples') 
    fruits.insert('orange')
    fruits.insert('tomato')

    fruits.append('cat')

    expected = 'apples,orange,tomato,cat,'

    assert expected == fruits.print()
def test_append_two():
    """
    Can successfully add multiple nodes to the end of a linked list
    """    
    fruits = LinkedList()
    fruits.insert('apples') 
    fruits.insert('orange')
    fruits.insert('tomato')
    fruits.append('cat')
    fruits.append('shoe')

    assert fruits.print() == 'apples,orange,tomato,cat,shoe,'

def test_insert_before():
    """
    Can successfully insert a node before a node located i the middle of a linked list
    """
    fruits = LinkedList()
    fruits.insert('apples') 
    fruits.insert('orange')
    fruits.insert('tomato')

    fruits.insert_before('orange', 'grape')

    expected = 'apples,grape,orange,tomato,'

    assert expected == fruits.print()
def test_insert_before_first():
    """
    Can successfully insert a node before the first node of a linked list
    """  
    fruits = LinkedList()
    fruits.insert('apples') 
    fruits.insert('orange')
    fruits.insert('tomato')

    fruits.insert_before('apples', 'grape')

    assert fruits.print() == 'grape,apples,orange,tomato,'

def test_insert_after():
    """
    Can successfully insert after a node in the middle of the linked list
    """
    fruits = LinkedList()
    fruits.insert('apples') 
    fruits.insert('orange')
    fruits.insert('tomato')

    fruits.insert_after('orange', 'grape')

    expected = 'apples,orange,grape,tomato,'

    assert expected == fruits.print()
def test_insert_after_last():
    """
    Can successfully insert a node after the last node of the linked list
    """
    fruits = LinkedList()
    fruits.insert('apples') 
    fruits.insert('orange')
    fruits.insert('tomato')

    fruits.insert_after('tomato', 'grape')

    assert fruits.print() == 'apples,orange,tomato,grape,'
def test_find_from_end():
    fruits = LinkedList()
    fruits.insert('apples') 
    fruits.insert('orange')
    fruits.insert('tomato')
    fruits.insert('cherry')
    fruits.insert('kiwi')

    actual = fruits.find_from_end(2)

    expected = 'tomato'

    assert actual == expected

def test_find_from_end_fail():
    fruits = LinkedList()
    fruits.insert('apples') 
    fruits.insert('orange')
    fruits.insert('tomato')
    fruits.insert('cherry')
    fruits.insert('kiwi')

    actual = fruits.find_from_end(7)

    expected = 'Value not found.'

    assert actual == expected    
def test_find_from_end_empty():
    fruits = LinkedList()
    actual = fruits.find_from_end(2)
    expected = 'List is empty.'

    assert actual == expected
