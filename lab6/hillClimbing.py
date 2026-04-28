import random


# --- Environment ---
class Environment:
    def __init__(self):
        self.n = 5  # 5 queens on a 5x5 board

    def calculate_conflicts(self, board):
        conflicts = 0

        for i in range(self.n):
            for j in range(i + 1, self.n):

                # same row
                if board[i] == board[j]:
                    conflicts += 1

                # same diagonal
                if abs(board[i] - board[j]) == abs(i - j):
                    conflicts += 1

        return conflicts


# --- Agent ---
class HillClimbingAgent:
    def __init__(self, environment):
        self.env = environment

    def create_board(self):
        # each index = column, value = row the queen is placed in
        # e.g [2, 4, 1, 3, 0] means queen in col0 is at row2, col1 at row4 etc
        board = list(range(self.env.n))
        random.shuffle(board)
        return board

    def get_neighbors(self, board):
        neighbors = []

        # move one queen at a time to a different row in its column
        for col in range(self.env.n):
            for row in range(self.env.n):
                if board[col] != row:
                    neighbor = board[:]       # copy current board
                    neighbor[col] = row       # move queen to new row
                    neighbors.append(neighbor)

        return neighbors

    def climb(self):
        board = self.create_board()
        current_conflicts = self.env.calculate_conflicts(board)

        print(f"Starting board: {board} | Conflicts: {current_conflicts}")

        steps = 0
        while True:
            neighbors = self.get_neighbors(board)

            # find the neighbor with the least conflicts
            best_neighbor = min(neighbors, key=lambda b: self.env.calculate_conflicts(b))
            best_conflicts = self.env.calculate_conflicts(best_neighbor)

            # if no neighbor is better, we're stuck (local maximum)
            if best_conflicts >= current_conflicts:
                print(f"\nStuck at step {steps} | Conflicts: {current_conflicts}")
                break

            # otherwise move to the better neighbor
            board = best_neighbor
            current_conflicts = best_conflicts
            steps += 1

            if current_conflicts == 0:
                print(f"\nSolved at step {steps}!")
                break

        return board, current_conflicts


# --- Run ---
def run_agent():
    env = Environment()
    agent = HillClimbingAgent(env)
    board, conflicts = agent.climb()


run_agent()
