
# example to understand variables 
a= [2, 4, 6]
b=a 
a.append(8)
print(b)


# example to understand variable scope

a=10;b=20
def my_function():
   global a 
   a=11; b=21

my_function()
print(a) #prints11 
print(b)  #prints20



# example to understand the conditions 
x='one' 

if x==0:
   print('False')
elif  x==1:
   print('True')
else:  print('Something else')

#prints 'Something else'


# example to understand looping

words = ['cat', 'dog', 'elephant']
for w in words:
     print(w)


 


