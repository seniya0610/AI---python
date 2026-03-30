#simple reflex agent with 3x3 grid

class Enviornment:
    def __init__(self):
        self.grid = ["Clean", "Dirty", "Dirty",
                     "Dirty", "CLean", "Clean",
                     "Clean", "Dirty", "Clean"]

    def get_percept(self, position):
        return self.grid[position]

    def cleanRoom(self, position):
        self.grid[position] = "Clean"

    def displayGrid(self):
        for i in range(len(self.grid)):
            print(self.grid[i], end="|")
            if (i + 1) % 3 == 0:
                print()

class ModelBasedAgent:
    def __init__(self):
        self.position = 0
        self.internalmap = ["Unknown", "Unknown", "Unknown",
                            "Unknown", "Unknown", "Unknown",
                            "Unknown", "Unknown", "Unknown"]
        pass

    def update_model(self, percept):
        self.internalmap[self.position] = percept

    def act(self):
        if self.internalmap[self.position] == "Dirty":
            print("Clean the room")
            return "Clean"
        else:
            return "Move"

    def move(self):
        if self.position < 8:
            self.position = self.position + 1
        else:
            self.position = 0
        return self.position

def runAgent(env, agent, steps):
    for i in range(steps):
        percept = env.get_percept(agent.position)
        agent.update_model(percept) #model percepts first before taking action
        action = agent.act()

        if action == "Clean":
            print(f"Action: Cleaning Position {agent.position}")
            env.cleanRoom(agent.position) #updates original model
            agent.update_model("Clean") #updates the model the agent has
            env.displayGrid()
        else:
            print(f"Action: Position {agent.position} is already clean. Moving...")
            agent.move()


agent = ModelBasedAgent()
env = Enviornment()
steps = int(input("enter steps of the vaccum: "))
runAgent(env, agent, steps)
