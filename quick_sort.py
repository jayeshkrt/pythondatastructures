# implementation of quicksort in python

arr = [1783,2134987,2149,129847,1239487,9843,2897,834,2123,17328,6541,91421,18721,1364]

def quicksort(arr):
    length = len(arr)
    if length<=1:
        return arr
    else:
        pivot = arr.pop()

    items_greater = []
    items_lower = []
    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)

print(quicksort(arr))