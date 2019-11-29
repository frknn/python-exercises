#find the rootes of given 2. order 1 unknown equation
# ax^2 + bx + c

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b**2 - (4 * a * c)
first_root = (-b - delta ** 0.5) / (2*a)
second_root = (-b + delta ** 0.5) / (2*a)

print("First Root: {}\n"
      "Second Root: {}\n"
      .format(first_root, second_root))