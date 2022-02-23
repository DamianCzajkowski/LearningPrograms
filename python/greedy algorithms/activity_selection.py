activities = [['A1', 0, 6],
              ['A2', 3, 4],
              ['A3', 1, 2],
              ['A4', 5, 8],
              ['A5', 5, 7],
              ['A6', 8, 9]]


def print_max_activities(activities):
    activities.sort(key=lambda x: x[2])  # O(log(N))
    i = 0
    first_a = activities[i][0]  # O(1)
    print(first_a)
    for j in range(len(activities)):  # O(N)
        if activities[j][1] > activities[i][2]:  # O(1)
            print(activities[j][0])
            i = j


print_max_activities(activities)
