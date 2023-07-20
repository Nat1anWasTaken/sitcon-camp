import cmath


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

# Solve the quadratic equation with ax^2 + bx + c = 0

# Calculate the discriminant
d = (b ** 2) - (4 * a * c)

# Find two solutions
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print(f"The solution are {sol1} and {sol2}")
