def gcd(a, b):
    assert isinstance(a, int) and isinstance(
        b, int), "a, b should be positive integer"
    if b < 0:
        b = b * -1
    if a < 0:
        a = a * -1
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(48, 18))
