

def devide(a,b):
    return a/b

def new(func):         #decorator function, here we take devide function as func, we should call it from below. This take function as a parameter.
    def equation(a,b): #get the parameters of devide function
        if b == 0:     
            a,b = b,a
        return func(a,b)
    return(equation)

devide = new(devide)

print(devide(5,0))