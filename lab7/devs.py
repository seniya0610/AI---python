from ortools.sat.python import cp_model

model = cp_model.CpModel()

#make variables
dev1 = model.new_int_var(0, 5, "Dev1")
dev2 = model.new_int_var(0, 5, "Dev2")
dev3 = model.new_int_var(0, 5, "Dev3")
dev4 = model.new_int_var(0, 5, "Dev4")
dev5 = model.new_int_var(0, 5, "Dev5")
dev6 = model.new_int_var(0, 5, "Dev6")

devs = [dev1, dev2, dev3, dev4, dev5, dev6]

#constraints
model.add_all_different(devs)

model.add(dev2 != 4)
model.add(dev1 != 0)

b = model.new_bool_var("condition")
model.add(dev1 == 3).only_enforce_if(b)
model.add(dev1 != 3).only_enforce_if(b.Not())
model.add(dev2 != 5).only_enforce_if(b)
model.add(dev2 == 5).only_enforce_if(b.Not())

solver = cp_model.CpSolver()
status = solver.Solve(model)

modules = {0:"AI", 1:"Web", 2:"Mobile", 3:"Cloud", 4:"Security", 5:"Testing"}

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("Optimal solution:")
    for i, dev in enumerate(devs):
        print(f"Developer{i+1}: {modules[solver.Value(dev)]}")
