from insertion_sort import insertion_sort

def test_insertion_sort_one():
    arr =[4,1,5,6,3]

    assert insertion_sort(arr) == [1,3,4,5,6,]
def test_insertion_sort_two():
    arr =[20,11,14,17,19]
    assert insertion_sort(arr) == [11,14,17,19,20]
def test_insertion_sort_empty():
    arr =[]
    assert insertion_sort(arr) == 'List is empty.'    