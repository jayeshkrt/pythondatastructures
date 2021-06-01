# array
arr=[]
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)

# make copy of the array
arr2 = arr.copy()

# remove all elements from array
arr.clear()

# return count of number of time that element is occuring in that array
print(arr2.count(1))

# when you pass something in extend, it iterates over that object and then add the output to the list
arr.extend("apple")   # it will add all characters in the string and add to the list
arr.extend([1,2,3,4,5,6,7,8,9])      # it will add the elements of the list to that list

# index returns the index at which the element is located in the list
print(arr.index(4))

# insert will insert the element ant the given index (index first, element second)
arr.insert(3,51)

# pop returns the last element and deletes it from the list
print(arr.pop())

# remove removes that element. Enter that element not its index. It returns None
print(arr.remove(51))

# reverse reverses the list. It also returns None
print(arr.reverse())

# sort in ascending or increasing order. It works only when the elements are of the same type
arr2 = ['agdydg','uyfg','hweu','oiwqdj','uewfyg']
arr2.sort()


print(arr2)

print(arr)
print(arr2)
