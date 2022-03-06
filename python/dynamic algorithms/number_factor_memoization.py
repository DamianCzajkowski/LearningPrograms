def number_factor(n, memo):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    elif n not in memo:
        sub_p1 = number_factor(n-1, memo)
        sub_p2 = number_factor(n-3, memo)
        sub_p3 = number_factor(n-4, memo)
        memo[n] = sub_p1 + sub_p2 + sub_p3
    return memo[n]


cst_dict = {}
print(number_factor(5, cst_dict))
print(cst_dict)
