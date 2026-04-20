graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

def ucs(graph, start, goal):
    frontier = [(0, start, [start])]
    visited = []

    while frontier:
        frontier.sort(key=lambda x: x[0])
        cost, node, path = frontier.pop(0)

        if node in visited:
            continue

        visited.append(node)
        print(f"Visiting: {node} | Cost: {cost}")

        if node == goal:
            print(f"\nPath: {' -> '.join(path)}")
            print(f"Total Cost: {cost}")
            return

        for neighbour, edge_cost in graph[node].items():
            if neighbour not in visited:
                frontier.append((cost + edge_cost, neighbour, path + [neighbour]))

    print("Goal not found")

ucs(graph, 'A', 'I')