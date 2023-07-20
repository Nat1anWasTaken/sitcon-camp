def is_prime(x: int):
    if x < 2:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False

    return True


number = int(input("Enter a number: "))
print(f"{number} is prime: {is_prime(number)}")
