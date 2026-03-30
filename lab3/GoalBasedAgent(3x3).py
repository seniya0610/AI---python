#Goal based agent with 3x3 grid

class Enviornment:
    def __init__(self):
        self.grid = ["Clean", "Dirty", "Dirty",
                     "Dirty", "Clean", "Clean",
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

class GoalBasedAgent:
    def __init__(self):
        self.position = 0
        self.internalmap = ["Unknown", "Unknown", "Unknown",
                            "Unknown", "Unknown", "Unknown",
                            "Unknown", "Unknown", "Unknown"]
        self.goal_state = ["Clean", "Clean", "Clean",
                           "Clean", "Clean", "Clean",
                           "Clean", "Clean", "Clean"]
        pass

    def update_model(self, percept):
        self.internalmap[self.position] = percept

    def is_goal_achieved(self):
        return self.internalmap == self.goal_state

    def act(self):
        if self.is_goal_achieved():
            return "shutting down"
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

def runAgent(env, agent):
    steps = 0

    while not agent.is_goal_achieved():
        steps += 1
        percept = env.get_percept(agent.position)
        agent.update_model(percept) #model percepts first before taking action
        action = agent.act()

        if action == "Clean":
            print(f"Action: Cleaning Position {agent.position}")
            env.cleanRoom(agent.position) #updates original model
            agent.update_model("Clean") #updates the model the agent has
            env.displayGrid()
        elif action == "Move":
            print(f"Action: Position {agent.position} is already clean. Moving...")
            agent.move()
        else:
            print("shutting down")
            break

agent = GoalBasedAgent()
env = Enviornment()
runAgent(env, agent)
