def factorial(a):
    if not isinstance(a, int) or a < 0:
        return
    x = 1
    for i in range(2, a + 1):
        x *= i
    return x

print(factorial(-6), factorial(0), factorial(1), factorial(5), factorial(5.6), factorial('5'))