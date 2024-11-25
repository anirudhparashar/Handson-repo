def bellman_ford(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                return "Negative weight cycle detected."

    return distances

# Example Usage
graph = {
    'A': [('B', 1)],
    'B': [('C', 2)],
    'C': [('A', -6)]
}
print(bellman_ford(graph, 'A'))
