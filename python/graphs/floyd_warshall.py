def print_solution(nv, distance):
    for i in range(nv):
        for j in range(nv):
            if distance[i][j] == float("Inf"):
                print("inf", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


def floyd_warshall(nv, g):
    distance = g
    for k in range(nv):
        for i in range(nv):
            for j in range(nv):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
    print_solution(nv, distance)
