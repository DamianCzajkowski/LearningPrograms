def number_of_paths(two_d_arr, row, col, cost):
    if cost < 0:
        return 0
    elif row == 0 and col == 0:
        if two_d_arr[0][0] - cost == 0:
            return 1
        return 0
    elif row == 0:
        return number_of_paths(two_d_arr, 0, col - 1, cost - two_d_arr[row][col])
    elif col == 0:
        return number_of_paths(two_d_arr, row - 1, 0, cost - two_d_arr[row][col])
    op1 = number_of_paths(two_d_arr, row - 1, col, cost - two_d_arr[row][col])
    op2 = number_of_paths(two_d_arr, row, col - 1, cost - two_d_arr[row][col])
    return op1 + op2


two_d_arr = [[4, 7, 1, 6],
             [5, 7, 3, 9],
             [3, 2, 1, 2],
             [7, 1, 6, 3]]
print(number_of_paths(two_d_arr, 3, 3, 25))
