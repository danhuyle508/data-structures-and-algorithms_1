from radix_sort import radix_sort
def test_radix_sort_one():
    arr =[312,456,1024,566,891,1]
    assert radix_sort(arr) == [1,312,456,566,891,1024]

def test_radix_sort_empty():
    arr =[]
    assert radix_sort(arr) == []

def test_radix_sort_two():
    arr =[499]
    assert radix_sort(arr) == [499]
                