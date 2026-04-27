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

def a_star(start, goal):
    open_list = [(heuristic[start], start, [start], 0)]
    #             f=g+h,           node,  path,     g
    visited = []

    while len(open_list) > 0:
        open_list.sort()             # sorts by f = g + h
        f, node, path, g = open_list.pop(0)

        if node in visited:
            continue

        visited.append(node)
        print("Visiting:", node, " cost so far:", g)

        if node == goal:
            print("Path:", path)
            print("Total cost:", g)
            return

        for pair in graph[node]:
            neighbor = pair[0]
            edge_cost = pair[1]
            if neighbor not in visited:
                new_g = g + edge_cost
                new_f = new_g + heuristic[neighbor]
                open_list.append((new_f, neighbor, path + [neighbor], new_g))

    print("No path found")

a_star('A', 'G')
