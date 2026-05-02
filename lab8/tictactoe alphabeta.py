board = [None] * 9

def print_board():
    symbols = [v if v else str(i) for i, v in enumerate(board)]
    for row in [symbols[0:3], symbols[3:6], symbols[6:9]]:
        print(" | ".join(row))
    print()

def get_legal_moves():
    return [i for i, v in enumerate(board) if v is None]

def check_winner():
    lines = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for a, b, c in lines:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None


# ── Minimax with Alpha-Beta Pruning ──────────────

# alpha = best score the MAXIMIZER (AI) is guaranteed so far
# beta  = best score the MINIMIZER (human) is guaranteed so far
#
# The idea:
#   if the minimizer finds a score LOWER than alpha → maximizer will never pick this branch → PRUNE
#   if the maximizer finds a score HIGHER than beta  → minimizer will never pick this branch → PRUNE

def minimax(is_maximizing, alpha, beta):
    winner = check_winner()
    if winner == "X": return  1
    if winner == "O": return -1
    if not get_legal_moves(): return 0

    if is_maximizing:
        best = float("-inf")
        for move in get_legal_moves():
            board[move] = "X"
            score = minimax(False, alpha, beta)
            board[move] = None

            best = max(best, score)
            alpha = max(alpha, best)    # update best guaranteed score for maximizer

            if beta <= alpha:           # minimizer won't allow this branch → stop
                break                   # ← this is the PRUNE

        return best

    else:
        best = float("inf")
        for move in get_legal_moves():
            board[move] = "O"
            score = minimax(True, alpha, beta)
            board[move] = None

            best = min(best, score)
            beta = min(beta, best)      # update best guaranteed score for minimizer

            if beta <= alpha:           # maximizer won't allow this branch → stop
                break                   # ← this is the PRUNE

        return best


def best_move():
    best_score = float("-inf")
    result = None
    for move in get_legal_moves():
        board[move] = "X"
        score = minimax(False, float("-inf"), float("inf"))  # alpha starts at -inf, beta at +inf
        board[move] = None
        if score > best_score:
            best_score = score
            result = move
    return result


# ── Game Loop ─────────────────────────────────────

print_board()

while True:
    human = int(input("Your move (0-8): "))
    if board[human] is not None:
        print("Cell taken, try again")
        continue

    board[human] = "O"
    print_board()

    if check_winner() or not get_legal_moves():
        break

    ai = best_move()
    board[ai] = "X"
    print(f"AI plays at {ai}")
    print_board()

    if check_winner() or not get_legal_moves():
        break

winner = check_winner()
if winner: print(f"{winner} wins!")
else: print("Draw!")
