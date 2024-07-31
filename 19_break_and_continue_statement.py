# In continue when the condition is true in if statement or what ever state skip once that moment
# In break, when the condition is true the it stops the program

for x in range(1,6):
    if (x==3):
        continue
    print(x)

print("\n ----------------------------------")

i=0
while (i<5):
    i= i+1
    if (i==3):
        continue
    print(i)
    

print("\n ------------------------ break -----------------------")

for x in range(1,6):
    if (x==3):
        break
    print(x)

print("\n ----------------------------------")

i=0
while (i<5):
    i= i+1
    if (i==3):
        break
    print(i)