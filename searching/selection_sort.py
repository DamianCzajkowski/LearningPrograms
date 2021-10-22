def find_smallest(arr):
    smallest = arr[0]
    smallest_id = 0
    for id, item in enumerate(arr):
        if item < smallest:
            smallest = item
            smallest_id = id
    return smallest_id


def selection_sort(arr):
    new_arr = []
    for _ in range(len(arr)):
        smallest_id = find_smallest(arr)
        new_arr.append(arr.pop(smallest_id))
    return new_arr


print(selection_sort([90, 20, 10, 1]))
