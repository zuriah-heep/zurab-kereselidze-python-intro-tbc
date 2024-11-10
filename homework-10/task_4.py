def is_prime(a):
    if not isinstance(a, int) or a <= 1:
        return

    for i in range(2, int(abs(a)**0.5) + 1):
        if not a % i:
            return 'No'
    return 'Yes'

print(is_prime(1), is_prime(2), is_prime(4), is_prime(5), is_prime(137))