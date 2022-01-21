def merge(custom_list, left, middle, last):
    n1 = middle - left + 1
    n2 = last - middle

    left_arr = [0] * (n1)
    right_arr = [0] * (n2)

    for i in range(0, n1):
        left_arr[i] = custom_list[left + i]

    for j in range(0, n2):
        right_arr[j] = custom_list[middle + 1 + j]

    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            custom_list[k] = left_arr[i]
            i += 1
        else:
            custom_list[k] = right_arr[j]
            j += 1
        k += 1

    while i < n1:
        custom_list[k] = left_arr[i]
        i += 1
        k += 1

    while j < n1:
        custom_list[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort(custom_list, left, right):
    if left < right:
        middle = (left+(right-1))//2
        merge_sort(custom_list, left, middle)
        merge_sort(custom_list, middle+1, right)
        merge(custom_list, left, middle, right)

    return custom_list


print(merge_sort([5, 2, 1, 6, 78, 2, 11, 3], 0, 7))
