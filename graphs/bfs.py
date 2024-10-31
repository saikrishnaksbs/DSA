def bfs(graph, start):
    visited = set()
    queue = [start]  # Using a list instead of deque
    visited.add(start)

    while queue:
        node = queue.pop(0)  # Popping from the front
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS traversal:")
bfs(graph, 'A')
