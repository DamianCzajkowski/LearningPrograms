def find_min_operation(s1, s2, index1, index2, temp_dict):
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return find_min_operation(s1, s2, index1 + 1, index2 + 1, temp_dict)
    dict_key = str(index1) + str(index2)
    if dict_key not in temp_dict:
        delete_op = 1 + find_min_operation(s1, s2, index1, index2 + 1, temp_dict)
        insert_op = 1 + find_min_operation(s1, s2, index1 + 1, index2, temp_dict)
        replace_op = 1 + find_min_operation(s1, s2, index1 + 1, index2 + 1, temp_dict)
        temp_dict[dict_key] = min(delete_op, insert_op, replace_op)
    return temp_dict[dict_key]


print(find_min_operation("Table", "Tbrlt", 0, 0, {}))
