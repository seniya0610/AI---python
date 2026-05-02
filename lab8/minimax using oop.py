# ── Environment ──────────────────────────────────────────────
class Environment:
    def __init__(self):
        self.board = [None] * 9   # None | "X" | "O"
        self.current_turn = "O"   # human goes first
        self.game_over = False
        self.winner = None

    def get_legal_moves(self):
        return [i for i, v in enumerate(self.board) if v is None]

    def apply_move(self, index, player):
        if self.board[index] is not None or self.game_over:
            return False
        self.board[index] = player
        self.winner = self.check_winner()
        if self.winner or all(v is not None for v in self.board):
            self.game_over = True
        else:
            self.current_turn = "O" if self.current_turn == "X" else "X"
        return True

    def check_winner(self):
        lines = [
            [0,1,2],[3,4,5],[6,7,8],  # rows
            [0,3,6],[1,4,7],[2,5,8],  # cols
            [0,4,8],[2,4,6]           # diagonals
        ]
        for a, b, c in lines:
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def clone(self):
        e = Environment()
        e.board = self.board[:]
        e.current_turn = self.current_turn
        e.game_over = self.game_over
        e.winner = self.winner
        return e

    def print_board(self):
        symbols = [v if v else str(i) for i, v in enumerate(self.board)]
        for row in [symbols[0:3], symbols[3:6], symbols[6:9]]:
            print(" | ".join(row))
        print()


# ── Minimax ──────────────────────────────────────────────────
class Minimax:
    def __init__(self, ai_player="X", human_player="O"):
        self.ai_player = ai_player
        self.human_player = human_player

    def minimax(self, env, is_maximizing):
        # Base cases
        winner = env.check_winner()
        if winner == self.ai_player:    return  1
        if winner == self.human_player: return -1
        if not env.get_legal_moves():   return  0

        if is_maximizing:
            best = float("-inf")
            for move in env.get_legal_moves():
                next_env = env.clone()
                next_env.board[move] = self.ai_player
                best = max(best, self.minimax(next_env, False))
            return best
        else:
            best = float("inf")
            for move in env.get_legal_moves():
                next_env = env.clone()
                next_env.board[move] = self.human_player
                best = min(best, self.minimax(next_env, True))
            return best

    def best_move(self, env):
        best_score = float("-inf")
        best = None
        for move in env.get_legal_moves():
            next_env = env.clone()
            next_env.board[move] = self.ai_player
            score = self.minimax(next_env, False)
            if score > best_score:
                best_score = score
                best = move
        return best


# ── runAgent ─────────────────────────────────────────────────
def runAgent(env, agent):
    """Call this after every human move. AI adapts and plays."""
    if env.game_over or env.current_turn != agent.ai_player:
        return
    move = agent.best_move(env)
    env.apply_move(move, agent.ai_player)
    print(f"AI plays at cell {move}")
    env.print_board()


# ── Play loop ────────────────────────────────────────────────
env = Environment()
agent = Minimax(ai_player="X", human_player="O")

print("Board positions:")
env.print_board()

while not env.game_over:
    try:
        human = int(input("Your move (0-8): "))
    except ValueError:
        continue

    if env.apply_move(human, "O"):
        env.print_board()
        if env.game_over:
            break
        runAgent(env, agent)

if env.winner:
    print(f"{env.winner} wins!")
else:
    print("Draw!")
