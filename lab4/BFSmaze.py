maze = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]
# 0 = open, 1 = wall

class Enviornment:
    def __init__(self, grid):
        self.tree = grid  # kept as self.tree so nothing else breaks

    def get_neighbours(self, node):
        row, col = node

        up    = (row - 1, col)
        down  = (row + 1, col)
        left  = (row, col - 1)
        right = (row, col + 1)

        possible = [up, down, left, right]

        neighbours = []
        for r, c in possible:
            in_bounds  = 0 <= r < len(self.tree) and 0 <= c < len(self.tree[0])
            if in_bounds:
                not_a_wall = self.tree[r][c] == 0
                if not_a_wall:
                    neighbours.append((r, c))
        return neighbours

    def get_percept(self, node):
        return node


class BFSgoalbasedagent:
    def __init__(self, target):
        self.goal = target

    def formulateGoal(self, percept):
        if percept == self.goal:
            return True
        else:
            return False

    def BFSact(self, env, start):
        visited = []
        queue   = []

        visited.append(start)
        queue.append(start)

        while queue:
            node = queue.pop(0)
            print(f"Visiting: {node}")

            if self.formulateGoal(node):
                return "found"

            for neighbour in env.get_neighbours(node):
                if neighbour is not None and neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

        return "not found"


def runAgent():
    env    = Enviornment(maze)
    target = (4, 4)              # bottom right cell as goal
    agent  = BFSgoalbasedagent(target)

    start  = env.get_percept((0, 0))   # top left cell as start
    result = agent.BFSact(env, start)

    if result == "not found":
        print("No path found!")
    else:
        print(f"Found the goal {target}!")

runAgent()