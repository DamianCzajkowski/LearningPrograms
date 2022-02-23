def coin_change(total_number, coins):
    N = total_number
    coins.sort()
    index = len(coins) - 1

    while True:  # O(N)
        coin_value = coins[index]
        if N >= coin_value:  # O(1)
            print(coin_value)
            N -= coin_value
        if N < coin_value:  # O(1)
            index -= 1

        if N == 0:
            break


coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]

coin_change(2137, coins)
