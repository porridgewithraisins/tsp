tsp_type = input()  # unused in this trial run

n = int(input())
cities = [tuple(map(float, input().split())) for _ in range(n)]

distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    distances = list(map(float, input().split()))
    for j in range(n):
        distance_matrix[i][j] = distances[j]

tour = []
visited = set()

start_city = 0
current_city = start_city
tour.append(current_city)
visited.add(current_city)

for _ in range(n - 1):
    min_distance = float('inf')
    next_city = None

    for neighbor, distance in enumerate(distance_matrix[current_city]):
        if neighbor not in visited and distance < min_distance:
            min_distance = distance
            next_city = neighbor

    tour.append(next_city)
    visited.add(next_city)
    current_city = next_city


print(" ".join(map(str, tour)))
