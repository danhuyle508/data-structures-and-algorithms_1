def insertShiftArray(arr, num):
    count = len(arr)
    middle = len(arr) // 2
    shift_arr = []
    for i in range(count):
        if i != middle:
            shift_arr.append(arr[i])
        else:
            shift_arr.append(arr[i])
            shift_arr.append(num)    
    return shift_arr
           