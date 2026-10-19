
V = 5

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

visited = [False] * V
key = [float('inf')] * V
parent = [-1] * V

key[0] = 0

for count in range(V):
    minimum = float('inf')
    u = -1

    for i in range(V):
        if not visited[i] and key[i] < minimum:
            minimum = key[i]
            u = i

    if u == -1:
        break

    visited[u] = True

    for v in range(V):
        if graph[u][v] != 0 and not visited[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u

total = 0
print("Edge    Weight")

for i in range(1, V):
    print(parent[i], "-", i, "   ", graph[i][parent[i]])
    total += graph[i][parent[i]]

print("Total weight of MST =", total)
print("EN.No: 92460118673")