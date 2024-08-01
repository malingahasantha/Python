
from dir import cal
#here we should define as above, when our files are in another directories. we can write as below as well.
# --> "import dir.cal" -- if we write like this we should edit below print functions as print(dir.cal.add(i,j))
# --> "import dir.cal as cal" -- also we can write like this as well. in here we no longer need to type dir.cat...

i=25
j=5

print(cal.add(i,j))
print(cal.sub(i,j))
print(cal.mul(i,j))
print(cal.div(i,j))
