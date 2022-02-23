def find_min_cost(two_d_arr, row, col):
    if row == -1 or col == -1:
        return float("inf")
    elif row == 0 and col == 0:
        return two_d_arr[0][0]
    op1 = find_min_cost(two_d_arr, row-1, col)
    op2 = find_min_cost(two_d_arr, row, col-1)
    return two_d_arr[row][col] + min(op1, op2)


two_d_list = [[4, 7, 8, 6, 4],
              [6, 7, 3, 9, 2],
              [3, 8, 1, 2, 4],
              [7, 1, 7, 3, 7],
              [2, 9, 8, 9, 3]]
print(find_min_cost(two_d_list, 4, 4))
