#BFS Goal Based Agent

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

    def get_neighbours(self, alpha):
        neighbours = self.tree[alpha]
        return neighbours

    def get_percept(self, node):
        return node

class BFSgoalbasedagent:
    def __init__(self, target):
        self.goal = target
        pass

    def formulateGoal(self, percept):
        if percept == self.goal:
            return True

        else:
            return False

    def BFSact(self, env, start):
        visited = [] #to check visited nodes
        queue = [] #queue

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
    env = Enviornment(alphabetTree)

    target = input("Enter letter to find: ").upper()
    agent = BFSgoalbasedagent(target)

    result = agent.BFSact(env, 'A')
    if result == "not found":
        print("not found")
    else:
        print("found")

runAgent()

