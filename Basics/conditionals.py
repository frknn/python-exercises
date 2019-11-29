x=7
y=7.0

if x>y:
    print(f"{x} is greater than {y}")
elif x == y:
    print(f"{x} is equal to {y}")
else:
    print(f"{x} is less than {y}")
    
if x>2 and x <10: # we can use or instead of and too
    print(f"{x} is in between 2 and 10")

if not(x == y):
    print(f"{x} is not equal to {y}")

numbers = [1,2,3,4,5]
if x in numbers:
    print(x)
if x not in numbers:
    print("not found")

#identity operators(is, is not) compares the objects if they are actually the same object with the same memory location, not only if they are equal
if x is y:
    print("x = y")
else:
    print("x != y")