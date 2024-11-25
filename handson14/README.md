### **1. Implementing Dijkstra’s Algorithm**
**Description**: Dijkstra's algorithm finds the shortest paths from a source node to all other nodes in a graph with non-negative weights.

**Steps**:
- Use an adjacency list or matrix to represent the graph.
- Use a priority queue (min-heap) for efficient extraction of the minimum distance node.
- Update distances iteratively until all nodes are processed.

**Example Graph**:
```
Graph:
    A - 1 -> B
    A - 4 -> C
    B - 2 -> C
    B - 6 -> D
    C - 3 -> D

Expected Output (Shortest path from A):
    A -> 0, B -> 1, C -> 3, D -> 6
```

**Code (Python)**:
```python
import heapq

def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    pq = [(0, source)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example Usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 6)],
    'C': [('D', 3)],
    'D': []
}
print(dijkstra(graph, 'A'))
```

---

### **2. Bellman-Ford Algorithm**
**Description**: Bellman-Ford works for graphs with negative weights and detects negative weight cycles.

**Steps**:
- Initialize distances with `inf` except for the source.
- Relax edges for `|V| - 1` iterations (V: number of vertices).
- Check for negative weight cycles in a final pass.

**Example Graph**:
```
Graph:
    A - 1 -> B
    B - 2 -> C
    C - (-6) -> A

Expected Output (Shortest path from A):
    Negative weight cycle detected.
```

**Code (Python)**:
```python
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
```

---

### **3. Floyd-Warshall Algorithm**
**Description**: Floyd-Warshall calculates the shortest paths between all pairs of vertices in a graph.

**Steps**:
- Use a 2D matrix `dist` initialized with edge weights.
- Update `dist[i][j]` via intermediate vertices using the relation:  
  `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`.

**Example Graph**:
```
Graph:
    A - 1 -> B
    B - 2 -> C
    C - 3 -> A

Expected Output:
    Shortest path matrix:
    A: [0, 1, 3]
    B: [inf, 0, 2]
    C: [inf, inf, 0]
```

**Code (Python)**:
```python
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
```

---

### **Testing**
1. Run each example graph and verify that the output matches the expected results.
2. Use additional test cases, including edge cases like disconnected nodes or negative weight edges.

---

### **Uploading to GitHub**
1. **Setup GitHub Repo**:
   - Create a repository on GitHub (e.g., `Graph-Algorithms`).
   - Clone the repo locally:  
     `git clone <repo_url>`

2. **Organize Files**:
   - Create a directory structure like this:
     ```
     ├── dijkstra.py
     ├── bellman_ford.py
     ├── floyd_warshall.py
     ├── README.md
     ```
