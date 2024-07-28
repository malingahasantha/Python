name, age, score = "Malinga", 34, 98.5

# First method
print("He is "+ str(name) + ". He is " + str(age) + " years old, and his score is " + str(score)+ ".")

#we should convert the variable values to string values since we are going to print is a string value. So we should use str() function to convert variable values to string data type.

# Second method
print("He is %s. He is %d years old, and his score is %f ." %(name,age,score))

#In here, first we define the data types using % mark. %s - string, %d - decimal, %f - float. Then again in a bracket start with % mark, we should provide the variable names.
#In here the float value output shows 6 decimal points. we can define it as out expectation by using %.2f , %.3f ...etc

print("He is %s. He is %d years old, and his score is %.2f ." %(name,age,score))

# Third method
print("He is {}. He is {} years old, and his score is {}." .format(name,age,score))

#In here we use curly brackets. Values of the curly brackets we can define using .format function. We should provide the variables values in correct order.

print("He is {0}. He is {1} years old, and his score is {2}." .format(name,age,score))

# Fourth method
print(f"He is {name}. He is {age} years old, and his score is {score}.")
#Use f first to define this is a formatted print. Then use curly brackets to define variables.