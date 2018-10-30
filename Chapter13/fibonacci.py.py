def fib(n): 
        if n <= 2: 
            return 1 
        else: 
            return fib(n-1) + fib(n-2) 



def dyna_fib(n, lookup): 
        if n <= 2: 
            lookup[n] = 1 
        if lookup[n] is None: 
            lookup[n] = dyna_fib(n-1, lookup) + dyna_fib(n-2, lookup) 
        return lookup[n] 



def fib_tab(n): 
        results = [1, 1] 
        for i in range(2, n): 
            results.append(results[i-1] + results[i-2]) 
        return results[-1] 



for i in range(6):
    print(fib(i))

lookup = [None]*(1000) 

 
print("another way to print ith value in fibonacci series")
print(dyna_fib(6, lookup))

print("another way to print ith value in fibonacci series")
print(fib_tab(6))