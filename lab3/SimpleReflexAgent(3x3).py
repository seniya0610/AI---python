#simple reflex agent with 3x3 grid

class Enviornment:
    def __init__(self):
        self.grid = ["Clean", "Dirty", "Dirty",
                     "Dirty", "CLean", "Clean",
                     "Clean", "Dirty", "Clean"]

    def get_percept(self, position):
        return self.grid[position]

    def cleanRoom(self, position):
        self.grid[position] = "clean"

    def displayGrid(self):
        for i in range(len(self.grid)):
            print(self.grid[i], end="|")
            if (i + 1) % 3 == 0:
                print()

class SimpleReflexAgent:
    def __init__(self):
        self.position = 0
        pass

    def act(self, percept, grid):
        if percept == "Dirty":
            print("Clean the room")
            grid[self.position] = "Clean"
            return "Cleaned"
        else:
            return "room is clean"

    def move(self):
        if self.position < 8:
            self.position = self.position + 1
        else:
            self.position = 0
        return self.position

def runAgent(env, agent, steps):
    for i in range(steps):
        percept = env.get_percept(agent.position)
        action = agent.act(percept, env.grid)
        print(f"Step {steps + 1}: Position {agent.position} -> Percept - {percept}, Action - {action}")
        env.displayGrid()

        if percept == "Dirty":
            env.cleanRoom(agent.position)

        agent.move()

agent = SimpleReflexAgent()
env = Enviornment()
steps = int(input("enter steps of the vaccum: "))
runAgent(env, agent, steps)
