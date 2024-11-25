def floyd_warshall(graph):
    nodes = list(graph.keys())
    dist = {node: {n: float('inf') for n in nodes} for node in nodes}

    for node in graph:
        dist[node][node] = 0
        for neighbor, weight in graph[node]:
            dist[node][neighbor] = weight

    for k in nodes:
        for i in nodes:
            for j in nodes:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example Usage
graph = {
    'A': [('B', 1)],
    'B': [('C', 2)],
    'C': [('A', 3)]
}
dist_matrix = floyd_warshall(graph)
for node in dist_matrix:
    print(f"{node}: {dist_matrix[node]}")
