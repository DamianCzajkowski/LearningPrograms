def fib_memo(n, memo):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n not in memo:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]


cst_dict = {}
print(fib_memo(6, cst_dict))
print(cst_dict)
