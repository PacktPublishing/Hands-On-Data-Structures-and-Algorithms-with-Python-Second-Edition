list()   # an empty list   
list1 = [1,2,3, 4]
list1.append(1)
print ("print list",list1)

list2 = list1 *2
print(list2)

print("minimum in list 1 is ",min(list1))

print("maximum in list 1 is", max(list1))

list1.insert(0,2)  # insert an value 2 at index 0
print("updated list 1 is ", list1)

list1.reverse()
print("revised list 1 is ", list1)

list2=[11,12]
list1.extend(list2)
print("updated list 1 is",list1)

print("sum of all the elements in list1 is",sum(list1))

print("length of list 1 is ",len(list1))

list1.sort()
print("sorted list 1 is", list1)

list1.remove(12)   #remove value 12 form the list
print("list 1 after removal of element 12 is ", list1)

