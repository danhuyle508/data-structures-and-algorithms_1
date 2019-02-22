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