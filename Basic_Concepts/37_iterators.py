#normally we can access elements one by one using index numbers. But when it come to sets it cannot access by indexes. here we can use iterators.
lst = {3,5,7,9,11}

itr = iter(lst) #convert set to an iterator

print(next(itr))
print(next(itr))
print(itr.__next__())
print(itr.__next__())
#only one value we can get from iterators. 

print("\n")

while True:
        try:
            print(next(itr))  
        except StopIteration:
              break  
    
#since we don't have boundary the error will generate. to avoid that we can use exception handling.

