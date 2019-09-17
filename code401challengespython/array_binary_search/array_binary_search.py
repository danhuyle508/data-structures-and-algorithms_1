def binary_search(arr, value):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (high+low) // 2
        i = mid
        #import pdb; pdb.set_trace()
        if arr[mid] == value: 
            return i
        else:    
            if arr[mid] > value:
                high = mid -1
            elif arr[mid] < value:
                low = mid + 1
            else: 
                return -1  
    return arr


if __name__ == '__main__':
    print(binary_search([1,2,3], 3))