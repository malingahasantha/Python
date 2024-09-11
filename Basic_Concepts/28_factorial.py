#get a factorial value of a given number.
#factorial means 4!(factorial 4) = 1*2*3*4

x = int(input("Enter the number needs in Factorial: "))
result = 1

for i in range(1,x+1):
    result = result*i

print(result)