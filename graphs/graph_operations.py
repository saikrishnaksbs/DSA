class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v):
        if u in self.graph and v in self.graph:
            self.graph[u].append(v)
            self.graph[v].append(u)  # For undirected graph

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for u in list(self.graph.keys()):
                if vertex in self.graph[u]:
                    self.graph[u].remove(vertex)

    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        if v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)

    def get_neighbors(self, vertex):
        return self.graph.get(vertex, [])

    def bfs(self, start):
        visited = set()
        queue = [start]
        bfs_order = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                bfs_order.append(vertex)
                queue.extend(neighbor for neighbor in self.graph[vertex] if neighbor not in visited)

        return bfs_order

    def dfs(self, start):
        visited = set()
        dfs_order = []

        def dfs_recursive(vertex):
            visited.add(vertex)
            dfs_order.append(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return dfs_order


# Example usage:
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')

print("Neighbors of A:", g.get_neighbors('A'))  # Output: ['B', 'C']
print("BFS starting from A:", g.bfs('A'))  # Output: ['A', 'B', 'C', 'D']
print("DFS starting from A:", g.dfs('A'))  # Output: ['A', 'B', 'D', 'C']
