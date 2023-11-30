def nearest_neighbor_tour(distance_matrix):
    n = len(distance_matrix)
    tour = []
    visited = set()

    start_city = 0  # Choose any city as the starting point
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

    return tour

def two_opt_swap(tour, i, k):
    return tour[:i] + tour[i:k+1][::-1] + tour[k+1:]

def two_opt(distance_matrix):
    tour = nearest_neighbor_tour(distance_matrix)
    best_tour = list(tour)

    def calculate_tour_length(tour):
        length = 0
        for i in range(len(tour) - 1):
            length += distance_matrix[tour[i]][tour[i + 1]]
        length += distance_matrix[tour[-1]][tour[0]]  # Return to the starting city
        return length

    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 1):
            for k in range(i + 1, len(tour)):
                new_tour = two_opt_swap(best_tour, i, k)
                new_tour_length = calculate_tour_length(new_tour)

                if new_tour_length < calculate_tour_length(best_tour):
                    best_tour = list(new_tour)
                    improvement = True

    return best_tour

# Example Usage:
tsp_type = input()  # unused in this trial run

n = int(input())
cities = [tuple(map(float, input().split())) for _ in range(n)]

# Create a matrix to store distances between cities
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    distances = list(map(float, input().split()))
    for j in range(n):
        distance_matrix[i][j] = distances[j]

# Apply 2-opt
optimal_tour = two_opt(distance_matrix)

# Output the improved tour
print(" ".join(map(str, optimal_tour)))