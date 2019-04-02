from merge_sort import merge_sort

def test_merge_sort_one():
    arr = [5,3,2,11,6,14,7,1]
    assert merge_sort(arr) == [1,2,3,5,6,7,11,14]

def test_merge_sort_fail():
    arr = []
    assert merge_sort(arr) == 'List is empty.'

def test_merge_sort_two():
    arr = [4]
    assert merge_sort(arr) == [4]
      
    