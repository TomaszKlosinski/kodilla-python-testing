import math

def prime_factors(number: int) -> list[int]:

    n = int(number)
    result = []

    while n % 2 == 0:
        result.append(2),
        n = n / 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while (n % i == 0):
            result.append(int(i))
            n = n / i
    if n > 2:
        result.append(int(n))

    return result
