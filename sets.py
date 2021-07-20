# sets in python

# define an empty set
set1 = set()

# add single elements to the set
set1.add(1)
set1.add("apple")

# add multiple elements
# NOTE: in update ONLY ITERABLE items can be inserted like tuples, lists, strings. ints, floats cannot be inserted
set1.update("boy",(1,2))

# manually define a set
set2 = {1,2,3,"hello","hi",("youtube",4.098)}

# print elements of set (you cannot access them by index)
for i in set1:
	print(i, end=" ")
# Output:
# 1 2 y o apple b

# remove element and don't throw error if it's not present
set1.discard("boy")

# remove but throw an error if the element is not present
set1.remove(2)

# remove the last element of the set (does not matter here because order of elements is not fixed)
# also pop doesn not take any arguments. if you fill one it'll throw an error
# set2.pop("hello")	-> this will throw error
set2.pop()
print()
for i in set2:
	print(i, end=" ")
# Output:
# 1 2 3 ('youtube', 4.098) hello
print()

################ SET OPERATIONS ######################
# get the union of two sets
set3 = set1 | set2
# or
set3 = set1.union(set2)
for i in set3:
	print(i, end=" ")
# Output:
# 1 2 3 y o ('youtube', 4.098) apple b hello

# intersection of sets
print("\n\n now intersection\n")
set4 = set1 & set3
# or
set4 = set3.intersection(set1)
print(set1)
print(set3)
print(set4)
print("\n")

# intersection_update
# updates the output that we get in the original set itself
set1.intersection_update(set2)
print(set1,set2, sep="\n")

# left outer join
"""
______________________
|*******[---|--------]
|*******[---|--------]  		# the * part i.e. A-(A&B)
|*******[---|--------]
______________________
"""
set1 = {'a','b','c','d','e','f','g','h','i'}
set2 = {'b','o','a','r','d'}
set3 = set1-set2
# OR
set3 = set1.difference(set2)
print(set3,"\n")
set3 = set2-set1
# OR
set3 = set2.difference(set1)
print(set3,"\n")

# A | B - A & B
"""
______________________
|*******[---|********]
|*******[---|********]  		# the * part i.e. (A|B)-(A&B)
|*******[---|********]
______________________
"""
set4 = set3 ^ set2
# OR
set4 = set3.symmetric_difference(set2)
# OR
set4 = (set3 | set2) - (set3 & set2)
print(set4,"\n")

# check if set is subset of another
print(set1<set2,"\n")
print(set2<set1,"\n")
print(set1<=set2,"\n")
print(set1==set2,"\n")

# create frozensets
# neither you can add something to it, neither can you remove from it
# it takes dictionary's keys only
frset = frozenset({"apple":"boy","cat":"2","bat":4,5:"cameo",("tata","byebye"):"hola"})
for i in frset:
	print(i, end=" ")