#DFS Goal Based Agent

alphabetTree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': ['P', 'Q'],
    'I': ['R', 'S'],
    'J': ['T', 'U'],
    'K': ['V', 'W'],
    'L': ['X', 'Y'],
    'M': ['Z', None],
    'N': [None, None],
    'O': [None, None],
    'P': [None, None],
    'Q': [None, None],
    'R': [None, None],
    'S': [None, None],
    'T': [None, None],
    'U': [None, None],
    'V': [None, None],
    'W': [None, None],
    'X': [None, None],
    'Y': [None, None],
    'Z': [None, None]
}

class Enviornment:
    def __init__(self, tree):
        self.tree = tree
        pass

    def get_neighbours(self, node):
        neighbours = self.tree[node]
        return neighbours

    def get_percept(self, node):
        return node
        pass

class DfsAgent:
    def __init__(self, target):
        self.goal = target
        pass

    def is_goal(self, percept):
        if percept == self.goal:
            return True
        else:
            return False

    def DFSact(self, start, env):
        visited = []
        stack = []

        visited.append(start)
        stack.append(start)

        while stack:
            node = stack.pop()
            print(f"DFS Visiting: {node}")

            if self.is_goal(node):
                return "found"

            for neighbours in env.get_neighbours(node):
                if neighbours is not None and neighbours not in visited:
                    visited.append(neighbours)
                    stack.append(neighbours)

        return "not found"

def runAgent():
    env = Enviornment(alphabetTree)
    target = input("enter the node to find: ").upper()
    agent = DfsAgent(target)

    start = env.get_percept('A')
    result = agent.DFSact(start, env)
    print(f"{result}")

runAgent()
