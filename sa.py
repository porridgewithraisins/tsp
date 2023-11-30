import math
import random

def calculate_tour_length(tour, distance_matrix):
    length = 0
    for i in range(len(tour) - 1):
        length += distance_matrix[tour[i]][tour[i + 1]]
    length += distance_matrix[tour[-1]][tour[0]]  # return to the starting city
    return length

def generate_random_tour(n):
    return random.sample(range(n), n)

def generate_neighbor_tour(current_tour):
    i, j = sorted(random.sample(range(len(current_tour)), 2))
    return current_tour[:i] + current_tour[i:j+1][::-1] + current_tour[j+1:]

def simulated_annealing(distance_matrix, initial_temperature, cooling_rate, iterations):
    initial_tour = generate_random_tour(len(distance_matrix))

    current_tour = initial_tour[:]
    current_cost = calculate_tour_length(current_tour, distance_matrix)
    best_tour = current_tour[:]
    best_cost = current_cost

    for iteration in range(iterations):
        temperature = initial_temperature / (1 + cooling_rate * iteration)

        neighbor_tour = generate_neighbor_tour(current_tour)
        neighbor_cost = calculate_tour_length(neighbor_tour, distance_matrix)

        if neighbor_cost < current_cost or random.uniform(0, 1) < math.exp((current_cost - neighbor_cost) / temperature):
            current_tour = neighbor_tour[:]
            current_cost = neighbor_cost

            if current_cost < best_cost:
                best_tour = current_tour[:]
                best_cost = current_cost

    return best_tour

tsp_type = input()  # unused

n = int(input())
cities = [tuple(map(float, input().split())) for _ in range(n)]

distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    distances = list(map(float, input().split()))
    for j in range(n):
        distance_matrix[i][j] = distances[j]

# SA parameters
initial_temperature = 750.
cooling_rate = 0.0075
iterations = 50000

sa_tour = simulated_annealing(distance_matrix, initial_temperature, cooling_rate, iterations)

print(" ".join(map(str, sa_tour)))