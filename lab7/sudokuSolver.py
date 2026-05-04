from ortools.sat.python import cp_model

model = cp_model.CpModel()

# variables

puzzle = [
    [0, 0, 6, 2, 0, 5],
    [0, 0, 0, 4, 6, 0],
    [0, 1, 2, 0, 0, 0],
    [5, 6, 0, 0, 0, 4],
    [0, 0, 4, 3, 0, 2],
    [3, 0, 0, 5, 0, 6],
]
cell = [[None] * 6 for _ in range(6)]
for r in range(6):
    row = []
    for c in range(6):
        cell[r][c] = model.new_int_var(1, 6, f"cell_row{r}_col{c}")

# constraints
for r in range(6):
    for c in range(6):
        if puzzle[r][c] != 0:
            model.add(cell[r][c] == puzzle[r][c])

for r in range(6):
    model.add_all_different(cell[r])

for c in range(6):
    model.add_all_different([cell[r][c] for r in range(6)])

for r in range(0, 6, 2):
    for c in range(0, 6, 3):
        model.add_all_different([cell[r][c], cell[r][c+1], cell[r][c+2],
                                 cell[r+1][c], cell[r+1][c+1], cell[r+1][c+2]])

solver = cp_model.CpSolver()
status = solver.solve(model)
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("Solved Sudoku:")
    for r in range(6):
        row_values = []
        for c in range(6):
            row_values.append(solver.value(cell[r][c]))
        print(row_values)
else:
    print("No solution found.")
