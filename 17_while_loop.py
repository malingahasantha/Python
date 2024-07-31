#we should have define a condition and while loop runs only the condition is True and until the condition is True.

#get 5 input values from user and then return the sum of the input values

i=1
sum=0
while (i<=5):
    val = int(input(f"Enter value {i}: "))
    sum = sum + val
    i = i + 1

print(f"Sum of your entered values are: {sum}")