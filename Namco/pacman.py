import numpy as np
from pytimedinput import timedInput

class PacMan:
    def __init__(self, map_size=10, max_time_step=100):
        # PacMan variables
        self.map_size = map_size
        self.time_step = 0
        self.max_time_step = max_time_step
        self.map = np.zeros((map_size, map_size))
        self.x = np.random.randint(0, self.map_size)
        self.y = np.random.randint(0, self.map_size)

    def reset(self):
        pass

    def step(self, action):
        done = False

        # Increasing the timestep
        self.time_step += 1

        # Terminating after max time steps
        if self.time_step > self.max_time_step:
            done = True

        return done

    def render(self):
        pass

    # Automatic stepping if no input (direction) given
    def auto_step(self, prev_action):
        a, timedOut = timedInput("Choose your next action:\n")
        if timedOut:
            done_ = env.step(action=prev_action)
        else:
            done_ = env.step(action=int(a))
            prev_action = a
        return prev_action

if __name__ == "__main__":
    # Instantiating the environment
    env = PacMan(map_size=10,
                 max_time_step=100)
    done_ = False
    # First step
    a = int(input("Choose your first action:\n"))
    state, reward, done_, info = env.step(action=a)
    prev_action = a
    while not done_:
        done_ = env.auto_step(prev_action)


