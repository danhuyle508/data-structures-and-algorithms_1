from linked_list import LinkedList
import pytest

def test_linked_list_class():
    assert LinkedList

def test_linked_list_instance():
    assert LinkedList('foo')

def test_linked_list_insert_one():
    ll = LinkedList()
    ll.insert('apples')
    assert ll.head.value == 'apples'

def test_linked_list_insert_two():
    ll = LinkedList()
    ll.insert('apples')
    ll.insert('bananas')
    assert ll.head.value == 'apples'
    assert ll.head._next.value == 'bananas'


def test_linked_list_iteration():
    ll = LinkedList()
    ll.insert('apples')
    ll.insert('bananas')

    items = []
    for item in ll:
        items.append(item)

    assert items == ['apples','bananas']

def test_linked_list_conversion ():
    ll = LinkedList()
    ll.insert('apples')
    ll.insert('bananas')

    items = list(ll)

    assert items == ['apples','bananas']

def test_linked_list_expressesion():
    ll = LinkedList()
    ll.insert('apples')
    ll.insert('bananas')

    cap_fruits = [f.upper() for f in ll]

    assert cap_fruits == ['APPLES','BANANAS']

def test_linked_list_filter():
    letters = LinkedList()
    letters.insert('a')
    letters.insert('b')
    letters.insert('c')
    letters.insert('d')
    letters.insert('e')
    letters.insert('f')
    letters.insert('g')

    vowels = 'aeiou'
    
    consonants = [char for char in letters if char not in vowels]

    assert consonants == ['b','c','d','f','g']

    

def test_insert_operator():
    animals = LinkedList()

    animals += 'giraffe'

    assert list(animals) == ['giraffe']

def test_concat():
    montagues = LinkedList(['Romeo','Benvolio'])

    capulets = LinkedList(['Juliet','Tybalt'])

    tutti = montagues + capulets

    assert len(list(tutti)) == 4

    assert len(list(montagues)) == 2