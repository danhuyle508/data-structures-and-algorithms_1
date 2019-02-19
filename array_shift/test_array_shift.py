from array_shift import insertShiftArray

def test_insertShiftArray():
    actual = insertShiftArray([2,4,6,8], 5)
    expected =[2,4,5,6,8]
    assert expected == actual
def test_insertShiftArray_2():
    actual = insertShiftArray([1,3,5,7,9], 20)
    expected = [1,3,5,20,7,9]
    assert expected == actual
def test_insertShiftArray_3():
    actual = insertShiftArray([5,10,15,20,25,30], 7)
    expected = [5,10,15,7,20,25,30]
    assert expected == actual        