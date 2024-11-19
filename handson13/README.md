Here’s a high-level overview of how to implement each algorithm with code snippets, test cases, and an outline for how to organize everything for upload to GitHub.

---

### 1. **Topological Sort**
Topological sorting applies to Directed Acyclic Graphs (DAGs) and is typically implemented using Depth-First Search (DFS).

#### Implementation (Python):
```python
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)
        stack.append(v)

    def topological_sort(self):
        visited = [False] * self.vertices
        stack = []

        for i in range(self.vertices):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        return stack[::-1]  # Reverse the stack for the correct order
```

#### Test Case:
```python
if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    result = g.topological_sort()
    print("Topological Sort:", result)
```

---

### 2. **Depth-First Search (DFS)**
DFS is a graph traversal technique.

#### Implementation (Python):
```python
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = [False] * self.vertices
        self.dfs_util(start, visited)
```

#### Test Case:
```python
if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("DFS starting from vertex 2:")
    g.dfs(2)
```

---

### 3. **Kruskal's Algorithm**
Kruskal's algorithm is used to find the Minimum Spanning Tree (MST).

#### Implementation (Python):
```python
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal(self):
        self.edges.sort()
        parent = []
        rank = []

        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        mst = []
        for weight, u, v in self.edges:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            if root_u != root_v:
                mst.append((u, v, weight))
                self.union(parent, rank, root_u, root_v)

        return mst
```

#### Test Case:
```python
if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    mst = g.kruskal()
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")
```

---

### Instructions for Uploading to GitHub
1. **Directory Structure**:
   ```
   ├── topological_sort.py
   ├── dfs.py
   ├── kruskal.py
   ├── README.md
   ```

2. **Sample `README.md`**:
   ```markdown
   # Graph Algorithms

   This repository contains Python implementations for the following algorithms:

   1. Topological Sort
   2. Depth-First Search (DFS)
   3. Kruskal's Algorithm

   ## How to Run
   Each algorithm is implemented in its respective `.py` file. Tests are included in the `tests` directory.

   Example:
   ```bash
   python3 topological_sort.py
   Topological Sort: [5, 4, 2, 3, 1, 0]
   python3 dfs.py
   DFS starting from vertex 2:
   2 0 1 3
   python3 kruskal.py
   2 -- 3 == 4
   0 -- 3 == 5
   0 -- 1 == 10
   ```

   ```

   ## Author
   Anirudh Parashar
   ```