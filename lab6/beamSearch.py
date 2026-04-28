import random

# --- Environment ---
class Environment:
    def __init__(self):
        self.graph = {
            'A': [('B', 4),  ('C', 3),  ('D', 7)],
            'B': [('E', 12), ('F', 5)],
            'C': [('G', 6),  ('H', 4)],
            'D': [('I', 3),  ('J', 8)],
            'E': [('K', 5)],
            'F': [('K', 9),  ('L', 7)],
            'G': [('L', 4),  ('M', 6)],
            'H': [('M', 3),  ('N', 5)],
            'I': [('N', 7),  ('O', 2)],
            'J': [('O', 4)],
            'K': [],
            'L': [],
            'M': [],
            'N': [],
            'O': []
        }
        self.heuristic = {
            'A': 15, 'B': 12, 'C': 11, 'D': 13,
            'E': 8,  'F': 7,  'G': 6,  'H': 5,
            'I': 4,  'J': 9,  'K': 3,  'L': 2,
            'M': 3,  'N': 2,  'O': 0
        }

    def get_neighbors(self, node):
        return self.graph[node]

    def get_heuristic(self, node):
        return self.heuristic[node]


# --- Agent ---
class LocalBeamAgent:
    def __init__(self, environment):
        self.env = environment
        self.beam_width     = 2   # start small
        self.max_beam_width = 5   # never go beyond this
        self.levels_without_progress = 0
        self.expand_after   = 3   # widen beam if stuck for 3 levels

    def search(self, start, goal):
        # each state = (heuristic, node, path, cost)
        beam = [(self.env.get_heuristic(start), start, [start], 0)]
        visited = []
        level = 0
        best_h_so_far = self.env.get_heuristic(start)

        while beam:
            level += 1
            print(f"\n--- Level {level} | Beam Width: {self.beam_width} ---")
            print(f"Beam nodes: {[node for _, node, _, _ in beam]}")

            # --- check if goal is in current beam ---
            for h, node, path, cost in beam:
                if node == goal:
                    print(f"\nGoal found!")
                    print(f"Path: {' -> '.join(path)}")
                    print(f"Total cost: {cost}")
                    return path, cost

            # --- expand all nodes in the beam ---
            all_neighbors = []
            for h, node, path, cost in beam:
                if node in visited:
                    continue
                visited.append(node)

                for neighbor, edge_cost in self.env.get_neighbors(node):
                    if neighbor not in visited:
                        new_cost = cost + edge_cost
                        new_h    = self.env.get_heuristic(neighbor)
                        all_neighbors.append((new_h, neighbor, path + [neighbor], new_cost))

            if not all_neighbors:
                print("No more nodes to expand.")
                break

            # --- sort by heuristic, keep only beam_width best ---
            all_neighbors.sort(key=lambda x: x[0])
            beam = all_neighbors[:self.beam_width]

            # --- check if we're making progress ---
            current_best_h = beam[0][0]
            if current_best_h >= best_h_so_far:
                self.levels_without_progress += 1
            else:
                best_h_so_far = current_best_h
                self.levels_without_progress = 0  # reset counter, we're improving

            # --- widen beam if stuck for too long ---
            if self.levels_without_progress >= self.expand_after:
                if self.beam_width < self.max_beam_width:
                    self.beam_width += 1
                    print(f"No progress for {self.expand_after} levels — increasing beam width to {self.beam_width}")
                self.levels_without_progress = 0  # reset after widening

        print("Goal not found")
        return None, 0


# --- Run ---
def run_agent(start, goal):
    env   = Environment()
    agent = LocalBeamAgent(env)
    agent.search(start, goal)


run_agent('A', 'O')
