def partition(custom_list, low, high):
    i = low - 1
    pivot = custom_list[high]
    for j in range(low, high):
        if custom_list[j] <= pivot:
            i += 1
            custom_list[i], custom_list[j] = custom_list[j], custom_list[i]
    custom_list[i+1], custom_list[high] = custom_list[high], custom_list[i+1]
    return (i+1)


def quick_sort(custom_list, low, high):
    if low < high:
        pi = partition(custom_list, low, high)
        quick_sort(custom_list, low, pi-1)
        quick_sort(custom_list, pi+1, high)
    return custom_list


print(quick_sort([5, 2, 1, 6, 78, 2, 11, 3], 0, 7))
