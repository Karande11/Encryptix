#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def game():
    choices = ["rock", "paper", "scissor"]
    computer = random.choice(choices)

    user = input("Enter your choice (rock/paper/scissor): ").lower()
    while user not in choices:
        user = input("Invalid input. Enter your choice (rock/paper/scissor): ").lower()

    print(f"\nComputer chose {computer}, you chose {user}.\n")

    if user == computer:
        return "It's a tie!"
    if user == "rock":
        if computer == "scissor":
            return "Rock smashes scissor! You win!"
        else:
            return "Paper covers rock! You lose."
    if user == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissor cuts paper! You lose."
    if user == "scissor":
        if computer == "paper":
            return "Scissor cuts paper! You win!"
        else:
            return "Rock smashes scissor! You lose."

print(game())


# In[ ]:




