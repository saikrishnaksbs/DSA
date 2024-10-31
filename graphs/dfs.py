def dfs_iterative(graph, start):
    visited = set()
    stack = [start]  # Using a list as a stack

    while stack:
        node = stack.pop()  # Popping from the end
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Add neighbors to the stack in reverse to maintain order
            stack.extend(reversed(graph[node]))

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("\nDFS traversal (iterative):")
dfs_iterative(graph, 'A')
