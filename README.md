# What is The World:
It's a Reinforcement Learning problem introduced in udacity's reinforcement learning ud600 course. The problem is very similar to The Frozen Lake problem by openAI. The main goal is to make the agent start from a specfic point in the world and find the best way that maximizes the reward that's gitting along the way to high reward. 

# World (Environment) Design:
This grid world was designed using Unity Platform. The source code of the environment isn't available for public at the moment, but feel free to contact me if you have any question related to the it. The environment _Stochastic_ which means that if you choose an action the agent will go to the direction you chose with only .8 probability, and the agent might go to a wrong direction other that oppsite one with .2 probability. E.g. if the agent chooses action up it might go to up with .8, right with .1 and left with .1 probability. There's two ways to finish the game and end the episode. The first one is to come across the green grid which gives the agent +15 reward, and the other one is to come across the red grid which gives the agent -10 reward (punishment). Every step that doesn't take the agent to a state that ends the episode gives him -0.01 reward (punishment). 

# Content of The Project
The project has 3 main folders. One contains the python code where we use Reinforcement Learning to solve the problem. Q-Learing is used in the training process but you can use whatever algorithm you want by changing the code or you can just adjust the Hyperparameters. Feel free to share your own solution of the problem in the comments. 
The other two folders contain the excutable environment for both Windows and Linux. 

![Screenshot](https://i.ibb.co/2ZFyJXJ/Screenshot-from-2020-08-29-14-29-37.png)

# How to Use
After running the version of the app that is compatible with your platform. You'll see the MainMenu which contains 2 main options. 
**Play Yourself:** You can use this option if you want to try to play in the world as the agent. You can take actions by using keyboard keys: Up, Down, Left and Right. ESC can be used to get back to the MainMenu.
**Train with Python:** This option is used to train the agent with python code. In order for you to start the training, you have to open and run the python code before choosing this option from the MainMenu. If the python code is running correctly, the agent will start learning as soon as the environment show. 

# Training Process Overview
![Screenshot](https://i.ibb.co/zGN79fK/2020-08-20-12-53-42.gif)



