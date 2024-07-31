# Create function
def functionName(arg1): #define function, def keyword use to identify the function(define the function)
    print(arg1)

functionName("Hello") #pass parameter to fuction

#-----------------------------------------------------

def sum(arg1,arg2):
    print(arg1+arg2)

sum(4,5)


print("\n ------------------------------------------------------------")

def funcRectangle(length,width):
    perimeter = 2*(length+width)
    area = length*width
    print(f"Perimeter of the Rectangle is: {perimeter}")
    print(f"Area of the Rectangle is: {area}")

funcRectangle(4,5)
funcRectangle(8,4)
#we can call the function any time we want

funcRectangle(int(input("Enter Length: ")), int(input("Enter Width: "))) 

