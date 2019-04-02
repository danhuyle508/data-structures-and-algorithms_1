def merge_sort(arr):
    """
    A funciton to merge sort an array
    """
    if arr != []:
        if len(arr) <= 1:  
            return arr
        mid = len(arr) //2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left,right)
    return 'List is empty.' 
   
def merge(left,right):
    """
    a function to merge the contents of an array
    """
    left_index = 0
    right_index = 0
    sorted_arr = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_arr.append(left[left_index])
            left_index += 1
        else:
            sorted_arr.append(right[right_index])
            right_index += 1
    
    sorted_arr += left[left_index:]
    sorted_arr += right[right_index:]
    return sorted_arr