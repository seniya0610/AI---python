import random

# --- Environment ---
class Environment:
    def __init__(self):
        self.num_trucks   = 3
        self.truck_capacity = 50
        self.depot        = 0

        self.locations = {
            0: (0, 0),   # depot
            1: (2, 4),
            2: (5, 3),
            3: (7, 1),
            4: (1, 6),
            5: (8, 5),
            6: (3, 7),
            7: (6, 2),
            8: (4, 8),
            9: (9, 3)
        }

        self.demands = {
            0: 0,
            1: 8, 2: 5, 3: 10,
            4: 6, 5: 8, 6: 7,
            7: 9, 8: 4, 9: 6
        }

    def get_distance(self, a, b):
        x1, y1 = self.locations[a]
        x2, y2 = self.locations[b]
        return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)

    def calculate_fitness(self, schedule):
        penalty   = 0
        total_distance = 0

        for route in schedule:
            if not route:
                continue

            # constraint 1: truck over capacity
            load = sum(self.demands[stop] for stop in route)
            if load > self.truck_capacity:
                penalty += (load - self.truck_capacity) * 10

            # distance: depot -> stops -> depot
            total_distance += self.get_distance(self.depot, route[0])
            for i in range(len(route) - 1):
                total_distance += self.get_distance(route[i], route[i + 1])
            total_distance += self.get_distance(route[-1], self.depot)

        return round(total_distance + penalty, 2)  # lower = better

    def is_valid(self, schedule):
        for route in schedule:
            load = sum(self.demands[stop] for stop in route)
            if load > self.truck_capacity:
                return False
        return True


# --- Agent ---
class GeneticAgent:
    def __init__(self, environment):
        self.env            = environment
        self.population_size = 20
        self.generations    = 200
        self.mutation_rate  = 0.1

    def create_schedule(self):
        # all stops except depot
        stops = [s for s in self.env.locations.keys() if s != self.env.depot]
        random.shuffle(stops)

        # split stops across trucks
        schedule = [[] for _ in range(self.env.num_trucks)]
        for i, stop in enumerate(stops):
            schedule[i % self.env.num_trucks].append(stop)
        return schedule

    def create_population(self):
        return [self.create_schedule() for _ in range(self.population_size)]

    def fitness(self, schedule):
        return self.env.calculate_fitness(schedule)

    def select_parents(self, population):
        sample = random.sample(population, 4)
        sample.sort(key=lambda s: self.fitness(s))  # lower = better
        return sample[0], sample[1]

    def crossover(self, parent1, parent2):
        # flatten both into one stop list
        flat1 = [stop for route in parent1 for stop in route]
        flat2 = [stop for route in parent2 for stop in route]

        # slice from parent1, fill rest from parent2
        split = random.randint(1, len(flat1) - 1)
        child_flat = flat1[:split]
        for stop in flat2:
            if stop not in child_flat:
                child_flat.append(stop)

        # split back into truck routes
        child = [[] for _ in range(self.env.num_trucks)]
        for i, stop in enumerate(child_flat):
            child[i % self.env.num_trucks].append(stop)
        return child

    def mutate(self, schedule):
        if random.uniform(0, 1) < self.mutation_rate:
            # pick two trucks and swap one stop between them
            t1, t2 = random.sample(range(self.env.num_trucks), 2)
            if schedule[t1] and schedule[t2]:
                i = random.randint(0, len(schedule[t1]) - 1)
                j = random.randint(0, len(schedule[t2]) - 1)
                schedule[t1][i], schedule[t2][j] = schedule[t2][j], schedule[t1][i]
        return schedule

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
                best = min(population, key=lambda s: self.fitness(s))

        return min(population, key=lambda s: self.fitness(s))


# --- Run ---
def run_agent():
    env   = Environment()
    agent = GeneticAgent(env)

    best_schedule = agent.evolve()

run_agent()
