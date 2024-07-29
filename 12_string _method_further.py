name = "Garb Studiolk"

# startswith(), endswith()
print(name.startswith("G"))
print(name.startswith("a"))
print(name.startswith("garb"))
print(name.startswith("Garb"))
print(name.startswith("pro"))
print(name.startswith("studio", 4))

print("-------------------------------------------------------")

print(name.endswith("lk"))
print(name.endswith("l"))


print("------------------replace---------------------------")
#replace method
x = "Malinga, 34, Ratnapura"

print(x)
print(x.replace(",", "|"))
print(x.replace("a", "v"))

print("-------------------------join----------------------------")
#join method
x = 'abc'
y = 'xyz'

print(x.join(y))
print("-".join(y))

name = ["kamal", "saman", "nimal"]
print(" | ".join(name))

print("------------------------------split------------------------")
#split method

name2 = "kamal saman nimal"
print(name2.split())
print(name2.split(" "))
print(name2.split("a"))


name2 = "kamal saman nimal \n 45 65 23"
print(name2.split())
print(name2.split("\n"))
print(name2.splitlines())