tsp_type = input() # unused in this trial run

n = int(input())
for _ in range(n):
    input()

edges = []

for i in range(n):
    line = input().split()
    for j in range(i + 1, n):
        edges.append(((i, j), float(line[j])))

edges.sort(key=lambda x: x[1])

class DisjointSet:
    def __init__(self, items):
        self.parent = {x: x for x in items}

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        x_repr = self.find(x)
        y_repr = self.find(y)
        self.parent[x_repr] = y_repr


ds = DisjointSet(range(n))
deg = [0] * n

from collections import defaultdict
tour = defaultdict(list)

for (u, v), w in edges:
    if ds.find(u) == ds.find(v):
        continue  # cycle
    if (deg[u] >= 2) or (deg[v] >= 2):
        continue
    tour[u].append(v)
    tour[v].append(u)
    ds.union(u, v)
    deg[u] += 1
    deg[v] += 1

# there will be two vertices with degree 1
# any one of them works as a start (the other will automatically be the end)
for i in range(n):
    if deg[i] == 1:
        break

output = ''

cur = i
prev = i
for i in range(n):
    output += str(cur) + ' '
    for new_cur in tour[cur]:
        if new_cur != prev:
            prev = cur
            cur = new_cur
            break

print(output[:-1])
