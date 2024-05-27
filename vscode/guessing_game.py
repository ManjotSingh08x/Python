#27 May 2024 Manjot Singh 
# This program is a guessing game where a number is choosen from 0 to 100 including both end points 

import random 
def display_game(life_index):
	answer = random.randint(0,100)
	print("lets play a game \n")
	print(f"you are given {life_index} tries") 
	while life_index > 0:
		attempt = int(input("guess the number (between 1 to 100): "))
		if attempt < answer:
			life_index -= 1
			print("too low try again")

		elif attempt > answer:
			life_index -= 1
			print("too high try again")

		else:
			print("congrats you guessed the number!! it was ", answer)
			return 1
	return 0

display_game(10)


