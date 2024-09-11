#when we define default arguments, program will take them when the parameters not provided

def students(subject="Physics",marks="95"):
    print("Subject = ", subject)
    print("Marks = ", marks)

students("Maths",89)
students()
students("Chemistry")

print("\n ----------------------------------------------------------\n")
def students2(subject,marks,*friends):
    print("Subject = ", subject)
    print("Marks = ", marks)
    print("Friends = ", friends)

students2("Maths", 96, 'Saman','Kamal')
#when we want to provide more than one parameters for an argument we can use * sign before the argument.

print("\n ----------------------------------------------------------\n")
#if we use ** two star signs before an argument we can pass a dictionary to that argument.

def students3(subject,marks,**friends):
    print("Subject = ", subject)
    print("Marks = ", marks)
    print("Friends = ", friends)
    for key,value in friends.items():
        print(key, "=", value)

students3("English", 78, Saman=69, Kamal=54)