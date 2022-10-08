


import cProfile
from itertools import count


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class CircularList:
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        self.size = 0

    def clear(self):
        self.tail = None
        self.head = None

    def append(self, data):
        node = Node(data, None, None)
        if self.head:
            node.prev=self.head
            self.head.next = node
            self.head = node        
        else:
            self.head = node
            self.tail = node
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size += 1

    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current == prev or prev!=self.head:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                    self.tail.prev = self.head
                    self.head.next = self.tail
                else:
                    prev.next = current.next
                    current.next.prev = prev
                self.size -= 1
                return   
            prev = current
            current = current.next
                
                
                 
    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val
            
    def reverse_iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.prev
            yield val
 
 
            
            
d1=CircularList()
d1.append('eggs')
d1.append('ham')
d1.append('spam')

d1.append('foo')

d1.delete('ham')


counter = 0
for word in d1.reverse_iter():
    print(word)
    counter +=1
    if counter > 10:
        break    
