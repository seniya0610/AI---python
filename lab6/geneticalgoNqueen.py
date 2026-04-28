import random

class Environment:
    def __init__(self):
        self.n = 8 

    def calculate_fitness(self, board):
        conflicts = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if board[i] == board[j]:              # same row
                    conflicts += 1
                if abs(board[i] - board[j]) == abs(i - j):  # same diagonal
                    conflicts += 1
        return conflicts

class GeneticAgent:
    def __init__(self, environment):
        self.env = environment
        self.population_size = 20
        self.generations = 200
        self.mutation_rate = 0.1

    def create_board(self):
        board = list(range(self.env.n))
        random.shuffle(board)
        return board

    def create_population(self):
        return [self.create_board() for _ in range(self.population_size)]

    def fitness(self, board):
        return self.env.calculate_fitness(board)

    def select_parents(self, population):
        sample = random.sample(population, 4)
        sample.sort(key=lambda b: self.fitness(b))  # lower conflicts = better
        return sample[0], sample[1]

    def crossover(self, parent1, parent2):
        # take first half from parent1, second half from parent2
        split = random.randint(1, self.env.n - 1)
        child = parent1[:split] + parent2[split:]
        return child

    def mutate(self, board):
        if random.uniform(0, 1) < self.mutation_rate:
            # swap two queens
            i, j = random.sample(range(self.env.n), 2)
            board[i], board[j] = board[j], board[i]
        return board

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

            best = min(population, key=lambda b: self.fitness(b))
            if (generation + 1) % 50 == 0:
                print(f"Generation {generation + 1} | Conflicts: {self.fitness(best)}")

            if self.fitness(best) == 0:
                print(f"\nSolved at generation {generation + 1}!")
                return best

        return min(population, key=lambda b: self.fitness(b))


# --- Run ---
def run_agent():
    env = Environment()
    agent = GeneticAgent(env)

    board, = [agent.evolve()]

run_agent()
