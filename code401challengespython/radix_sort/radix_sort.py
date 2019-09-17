import math
def radix_sort(arr):
    if arr != []:
        bucket_size = 10
        maxLength = False
        temp = -1 
        placement = 1

        while not maxLength:
            maxLength = True
            buckets = [list() for i in range( bucket_size )]
            #empty the arr
            for i in arr:
                temp = math.floor(i / placement)
                buckets[temp % bucket_size].append( i )
                if maxLength and temp > 0:
                    maxLength = False
        
            a = 0
            #append numbers back to arr in order
            for b in range( bucket_size ):
                buck = buckets[b]
                for i in buck:
                    arr[a] = i
                    a += 1
        
            placement *= bucket_size
        return arr
    return arr    