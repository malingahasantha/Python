#normally we can access elements one by one using index numbers. But when it come to sets it cannot access by indexes. here we can use iterators.
lst = {3,5,7,9}

itr = iter(lst)

print(next(itr))
print(next(itr))
#only one value we can get from iterators. 

while True:
        try:
            print(next(itr))  
        except:
              break  
    
#since we don't have boundary the error will generate. to avoid that we can use exception handling.

