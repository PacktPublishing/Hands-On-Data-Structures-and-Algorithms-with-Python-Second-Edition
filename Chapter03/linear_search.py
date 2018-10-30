def searching(search_arr, x):
     for i in range(len(search_arr)):
         if search_arr [i] == x:
             return i
     return -1


search_ar= [3, 4, 1, 6, 14]
x=4

searching(search_ar, x)
print("Index position for the element x is ",searching(search_ar, x))

