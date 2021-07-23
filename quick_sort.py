import random 

def quicksort(arr, start , stop): 
    if(start < stop): 
        pivotindex = partitionrand(arr, start, stop) 
        quicksort(arr , start , pivotindex - 1) 
        quicksort(arr, pivotindex + 1, stop) 


def partitionrand(arr , start, stop): 

    randpivot = random.randrange(start, stop) 

    arr[start], arr[randpivot] = arr[randpivot], arr[start] 
    return partition(arr, start, stop) 


def partition(arr,start,stop): 
    pivot = start # pivot 
    i = start + 1 # a variable to memorize where the  
                  # partition in the array starts from. 
    for j in range(start + 1, stop + 1): 
        if arr[j] <= arr[pivot]: 
            arr[i] , arr[j] = arr[j] , arr[i] 
            i = i + 1
    arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot] 
    pivot = i - 1
    return (pivot)

arr = [1783,2134987,2149,129847,1239487,9843,2897,834,2123,17328,6541,91421,18721,1364]
quicksort(arr, 0,len(arr)-1)
print(arr)