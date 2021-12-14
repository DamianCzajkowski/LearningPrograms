def binary_search(items, value):
    start = 0
    end = len(items) - 1
    while start <= end:
        middle = (start + end) // 2
        guess = items[middle]
        if guess == value:
            return middle
        if guess < value:
            start = middle + 1
        elif guess > value:
            end = middle - 1

    return None


print(binary_search([1, 3, 5, 7, 9], 3))
