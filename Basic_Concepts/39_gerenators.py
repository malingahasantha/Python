def test(a):
    for i in a:
        yield i

y = test([2,4,6,8,10])
print(next(y))
print(next(y))
print(next(y))

print("\n ------- fib -------")
def fib():
    a=0
    b=1
    #(a,b=0,1)
    while True:
        c = a+b
        yield a
        a = b
        b = c
        #(a,b = b,c)

y = fib()
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))