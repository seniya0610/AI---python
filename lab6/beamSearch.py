class Environment:
    def __init__(self):
        self.graph = {
            'A': [['B', 4], ['C', 3]],
            'B': [['E', 12], ['F', 5]],
            'C': [['D', 7], ['E', 10]],
            'D': [['E', 2]],
            'E': [['G', 5]],
            'F': [['G', 16]],
            'G': []
        }
        self.heuristic = {
            'A': 14, 'B': 12, 'C': 11,
            'D': 6,  'E': 4,  'F': 11, 'G': 0
        }

    def get_neighbors(self, node):
        return self.graph[node]

    def get_heuristic(self, node):
        return self.heuristic[node]


class BeamSearchAgent:
    def __init__(self, environment, beam_width=2):
        self.env        = environment
        self.beam_width = beam_width

    def search(self, start, goal):
        # beam holds multiple states at once instead of just one
        # each state = (heuristic, node, path, cost)
        beam    = [(self.env.get_heuristic(start), start, [start], 0)]
        visited = []

        while beam:

            # check if goal is in current beam
            for h, node, path, g in beam:
                if node == goal:
                    print(f"Path: {' -> '.join(path)}")
                    print(f"Total cost: {g}")
                    return path

            # expand every node in the beam
            all_neighbors = []
            for h, node, path, g in beam:
                if node in visited:
                    continue
                visited.append(node)

                for neighbor, edge_cost in self.env.get_neighbors(node):
                    if neighbor not in visited:
                        new_g = g + edge_cost
                        new_h = self.env.get_heuristic(neighbor)
                        all_neighbors.append((new_h, neighbor, path + [neighbor], new_g))

            # sort by heuristic, keep only the best beam_width nodes
            all_neighbors.sort()
            beam = all_neighbors[:self.beam_width]

        print("No path found")
        return None


def run_agent(start, goal):
    env   = Environment()
    agent = BeamSearchAgent(env, beam_width=2)
    agent.search(start, goal)


run_agent('A', 'G')
