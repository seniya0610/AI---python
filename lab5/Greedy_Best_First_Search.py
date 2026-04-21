graph = {
    'A': [['B', 4], ['C', 3]],
    'B': [['E', 12], ['F', 5]],
    'C': [['D', 7], ['E', 10]],
    'D': [['E', 2]],
    'E': [['G', 5]],
    'F': [['G', 16]],
    'G': []
}

heuristic = {
    'A': 14, 'B': 12, 'C': 11,
    'D': 6,  'E': 4,  'F': 11, 'G': 0
}

def greedy_best_first(start, goal):
    open_list = [(heuristic[start], start, [start])]
    visited = []

    while len(open_list) > 0:
        open_list.sort()
        h, node, path = open_list.pop(0)

        if node in visited:
            continue

        visited.append(node)
        print("Visiting:", node)

        if node == goal:
            print("Path:", path)
            return

        for pair in graph[node]:
            neighbor = pair[0]
            if neighbor not in visited:
                open_list.append((heuristic[neighbor], neighbor, path + [neighbor]))

    print("No path found")

greedy_best_first('A', 'G')