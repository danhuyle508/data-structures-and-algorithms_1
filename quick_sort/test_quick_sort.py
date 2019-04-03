from quick_sort import quick_sort

def test_quick_sort_one():
    arr = [5,2,11,9,4,18,10,7,14,8]

    assert quick_sort(arr,0,len(arr)-1) == [2,4,5,7,8,9,10,11,14,18]

def test_quick_sort_empty():
    arr = []
    assert quick_sort(arr,0,len(arr)-1) == []    
def test_quick_sort_two():
    arr = [3]
    assert quick_sort(arr,0,len(arr)-1) == [3]        