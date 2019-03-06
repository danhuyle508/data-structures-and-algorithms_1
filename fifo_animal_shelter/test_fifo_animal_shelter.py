from fifo_animal_shelter import Queue

def test_enqueue_one():
    shelter = Queue()

    shelter.enqueue({'type':'dog', 'name':'fido'})

    assert shelter.tail.value['type'] == 'dog'

def test_enqueue_two():
    shelter = Queue()

    shelter.enqueue({'type':'dog', 'name':'fido'})
    shelter.enqueue({'type':'cat', 'name':'mittens'})

    assert shelter.tail.value['type'] == 'cat'

def test_enqueue_three():
    shelter = Queue()

    shelter.enqueue({'type':'dog', 'name':'fido'})
    shelter.enqueue({'type':'cat', 'name':'mittens'})
    shelter.enqueue({'type':'dog', 'name':'bud'})

    assert shelter.tail.value['name'] == 'bud'  
def test_dequeue_one():
    shelter = Queue()

    shelter.enqueue({'type':'dog', 'name':'fido'})
    shelter.enqueue({'type':'cat', 'name':'mittens'})
    shelter.enqueue({'type':'dog', 'name':'bud'})

    assert  shelter.dequeue('cat') == 'mittens'     

def test_dequeue_two():
    shelter = Queue()

    shelter.enqueue({'type':'dog', 'name':'fido'})
    shelter.enqueue({'type':'cat', 'name':'mittens'})
    shelter.enqueue({'type':'dog', 'name':'bud'})
    # import pdb; pdb.set_trace()
    shelter.dequeue('cat')

    assert  shelter.dequeue('dog') == 'fido'  

def test_dequeue_three():
    shelter = Queue()

    shelter.enqueue({'type':'dog', 'name':'fido'})
    shelter.enqueue({'type':'cat', 'name':'mittens'})
    shelter.enqueue({'type':'dog', 'name':'bud'})
    # import pdb; pdb.set_trace()
    assert shelter.dequeue('cat') == 'mittens'
    assert shelter.dequeue('dog') == 'fido'
    assert shelter.dequeue('dog') == 'bud'      
