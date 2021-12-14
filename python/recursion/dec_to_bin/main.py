def dec_to_bin(number):
    assert isinstance(number, int), 'number have to be positive integer!'

    if number == 0:
        return 0

    return number % 2 + 10 * dec_to_bin(int(number/2))


print(dec_to_bin(-13))
