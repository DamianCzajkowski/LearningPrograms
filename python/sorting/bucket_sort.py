import math


def bucket_sort(custom_list):
    number_of_buckets = round(math.sqrt(len(custom_list)))
    max_value = max(custom_list)
    arr = []
    for _ in range(number_of_buckets):
        arr.append([])
    for j in custom_list:
        index_b = math.ceil(j*number_of_buckets/max_value)
        arr[index_b-1].append(j)

    for i in range(number_of_buckets):
        arr[i] = sorted(arr[i])

    new_list = []
    for s_list in arr:
        new_list.extend(s_list)
    return new_list


print(bucket_sort([5, 2, 1, 6, 78, 2, 11, 3]))
