#what happens in recursion is, we create a function and we call that function again and again.
#let's calculate factorial value using this method.

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1) #call above fact() function again and again --> 4*3*2*1
    
print(fact(4))
print(fact(int(input("Enter the number needs to be in factorial value: "))))

#4 * fact(4-1)
#4 * 3 * fact(3-1)
#4 * 3 * 2 * fact(2-1)
#4 * 3 * 2 * 1 * fact(1-1)
#4 * 3 * 2 * 1 