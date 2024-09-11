#first of all we should import datetime module. this module is an inbuilt module in python.

import datetime

b_day = datetime.date(1990,4,6)
print(b_day)

today = datetime.date.today()
print(today)

#this can take in several methods

print(b_day.strftime('%A, %B, %d, %Y'))
#these codes "use in strftime" you can find in internet. there are several types.

#Age = Today - Birthday

age = today - b_day
print(age)


print(today.weekday())
#in weekday method they define dates as this 0-6 : Monday=0, Tuesday=1, Wednesday=2, Thursday=3...
#in isoweekday method they define dates as from 1 to 7.
print(today.isoweekday())

#if we want to show both date and time, we should call datetime method in datetime module
t = datetime.datetime.today()
print(t)