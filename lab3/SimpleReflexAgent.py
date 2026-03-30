#goal based agent
import random

#surroundings and sensors
class Enviornment:
    def __init__(self, heat_level=None):
        if heat_level is None:
            self.heat_level = random.choice(["hot", "cold"])
        else:
            self.heat_level = heat_level

    def getPercept(self):
        self.heat_level = random.choice(["hot", "cold"])
        return self.heat_level

#the agent that have a bunch of inbuilt tasks
class Simple_Agent:
    def __init__(self):
        pass
    def act(self, percept):
        if percept == "hot":
            return "pull away hand"
        else:
            return "safe"

def run_agent(agent, env):
    percept = env.getPercept()
    action = agent.act(percept)
    print(f"percept: {percept}, action: {action}")

agent = Simple_Agent()
env = Enviornment()

choice = ""

while choice.upper() != "N":
    run_agent(agent, env)
    choice = input("would you like to run again? (Y/N)")
    while choice.upper() != "N" and choice.upper() != "Y":
        choice = input("Please enter Y for yes and N for no")


print("simulation ended")
