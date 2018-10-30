from collections import Counter

c1 = Counter('anysequence')
c2= Counter({'a':1, 'c': 1, 'e':3})
c3= Counter(a=1, c= 1, e=3)
print("print counter 1 is ",c1)
print("print counter 2 is ",c2)
print("print counter 3 is ",c3)



ct = Counter()  # creates an empty counter object
print("print an empty counter----",ct)

ct.update('abca') # populates the object
print("print updated counter ---", ct)

ct.update({'a':3}) # update the count of 'a'

print("print updated counter",ct)

# access all the items in the counter
for item in ct:
   print('%s: %d' % (item, ct[item]))



print("Print element which is not present", ct['x'])

ct.update({'a':-3, 'b':-2, 'e':2})
print ("updated counter", ct)

print("print sorted elements", sorted(ct.elements()))

print("print most common elements", ct.most_common())

ct.subtract({'e':2})

print("print updated counter", ct)





