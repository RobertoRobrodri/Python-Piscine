#!/usr/bin/python

import random

def possible_outcomes(player, machine):
	if player == "Rock":
		if machine == "Scissors":
			print("You won!")
		else:
			print("You lost!")
	elif player == "Paper":
		if machine == "Rock":
			print("You won!")
		else:
			print("You lost!")
	else:
		if machine == "Paper":
			print("You won!")
		else:
			print("You lost!")

selection = {1: "Rock", 2: "Paper", 3: "Scissors"}
while 1:
	player_hand = input("Choose: Rock, Paper or Scissors: ")
	if player_hand != "Rock" and player_hand != "Paper" and player_hand != "Scissors":
		print("Invalid input")
	else:
		computer_hand = selection[random.randint(1, 3)]
		if player_hand == computer_hand:
			print("Draw")
			pass
		else:
			possible_outcomes(player_hand, computer_hand)
			exit()