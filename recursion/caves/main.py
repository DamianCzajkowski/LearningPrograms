from collections import Counter


def chuj(arr):
    if


def recursion_search_for_neighbour(arr, ids, p_ids):
    o_ids = []
    if arr[ids[0]][ids[1]] == 'o':
        o_ids.append(ids)
        to_check = [[ids[0]+1, ids[1]], [ids[0], ids[1]+1],
                    [ids[0]-1, ids[1]], [ids[0], ids[1]-1]]
        to_check.remove(p_ids)
        o_ids.append(recursion_search_for_neighbour(arr, to_check[0], ids))
        o_ids.append(recursion_search_for_neighbour(arr, to_check[1], ids))
        o_ids.append(recursion_search_for_neighbour(arr, to_check[2], ids))
    else:
        return None
    return o_ids


def caves(arr):
    result_dict = [[] for _ in range(4)]
    for id, item in enumerate(arr):
        if type(item) is list:
            result_dict

        elif 'o' == item:
            result_dict[id] += 1
    return result_dict


def search_for_neighbour(arr, idx, idy):
    for i in range(max(idx-1, 0), min(idx+2, 4)):
        for j in range(max(idy-1, 0), min(idy+2, 4)):
            if arr[i][j] == 'o':
                print(i, j)


array = [['oxxx', 'xxxx', 'xxxo', 'xxxx'],
         ['ooxx', 'ooxx', 'xxxo', 'xxxo'],
         ['xxxx', 'xoxx', 'xxxx', 'xxxx'],
         ['xxxx', 'xxxx', 'oooo', 'oooo']]

array2 = [['oxxx', 'xxxx', 'xxxx', 'xxxx'],
          ['ooxx', 'ooxx', 'xxxx', 'xxxx'],
          ['xxxx', 'xoxx', 'xxxx', 'xxxx'],
          ['xxxx', 'xxxx', 'xxxx', 'xxxx']]

array3 = [[['o', 'x', 'x', 'x'], ['x', 'x', 'x', 'x'], ['x', 'x', 'x', 'o'], ['x', 'x', 'x', 'x']],
          [['o', 'o', 'x', 'x'], ['o', 'o', 'x', 'x'], [
              'x', 'x', 'x', 'o'], ['x', 'x', 'x', 'o']],
          [['x', 'x', 'x', 'x'], ['x', 'o', 'x', 'x'], [
              'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x']],
          [['x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x'], ['o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o']]]
# search_for_neighbour(array[1], 0, 0)
# [['oxxx', 'xxxx', 'xxxo', 'xxxx'],
#  ['ooxx', 'ooxx', 'xxxo', 'xxxo'],
#  ['xxxx', 'xoxx', 'xxxx', 'xxxx'],
#  ['xxxx', 'xxxx', 'oooo', 'oooo']]
# [['o','x', 'x', 'x'], ['x', 'x', 'x', 'x'], ['x', 'x', 'x', 'o'], ['x', 'x', 'x', 'x']]
print(recursion_search_for_neighbour(array[0], [0, 0], [-1, 0]))
