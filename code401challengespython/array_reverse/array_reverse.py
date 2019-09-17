def reverseArray(arr):
    #get the lenght of the array
    count = len(arr)
    #create a blank array
    reverse_arr = []
    #loop through the old array in reverse and store it in a new array
    for i in range(count):
        #append value of the element to new array
        reverse_arr.append(arr[count-i-1])
    #return array    
    return reverse_arr    
    
array = [4,8,16]
print(reverseArray(array))    