import random

class LearningBasedAgent:
    def __init__(self, actions):
        self.memory = {}          
        self.actions = actions
        self.learning_rate = 0.1  
        self.future_weight = 0.9  
        self.curiosity = 0.1      

    def recall(self, state, action):
        return self.memory.get((state, action), 0.0) 

    def select_action(self, state):
        if random.uniform(0, 1) < self.curiosity:
            return random.choice(self.actions)
        return max(self.actions, key=lambda a: self.recall(state, a))

    def learn(self, state, action, reward, next_state):
        current_knowledge = self.recall(state, action)
        best_next_move = max(self.recall(next_state, a) for a in self.actions)
        updated_knowledge = current_knowledge + self.learning_rate * (reward + self.future_weight * best_next_move - current_knowledge)
        self.memory[(state, action)] = updated_knowledge

    def act(self, state):
        return self.select_action(state)


class Environment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'
        return 10

    def no_action_reward(self):
        return 0


def run_agent(agent, environment, steps):
    for step in range(steps):
        current_state = environment.get_percept()
        chosen_action = agent.act(current_state)

        if chosen_action == 'Clean the room' and current_state == 'Dirty':
            points_earned = environment.clean_room()
        else:
            points_earned = environment.no_action_reward()

        print(f"Step {step + 1}: State - {current_state}, Action - {chosen_action}, Reward - {points_earned}")

        new_state = environment.get_percept()
        agent.learn(current_state, chosen_action, points_earned, new_state)


# --- Execution ---
actions = ['Clean the room', 'No action needed']
agent = LearningBasedAgent(actions)
environment = Environment(state='Dirty')

run_agent(agent, environment, 5)

print("\nFinal Learned Memory:")
for (state, action), value in agent.memory.items():
    print(f"State: {state} | Action: {action} | Value: {value:.4f}")
