n = int(input("Enter the target number: "))

result = 1

for i in range(1, n + 1):
    result *= i

print(result)