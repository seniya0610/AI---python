# The tree as a dictionary:
# Key   = node name
# Value = list of children (either node names or leaf integers)
#
#         A (Max)
#        / \
#     B(Min) C(Min)
#     / \     / \
#  D(Max) E(Max) F(Max) G(Max)
#  /\     /\     /\      /\
# 3  5   6  9   1  2    0  -1

TREE = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [3, 5],
    "E": [6, 9],
    "F": [1, 2],
    "G": [0, -1],
}

# Which nodes are Max and which are Min
NODE_TYPE = {
    "A": "Max",
    "B": "Min",
    "C": "Min",
    "D": "Max",
    "E": "Max",
    "F": "Max",
    "G": "Max",
}


# ── Environment ────────────────────────────────
# Knows the tree structure
# Answers questions like: "what are the children of this node?"

class Environment:
    def __init__(self, tree, node_type):
        self.tree = tree          # the full tree dictionary
        self.node_type = node_type

    def get_children(self, node):
        return self.tree[node]

    def is_leaf(self, node):
        return isinstance(node, int)

    def is_maximizing(self, node):
        return self.node_type[node] == "Max"

class Agent:
    def __init__(self, env):
        self.env = env
        self.pruned = []     # keeps track of what got pruned (for printing)

    def minimax(self, node, alpha, beta):
        # Base case: if this node is a leaf (an integer), just return it
        if self.env.is_leaf(node):
            return node

        children = self.env.get_children(node)

        if self.env.is_maximizing(node):
            best = float("-inf")

            for child in children:
                score = self.minimax(child, alpha, beta)    # recurse
                best  = max(best, score)
                alpha = max(alpha, best)

                # Prune: if beta <= alpha, minimizer above will never allow this
                if beta <= alpha:
                    # find remaining children we are skipping
                    remaining = children[children.index(child) + 1:]
                    if remaining:
                        self.pruned.append((node, remaining))
                    break

            return best

        else:  # minimizing
            best = float("inf")

            for child in children:
                score = self.minimax(child, alpha, beta)    # recurse
                best  = min(best, score)
                beta  = min(beta, best)

                # Prune: if beta <= alpha, maximizer above will never allow this
                if beta <= alpha:
                    remaining = children[children.index(child) + 1:]
                    if remaining:
                        self.pruned.append((node, remaining))
                    break

            return best

    def best_move(self, root):
        # Try each child of the root and pick the one with the highest score
        best_score = float("-inf")
        best_child = None
        alpha = float("-inf")
        beta  = float("inf")

        for child in self.env.get_children(root):
            score = self.minimax(child, alpha, beta)
            if score > best_score:
                best_score = score
                best_child = child
            alpha = max(alpha, best_score)

        return best_child, best_score

def runAgent():
    env   = Environment(TREE, NODE_TYPE)
    agent = Agent(env)

    best_child, best_score = agent.best_move("A")

# ── Run ─────────────────────────────────────────
runAgent()
