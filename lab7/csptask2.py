from ortools.sat.python import cp_model

model = cp_model.CpModel()

monday = model.new_int_var(0,4,"monday")
tuesday = model.new_int_var(0,4,"tuesday")
wednesday = model.new_int_var(0,4,"wednesday")
thursday = model.new_int_var(0,4,"thursday")
friday = model.new_int_var(0,4,"friday")

# Constraints
# 0: SQ1
# 1: SQ2
# 2: SP1
# 3: SP2
# 4: SP4

model.add(monday >= 2)
model.add(thursday >= 2)
model.add(friday <= 1)

model.add_all_different([monday, tuesday, wednesday, thursday, friday])

#solve
solver = cp_model.CpSolver()
status = solver.solve(model)

outfit_name = {0: "ShalwarQameez1", 1: "ShalwarQameez2", 2: "ShirtPant1", 3: "ShirtPant2", 4: "ShirtPant3"}

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("Monday:   ", outfit_name[solver.value(monday)])
    print("Tuesday: ", outfit_name[solver.value(tuesday)])
    print("Wednesday: ", outfit_name[solver.value(wednesday)])
    print("Thursday: ", outfit_name[solver.value(thursday)])
    print("Friday: ", outfit_name[solver.value(friday)])
