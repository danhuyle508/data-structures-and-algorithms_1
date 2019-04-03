def quick_sort(arr,low,high):
    if len(arr) > 1:
        if low < high:
            position = partition(arr,low,high)
            quick_sort(arr,low,position -1)
            quick_sort(arr,position +1,high)
        return arr
    return arr

def partition(arr,low,high):
    position = low
    for i in range(low,high):
        if arr[i] < arr[high]:
            arr[i],arr[position] = arr[position], arr[i]  
            position += 1
    arr[position],arr[high] = arr[high],arr[position] 
    return position         