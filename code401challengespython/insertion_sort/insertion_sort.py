def insertion_sort (arr):
    if arr != []:    
        for i in range(1, len(arr)): 
            current = arr[i] 
            key = i-1
            while key >=0 and current < arr[key] : 
                arr[key+1] = arr[key] 
                key -= 1
            arr[key+1] = current

        return arr    
    return 'List is empty.'    