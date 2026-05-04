from ortools.sat.python import cp_model

model = cp_model.CpModel()

#make variables
#red 0, green 1, blue 2

A = model.new_int_var(0,2, "A")
B = model.new_int_var(0,2, "B")
C = model.new_int_var(0,2, "C")
D = model.new_int_var(0,2, "D")
E = model.new_int_var(0,2, "E")

#constraints

model.add(A != B)
model.add(A != E)
model.add(E != D)
model.add(D != B)
model.add(C != B)
model.add(C != D)

class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__count = 0
    def on_solution_callback(self):
        self.__count += 1
        colors = ["RED", "GREEN", "BLUE"]
        print(f"solution {self.__count}: ")
        for v in self.__variables:
            color_name = colors[self.value(v)]
            print(f"{v.name} = {color_name}")
        print()


solved = cp_model.CpSolver()
solved.parameters.enumerate_all_solutions = True
printer = SolutionPrinter([A, B, C, D, E])
solved.solve(model, printer)
