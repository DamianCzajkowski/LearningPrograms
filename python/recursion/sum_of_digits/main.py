def sum_of_digits(n):
    assert n >= 0 and isinstance(n, int), 'Number should be positive int'
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n//10)


print(sum_of_digits(1.2))
