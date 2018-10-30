
# example to understand functions

def greeting(language):
	if language=='eng':
		return 'hello world'
	if language =='fr':
		return 'Bonjour le monde'
	else: 	return 'language not supported'



l= [greeting('eng'), greeting('fr'), greeting('ger')]

print(l[1])

# high order functions

list=[1,2,3,4]

for item in map(lambda n: n*2, list) : print(item)

for item in filter(lambda n:n<4, list ): print(item)



items= [["rice", 2.4, 8], ["flour", 1.9, 5], ["corn", 4.7, 6]]

items.sort(key=lambda item: item[1])

print(items)
