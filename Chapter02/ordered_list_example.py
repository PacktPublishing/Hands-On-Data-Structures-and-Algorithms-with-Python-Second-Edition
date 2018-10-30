import collections
od1=  collections.OrderedDict()
od1['one'] = 1
od1['two'] = 2
od2 =  collections.OrderedDict()
od2['two'] = 2
od2['one'] = 1
print("Print if two list are equal or not- ",od1==od2)

kvs = [('three',3), ('four',4), ('five',5)]
od1.update(kvs)
print("print updated ordered list", od1)

#print all the items of ordered list 1:
for k, v in od1.items(): print(k, v)


od3 = collections.OrderedDict(sorted(od1.items(), key= lambda t : (4*t[1])- t[1]**2))
print("print ordered list ", od3)

print("print ordered list values - ",od3.values())

