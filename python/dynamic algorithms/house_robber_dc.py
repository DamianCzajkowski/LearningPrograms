def house_robber_td(houses, current_index, temp_dict):
    if current_index >= len(houses):
        return 0
    if current_index not in temp_dict:
        steal_first_house = houses[current_index] + house_robber_td(houses, current_index + 2, temp_dict)
        skip_first_house = house_robber_td(houses, current_index + 1, temp_dict)
        temp_dict[current_index] = max(steal_first_house, skip_first_house)
    return temp_dict[current_index]


houses = [6, 7, 1, 30, 8, 2, 4]
print(house_robber_td(houses, 0, {}))


def house_robber_bu(houses, current_index):
    temp_arr = [0] * (len(houses)+2)
    for i in range(len(houses)-1, -1, -1):
        temp_arr[i] = max(houses[i] + temp_arr[i+2], temp_arr[i+1])
    return temp_arr[0]


print(house_robber_bu(houses, 0))
