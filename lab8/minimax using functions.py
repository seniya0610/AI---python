# ── The Board ────────────────────────────────────────────────
board = [None] * 9   

def print_board():
    symbols = []
    for i,v in enumerate(board):
        if v:
            symbols.append(v)
        else:
            symbols.append(str(i))
    for row in [symbols[0:3], symbols[3:6], symbols[6:9]]:
        print(" | ".join(row))
    print()

def get_legal_moves():
    return [i for i, v in enumerate(board) if v is None]

def check_winner():
    lines = [
        [0,1,2],[3,4,5],[6,7,8],   # rows
        [0,3,6],[1,4,7],[2,5,8],   # cols
        [0,4,8],[2,4,6]            # diagonals
    ]
    for a, b, c in lines:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

# ── Minimax ──────────────────────────────────────────────────
def minimax(is_maximizing):
    winner = check_winner()
    if winner == "X": return  1    # AI wins
    if winner == "O": return -1    # human wins
    if not get_legal_moves(): return 0  # draw

    if is_maximizing:
        best = float("-inf")
        for move in get_legal_moves():
            board[move] = "X"                        # try move
            best = max(best, minimax(False))         # recurse
            board[move] = None                       # undo move
        return best
    else:
        best = float("inf")
        for move in get_legal_moves():
            board[move] = "O"
            best = min(best, minimax(True))
            board[move] = None
        return best

def best_move():
    best_score = float("-inf")
    result = None
    for move in get_legal_moves():
        board[move] = "X"
        score = minimax(False)
        board[move] = None
        if score > best_score:
            best_score = score
            result = move
    return result

# ── Game Loop ────────────────────────────────────────────────
print("Board positions:")
print_board()

while True:
    # human move
    human = int(input("Your move (0-8): "))
    if board[human] is not None:
        print("Cell taken, try again")
        continue
    board[human] = "O"
    print_board()

    if check_winner() or not get_legal_moves():
        break

    # AI move
    ai = best_move()
    board[ai] = "X"
    print(f"AI plays at {ai}")
    print_board()

    if check_winner() or not get_legal_moves():
        break

# result
winner = check_winner()
if winner: print(f"{winner} wins!")
else: print("Draw!")
