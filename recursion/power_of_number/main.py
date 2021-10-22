def power(base, exp):
    assert exp >= 0 and isinstance(exp, int), "exp should be positive integer"
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if base == 0:
        return 0
    return base * power(base, exp-1)


print(power(2, 1))
