class Node:
    """ A singly-linked node. """
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """ A singly-linked list. """
    def __init__(self):
        """ Create an empty list. """
        self.tail = None
        self.head = None
        self.count = 0

    def append(self, data):
        """ Append an item to the list """
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1
    
    def iter(self):
        """ Iterate through the list. """
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    

    def delete(self, data):
        """ Delete a node from the list """
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.count -= 1
                return
            prev = current
            current = current.next

    def search(self, data):
        """ Search through the list. Return True if data is found, otherwise
        False. """
        for node in self.iter():
            if data == node:
                return True
        return False

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.tail
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.tail
        for n in range(index):
            current = current.next
        current.data = value

words = SinglyLinkedList()
words.append('foo')
words.append('bar')
words.append('bim')
words.append('baz')
words.append('quux')

print("access by index")
print("here is a node: {}".format(words[1]))

print("modify by index")
words[4] = "Quux"
print("Modified node by index: {}".format(words[4]))

print("This list has {} elements.".format(words.count))
for word in words.iter():
    print("Got this data: {}".format(word))

if words.search('foo'):
    print("Found foo in the list.")
if words.search('amiga'):
    print("Found amiga in the list.")

print("Now we try to delete an item")
words.delete('bim')
print("List now has {} elements".format(words.count))
for word in words.iter():
    print("data: {}".format(word))

print("delete the first item in the list")
words.delete('foo')
print("size: {}".format(words.count))
for word in words.iter():
    print("data: {}".format(word))

print("delete the last item in the list")
words.delete('quux')
print("size: {}".format(words.count))
for word in words.iter():
    print("data: {}".format(word))
