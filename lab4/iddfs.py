class IdDfsAgent:
    def __init__(self, target):
        self.goal = target

    def is_goal(self, percept):
        return percept == self.goal

    def DLSact(self, start, env, limit):
        visited = []
        stack = [(start, 0)]

        while stack:
            node, depth = stack.pop()

            if node in visited:
                continue
            visited.append(node)

            print(f"  Visiting: {node} (depth {depth})")

            if self.is_goal(node):
                return f"Found '{node}' at depth {depth}"

            if depth < limit:
                for neighbour in env.get_neighbours(node):
                    if neighbour is not None and neighbour not in visited:
                        stack.append((neighbour, depth + 1))

        return None  # Not found at this limit, signal to go deeper

    def IDDFSact(self, start, env):
        depth_limit = 0

        while True:
            print(f"\n--- Searching with depth limit: {depth_limit} ---")
            result = self.DLSact(start, env, depth_limit)

            if result:
                return result

            depth_limit += 1


def runAgent():
    env = Environment(alphabetTree)
    target = input("Enter the node to find: ").upper()
    agent = IdDfsAgent(target)

    start = env.get_percept('A')
    result = agent.IDDFSact(start, env)
    print(f"\n{result}")

runAgent()