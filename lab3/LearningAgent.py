import random

class Environment:
    def __init__(self):
        # 3x3 Grid
        self.grid = ["Clean", "Dirty", "Dirty",
                     "Dirty", "Clean", "Clean",
                     "Clean", "Dirty", "Clean"]

    def get_percept(self, position):
        return self.grid[position]

    def clean_room(self, position):
        if self.grid[position] == "Dirty":
            self.grid[position] = "Clean"
            return 10  # Reward for cleaning
        return -5  # Penalty for cleaning an already clean room

    def move_reward(self):
        return -1  # Small cost for moving (energy)

    def display_grid(self):
        print("--- Current Grid ---")
        for i in range(len(self.grid)):
            print(f"{self.grid[i]:<6}", end="|")
            if (i + 1) % 3 == 0: print()
        print("--------------------")


class LearningBasedAgent:
    def __init__(self, actions):
        self.position = 0
        self.actions = actions
        self.Q = {}
        self.lr = 0.1  # Learning Rate (Your 'Overrider')
        self.exploration = 0.2
        self.discount = 0.9

    def get_Q_value(self, state, action):
        # Checks internal memory for this specific state/action pair
        return self.Q.get((state, action), 0.0)

    def select_action(self, state):
        # Epsilon-Greedy: Decide to explore or use memory
        if random.uniform(0, 1) < self.exploration:
            return random.choice(self.actions)
        else:
            # Use lambda to find the action with the highest Q-value
            return max(self.actions, key=lambda a: self.get_Q_value(state, a))

    def learn(self, state, action, reward, next_state):
        # Bellman Equation update
        old_Q = self.get_Q_value(state, action)

        # Look at the next state and find the best potential future reward
        best_future_Q = max([self.get_Q_value(next_state, a) for a in self.actions])

        # Calculate new knowledge
        new_Q = old_Q + self.lr * (reward + self.discount * best_future_Q - old_Q)
        self.Q[(state, action)] = new_Q

    def move(self):
        self.position = (self.position + 1) % 9


def runAgent(agent, env, total_steps=50):
    for step in range(total_steps):
        # 1. PERCEIVE: What is the state of the current room?
        state = env.get_percept(agent.position)

        # 2. ACT: Agent decides based on the state
        action = agent.select_action(state)

        # 3. RESPOND: Environment gives reward based on action
        if action == "Clean":
            reward = env.clean_room(agent.position)
            next_state = env.get_percept(agent.position)  # Will be 'Clean' now
        else:  # Action is "Move"
            reward = env.move_reward()
            agent.move()
            next_state = env.get_percept(agent.position)  # State of the NEW room

        # 4. LEARN: Agent updates Q-Table
        agent.learn(state, action, reward, next_state)

        if "Dirty" not in env.grid:
            print(f"Step {step}: All rooms cleaned!")
            break


# --- Execution ---
actions = ["Clean", "Move"]
env = Environment()
agent = LearningBasedAgent(actions)

print("Initial State:")
env.display_grid()

runAgent(agent, env)

print("\nFinal State:")
env.display_grid()

print("\nLearned Q-Table (Memory):")
for key, val in agent.Q.items():
    print(f"State: {key[0]} | Action: {key[1]:<5} | Value: {val:.2f}")
