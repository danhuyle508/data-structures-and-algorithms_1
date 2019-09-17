from ll_merge import LinkedList


def test_merge():
    letters = LinkedList()
    numbers = LinkedList()

    letters.insert('A')
    letters.insert('B')
    letters.insert('C')

    numbers.insert(1)
    numbers.insert(2)
    numbers.insert(3)
    actual = letters.merge(numbers)
    expected = 'A'
    

    assert expected == actual.value

def test_merge_list_1_short():
    letters = LinkedList()
    numbers = LinkedList()

    letters.insert('A')
 
    numbers.insert(2)
    numbers.insert(3)

    actual = letters.merge(numbers)

    assert 'A' == actual.value
    assert 2 == actual._next.value
