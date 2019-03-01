from stacks_and_queues import Stack, Queue

def test_push_one():
    """
    Can successfully push onto a stack
    Can successfully peek the next item on the stack.
    """

    fruits = Stack()

    fruits.push('apple')

    expected = 'apple'

    assert expected == fruits.peek_stack()
def test_push_many():
    """
    Can successfully push multiple nodes onto a stack
    """

    fruits = Stack()

    fruits.push('apple')
    fruits.push('pear')

    expected = 'pear'

    assert expected == fruits.peek_stack()

def test_pop():
    """
    Can successfully pop off the stack
    Can successfully empty a stack after multiple pops.
    """

    fruits = Stack()

    fruits.push('apple')
    fruits.push('pear')
    fruits.pop()
    fruits.pop()

    assert 'No value.' == fruits.peek_stack()    
def test_enqueue_one():
    """
    Can successfully enqueue onto a queue
    Can successfully peek into a queue, seeing the expected value
    """
    food = Queue()
    food.enqueue('bacon')

    expected =  'bacon'

    assert expected == food.peek_queue()     


def test_enqueue_many():
    """
    Can successfully enqueue multiple items into a queue
    """
    food = Queue()
    food.enqueue('bacon')
    food.enqueue('cheese')

    expected =  'bacon'

    assert expected == food.peek_queue() 

def test_dequeue_one():
    food = Queue()
    food.enqueue('bacon')
    food.enqueue('cheese')
    food.dequeue()

    assert 'cheese' == food.peek_queue()        

def test_dequeue_empty():
    """
    Can successfully empty a queue after multiple dequeues
    """
    food = Queue()
    food.enqueue('bacon')
    food.enqueue('cheese')
    food.dequeue()
    food.dequeue()

    assert 'No Value.' == food.peek_queue()
