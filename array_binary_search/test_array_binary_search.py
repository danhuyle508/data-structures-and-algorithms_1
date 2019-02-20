from array_binary_search import binary_search

def test_binary_search_pass():
    actual = binary_search([1,2,3,4,5,6,7,8,9,10,11], 5)
    expected = 4
    assert expected == actual
    
def test_binary_search_fail():
    actual = binary_search([1,2,3,4,5,6,7], 14)
    expected = -1
    assert expected != actual    

def test_binary_search_pass_again():
    actual = binary_search([1,2,3,4,5,6,7,8,9,10,11], 10)
    expected = 9
    assert expected == actual
