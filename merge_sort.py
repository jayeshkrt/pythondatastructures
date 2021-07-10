# python implementation of merge sort
arr = [1783,2134987,2149,129847,1239487,9843,2897,834,2123,17328,6541,91421,18721,1364]

def merge(left, right, arr):
    nL = len(left)
    nR = len(right)

    i=0
    j=0
    k=0

    while i<nL and j<nR:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k]=right[j]
            j += 1
        k += 1

    while(i < nL):
        arr[k] = left[i]
        i+=1
        k+=1
    while(j < nR):
        arr[k] = right[j]
        j+=1
        k+=1
    return arr


def merge_sort(arr):
    n = len(arr)

    if n<2:
        return arr
    
    mid = n//2
    left = []
    right = []
    for i in range(mid):
        left.append(arr[i])
    
    for i in range(mid,n):    # Very important: it should range from mid to n
        right.append(arr[i])

    left = merge_sort(left)
    right = merge_sort(right)

    return(merge(left, right, arr))

print(merge_sort(arr))