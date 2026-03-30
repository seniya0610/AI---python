#basic Model Based Agent
import random

class Enviornment:
    def __init__(self):
        self.rain = random.choice(["Yes", "No"])
        if self.rain == "Yes":
            self.floor = "Wet"
        else:
            self.floor = "Dry"

    def get_percept(self, rainstat = None, floorstat = None):
        if self.rain == None:
            self.rain = random.choice(["Yes", "No"])
            if self.rain == "Yes":
                self.floor == "Wet"
            else:
                self.floor == "Dry"
        else:
            self.rain = rainstat
            self.floor = floorstat
        return self.rain

    def cleanFloor(self):
        self.floor = "Dry"
        print("AI cleaned floor")

class ModelBasedAgent:
    def __init__(self):
        self.agentRain = "No"
        self.agentfloor = "Dry"

    def act(self):
        if self.agentRain == "Yes":
            self.agentfloor == "Wet"
            return "Need to Clean"
        else:
            return "Floor is dry"

    def updateModel(self, rain):
        self.agentRain = rain
        if self.agentRain == "Yes":
            self.agentFloor = "Wet"

def runAgent(agn, env):
    percept = env.get_percept()
    agn.updateModel(percept)
    action = agn.act()
    print(f"Action: {action}")
    if action == "Need to Clean":
        env.cleanFloor()

env = Enviornment()
agn = ModelBasedAgent()
ch = ""

while ch != "N":
    runAgent(agn, env)
    ch = input("do you want to run again?(Y/N): ").upper()


