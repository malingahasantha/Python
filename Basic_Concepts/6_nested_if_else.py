number = 6

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Number is Zero")

# With nested if else
if number > 0:
    print("Positive Number")
else:
    if number < 0:
        print("Negative Number")
    else:
        print("Number is Zero")
# ---------------------------------------------------

if number != 0:
    if number > 0:
        print("Positive Number")
    elif number < 0:
        print("Negative Number")
else:
    print("Number is Zero")