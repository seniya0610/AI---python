#utility based agent

class Enviornment:
    def __init__(self):
        self.grid = ["Clean", "Dirty", "Dirty",
                     "Dirty", "Clean", "Clean",
                     "Clean", "Dirty", "Clean"]
        pass

    def get_percept(self, position):
        return self.grid[position]

    def cleanRoom(self, position):
        self.grid[position] = "Clean"

    def display_grid(self):
        for i in range(len(self.grid)):
            print(self.grid[i], end="|")
            if (i+1) % 3 == 0:
                print()

class UtilityBasedAgent:
    def __init__(self):
        self.position =0
        self.idle_val = -10
        self.move_val = -1
        self.clean_val = 50
        self.mygrid = ["Unknown", "Unknown", "Unknown",
                       "Unknown", "Unknown", "Unknown",
                       "Unknown", "Unknown", "Unknown"]
        pass

    def update_model(self, percept):
        self.mygrid[self.position] = percept

    def act(self):
        current_status = self.mygrid[self.position]

        #1. calculate the cost of cleaning
        if current_status == "Dirty":
            utility_clean = self.clean_val
        else:
            utility_clean = self.idle_val

        # 2. Calculate Utility of MOVING
        utility_move = self.move_val # Moving always costs a little

        print(f"Eval: Clean Utility={utility_clean}, Move Utility={utility_move}")

        #3. Compare the two
        if utility_clean >= utility_move:
            return "Clean"
        else:
            return "Move"

    def move(self):
        if self.position < 8:
            self.position = self.position + 1
        else:
            self.position = 0
        return self.position

def runAgent(agent, env):

    while "Dirty" in env.grid:
        percept = env.get_percept(agent.position)
        agent.update_model(percept)
        action = agent.act()

        if action == "Clean":
            env.cleanRoom(agent.position)
            agent.update_model("Clean")
            env.display_grid()
        elif action == "Move":
            print(f"Action: Position {agent.position} is already clean. Moving...")
            agent.move()
    print("Success! The environment is clean.")

env = Enviornment()
agent = UtilityBasedAgent()
runAgent(agent, env)

