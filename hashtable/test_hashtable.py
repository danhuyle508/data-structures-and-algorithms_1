from hashtable import HashTable

def test_hash():
    table = HashTable()

    assert table.hash('animal') == 121
def test_hash_two():
    table = HashTable()
    assert table.hash('house') == 106

def test_hash_three():
    table = HashTable()
    assert table.hash('human') == 104    

def test_add_one():
    table = HashTable()

    assert table.add('animal','cat')  == 'cat'
    
def test_add_two():
    table = HashTable()

    assert table.add('animal','cat')  == 'cat'
    assert table.add('house','ranch')  == 'ranch'

def test_add_three():
    table = HashTable()

    assert table.add('animal','cat')  == 'cat'  
    assert table.add('house','ranch')  == 'ranch'
    assert table.add('human','Dan')  == 'Dan'  

def test_get():
    table = HashTable()
    table.add('animal','cat')
    assert table.get('animal') == 'cat'

def test_get_two():
    table = HashTable()
    table.add('animal','cat')
    table.add('house','ranch')
    assert table.get('house') == 'ranch'  

def test_get_three():
    table = HashTable()
    table.add('animal','cat')
    table.add('house','ranch')
    assert table.get('car') == None     
    
def test_contains():
    table = HashTable()
    table.add('animal','cat')
    assert table.contains('animal') == True

def test_contains_false():
    table = HashTable()
    table.add('animal','cat')
    table.add('house','ranch')
    table.add('car','honda')
    assert table.contains('human') == False 

def test_contains_true():
    table = HashTable()
    table.add('animal','cat')
    table.add('house','ranch')
    table.add('car','honda')
    assert table.contains('house') == True   