import random

# --- Environment ---
class Environment:
    def __init__(self):
        self.teachers = ['T1', 'T2', 'T3', 'T4', 'T5']
        self.courses  = ['C1', 'C2', 'C3', 'C4', 'C5']
        self.days     = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
        self.slots    = [1, 2, 3, 4, 5]

        # which teacher teaches which course
        self.teacher_course = {
            'C1': 'T1', 'C2': 'T2', 'C3': 'T3', 'C4': 'T4', 'C5': 'T5'
        }

    def calculate_fitness(self, timetable):
        penalty = 0
    
        # --------------------------------------------------
        # CONSTRAINT 1: teacher can't teach two classes at the same time
        # --------------------------------------------------
        for day in self.days:
            for slot in self.slots:
                teachers_this_slot = []
                for course in self.courses:
                    if timetable[day][slot] == course:
                        teacher = self.teacher_course[course]
                        if teacher in teachers_this_slot:
                            penalty += 10  # same teacher, same slot = clash
                        teachers_this_slot.append(teacher)
    
        # --------------------------------------------------
        # CONSTRAINT 2: each course must appear exactly 3 times a week
        # --------------------------------------------------
        for course in self.courses:
            count = 0
            for day in self.days:
                for slot in self.slots:
                    if timetable[day][slot] == course:
                        count += 1
            # e.g count=5 -> penalty 20, count=1 -> penalty 20
            penalty += abs(count - 3) * 10
    
        # --------------------------------------------------
        # CONSTRAINT 3: no teacher teaches more than 3 consecutive slots
        # --------------------------------------------------
        for day in self.days:
            for teacher in self.teachers:
                consecutive = 0
                for slot in self.slots:
                    cell = timetable[day][slot]
                    if cell and self.teacher_course[cell] == teacher:
                        consecutive += 1
                        if consecutive > 3:
                            penalty += 5  # 4th class in a row = bad
                    else:
                        consecutive = 0  # reset streak when teacher has a gap
    
        return penalty  # 0 = perfect timetable, higher = more violations


# --- Agent ---
class GeneticAgent:
    def __init__(self, environment):
        self.env             = environment
        self.population_size = 20
        self.generations     = 200
        self.mutation_rate   = 0.1

    def create_timetable(self):
        # chromosome: timetable[day][slot] = course or None
        timetable = {day: {slot: None for slot in self.env.slots} for day in self.env.days}

        # schedule each course exactly 3 times
        all_slots = [(day, slot) for day in self.env.days for slot in self.env.slots]
        random.shuffle(all_slots)

        slot_index = 0
        for course in self.env.courses:
            for _ in range(3):
                day, slot = all_slots[slot_index]
                timetable[day][slot] = course
                slot_index += 1

        return timetable

    def create_population(self):
        return [self.create_timetable() for _ in range(self.population_size)]

    def fitness(self, timetable):
        return self.env.calculate_fitness(timetable)

    def select_parents(self, population):
        sample = random.sample(population, 4)
        sample.sort(key=lambda t: self.fitness(t))  # lower penalty = better
        return sample[0], sample[1]

    def crossover(self, parent1, parent2):
        child = {day: {slot: None for slot in self.env.slots} for day in self.env.days}
        # take first half of week from parent1, second half from parent2
        split = random.randint(1, len(self.env.days) - 1)
        for i, day in enumerate(self.env.days):
            if i < split:
                child[day] = dict(parent1[day])
            else:
                child[day] = dict(parent2[day])
        return child

    def mutate(self, timetable):
        if random.uniform(0, 1) < self.mutation_rate:
            # swap two random cells
            day1, day2 = random.choices(self.env.days, k=2)
            slot1, slot2 = random.choices(self.env.slots, k=2)
            timetable[day1][slot1], timetable[day2][slot2] = \
                timetable[day2][slot2], timetable[day1][slot1]
        return timetable

    def evolve(self):
        population = self.create_population()

        for generation in range(self.generations):
            new_population = []
            for _ in range(self.population_size):
                parent1, parent2 = self.select_parents(population)
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_population.append(child)
            population = new_population

            if (generation + 1) % 50 == 0:
                best = min(population, key=lambda t: self.fitness(t))
                print(f"Generation {generation + 1} | Penalty: {self.fitness(best)}")

        return min(population, key=lambda t: self.fitness(t))


# --- Run ---
def run_agent():
    env   = Environment()
    agent = GeneticAgent(env)

    best_timetable = agent.evolve()

    print("\n--- Best Timetable ---")
    print(f"{'':6}", end="")
    for slot in env.slots:
        print(f"  Slot{slot}", end="")
    print()
    for day in env.days:
        print(f"{day:<6}", end="")
        for slot in env.slots:
            cell = best_timetable[day][slot] or '----'
            print(f"  {cell:<5}", end="")
        print()

    print(f"\nFinal Penalty Score: {env.calculate_fitness(best_timetable)}")
    print("(0 = perfect, higher = more constraint violations)")


run_agent()
