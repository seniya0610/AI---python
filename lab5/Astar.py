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


class AStarAgent:
    def __init__(self, environment):
        self.env = environment

    def search(self, start, goal):
        open_list = [(self.env.get_heuristic(start), start, [start], 0)]
        #             f=g+h                           node   path    g
        visited = []

        while open_list:
            open_list.sort()
            f, node, path, g = open_list.pop(0)

            if node in visited:
                continue
            visited.append(node)
            print(f"Visiting: {node} | Cost so far: {g}")

            if node == goal:
                print(f"Path: {' -> '.join(path)}")
                print(f"Total cost: {g}")
                return path

            for neighbor, edge_cost in self.env.get_neighbors(node):
                if neighbor not in visited:
                    new_g = g + edge_cost
                    new_f = new_g + self.env.get_heuristic(neighbor)
                    open_list.append((new_f, neighbor, path + [neighbor], new_g))

        print("No path found")
        return None


def run_agent(start, goal):
    env = Environment()
    agent = AStarAgent(env)
    agent.search(start, goal)


run_agent('A', 'G')
