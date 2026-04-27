import heapq

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

class GreedyAgent:
    def __init__(self, environment):
        self.env = environment

    def search(self, start, goal):
        open_list = [(self.env.get_heuristic(start), start, [start])]
        visited = []

        while open_list:
            open_list.sort()
            h, node, path = open_list.pop(0)

            if node in visited:
                continue
            visited.append(node)
            print(f"Visiting: {node}")

            if node == goal:
                print(f"Path: {' -> '.join(path)}")
                return path

            for neighbor, _ in self.env.get_neighbors(node):
                if neighbor not in visited:
                    open_list.append((self.env.get_heuristic(neighbor), neighbor, path + [neighbor]))

        print("No path found")
        return None


# --- Run ---
def run_agent(start, goal):
    env = Environment()
    agent = GreedyAgent(env)
    agent.search(start, goal)


run_agent('A', 'G')
