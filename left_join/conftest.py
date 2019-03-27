from hashtable import HashTable
import pytest
import os

@pytest.fixture()
def hash_1():
    hash_1 = HashTable()
    hash_1.add('sad', 'depressed')
    hash_1.add('happy', 'glad')
    hash_1.add('tired', 'sleepy')
    hash_1.add('mad', 'angry')
    return hash_1

@pytest.fixture()
def hash_2():
    hash_2 = HashTable()
    hash_2.add('sad', 'happy')
    hash_2.add('tired', 'hyper')
    return hash_2
@pytest.fixture()
def hash_3():
    hash_3 = HashTable()
    hash_3.add('sad', 'happy')
    hash_3.add('cat', 'tiger')
    return hash_3   
@pytest.fixture()
def hash_4():
    hash_4 = HashTable()
    hash_4.add('cat', 'tiger')
    return hash_4 