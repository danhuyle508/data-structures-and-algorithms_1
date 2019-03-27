from left_join import left_join

def test_left_join_1(hash_1, hash_2):
    assert left_join(hash_1,hash_2) == [['mad', 'angry', None], ['sad', 'depressed', 'happy'], ['tired', 'sleepy', 'hyper'], ['happy', 'glad', None]]

def test_left_join_2(hash_1, hash_3):
    assert left_join(hash_1,hash_3) == [['mad', 'angry', None], ['sad', 'depressed', 'happy'], ['tired', 'sleepy', None], ['happy', 'glad', None]]
    
def test_left_join_none(hash_1, hash_4):
    assert left_join(hash_1,hash_4) == [['mad', 'angry', None], ['sad', 'depressed', None], ['tired', 'sleepy', None], ['happy', 'glad', None]]