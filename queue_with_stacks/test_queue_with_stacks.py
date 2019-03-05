from queue_with_stacks import Queue, Stack

def test_enqueue_one():
    do_something = Queue()
    do_something.enqueue('apple')
    
    assert do_something.show() == 'apple'

def test_enqueue_two():
    do_something = Queue()
    do_something.enqueue('apple')
    do_something.enqueue('pear')

    assert do_something.show() == 'pear'

def test_enqueue_three():
    do_something = Queue()
    do_something.enqueue('apple')
    do_something.enqueue('pear')
    do_something.enqueue('cherry')

    assert do_something.show() == 'cherry'

def test_dequeue_one():
    do_something = Queue()
    #import pdb; pdb.set_trace()

    do_something.enqueue('apple')
    do_something.enqueue('pear')
    do_something.enqueue('cherry')  
    assert do_something.dequeue() == 'apple'

def test_dequeue_two():
    fruits = Queue()    
    fruits.enqueue('apple')
    fruits.enqueue('pear')
    fruits.enqueue('cherry')

    fruits.dequeue()
    assert fruits.dequeue() == 'pear'

# def test_dequeue_two():
#     fruits = Queue()    
#     fruits.enqueue('apple')
#     fruits.enqueue('pear')
#     fruits.enqueue('cherry')
#     fruits.dequeue()
#     fruits.dequeue()
#     assert fruits.dequeue() == 'cherry'    

