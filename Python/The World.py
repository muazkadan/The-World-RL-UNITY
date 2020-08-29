import socket
import random
import matplotlib.pyplot as plt

import numpy as np

actions = ["U", "D", "L", "R"]

states = ["(1 1)", "(1 2)", "(1 3)", "(1 4)",
          "(2 1)", "(2 2)", "(2 3)", "(2 4)",
          "(3 1)", "(3 2)", "(3 3)", "(3 4)"]

q_table = np.zeros([len(states), len(actions)])

# Hyperparameter
# gamma = 0.95
gamma = 1
alpha = 0.9
epsilon = 0.15


def start():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket.setdefaulttimeout(None)
    s.bind(('127.0.0.1', 60000))
    s.listen(50)

    # Plotting Metrix
    reward_list = []

    episode_number = 200
    for i in range(1, episode_number):
        state = "(1 1)"
        reward_count = 0
        while True:
            c, addr = s.accept()  # when port connected
            bytes_received = c.recv(4000)  # received bytes
            state_received = str(bytes_received, 'utf-8')

            if random.uniform(0, 1) < epsilon:
                action = random.randrange(len(actions))
            else:
                action = np.argmax(q_table[states.index(state)])

            next_state, reward, done = state_received.split(",")
            

            old_value = q_table[states.index(state), action]  # old_value
            next_max = np.max(q_table[states.index(next_state)])  # next_max

            next_value = (1 - alpha) * old_value + alpha * (float(reward) + gamma * next_max)

            # Q table update
            q_table[states.index(state), action] = next_value

            # update state
            state = next_state

            reward_count += float(reward)

            c.sendall(str.encode(actions[action]))  # sending back
            c.close()
            if done == " True":
                break

        if i % 1 == 0:
            reward_list.append(reward_count)
            print("Episode: {}, reward {}".format(i, reward_count))

    print(q_table)

    fig, axs = plt.subplots(1, 1)
    axs.plot(reward_list)
    axs.set_xlabel("episode")
    axs.set_ylabel("reward")

    axs.grid(True)
    axs.grid(True)

    plt.show()


start()
