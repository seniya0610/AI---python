import random

# The graph — each node maps to a list of [neighbor, edge_cost]
graph = {
    'S': [['A', 3], ['B', 6], ['C', 5]],
    'A': [['D', 9], ['E', 8]],
    'B': [['F', 12], ['G', 14]],
    'C': [['H', 7]],
    'H': [['I', 5], ['J', 6]],
    'I': [['K', 1], ['L', 10], ['M', 2]],
    'D': [], 'E': [], 'F': [], 'G': [],
    'J': [], 'K': [], 'L': [], 'M': []
}

def beam_search(start, goal, beam_width):

    # beam holds our current candidate paths
    # each item is [total_cost_so_far, path_as_a_list]
    # we start with cost 0 and path = just the start node
    beam = [[0, [start]]]

    while len(beam) > 0:

        # candidates = all possible next steps from every path in beam
        candidates = []

        for item in beam:
            cost = item[0]       # cost so far for this path
            path = item[1]       # the path taken so far
            current = path[-1]   # the last node in the path = where we are now

            # goal check
            if current == goal:
                print("Path:", path, "Cost:", cost)
                return

            # expand: look at all neighbors of current node
            for neighbor_info in graph[current]:
                neighbor = neighbor_info[0]   # the neighbor node name
                edge_cost = neighbor_info[1]  # cost to reach that neighbor

                new_cost = cost + edge_cost
                new_path = path + [neighbor]

                candidates.append([new_cost, new_path])

        # sort all candidates by cost (lowest first)
        candidates.sort()

        # BEAM: only keep the top k candidates, throw the rest away
        beam = candidates[:beam_width]

    print("Goal not found")

beam_search('S', 'L', beam_width=2)