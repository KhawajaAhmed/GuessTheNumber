# This is 'Guess the Number Game'

import random

num = random.randint(1,20)

print("Hello! What is your name?")
name = input()

print("Well, " + name + ", I am thinking of a number between 1 and 10.")

for i in range(6):
	
	print("\nTake a guess.")
	guess = input()
	guess = int(guess)

	if(guess == num):
		break
	elif(guess > num):
		print("Your guess is high")
	else:
		print("Your guess is low")

if(guess == num):
	print("\nCongratulations! You guessed my number in", i+1,"guesses." )
else:
	print("\nYou ran out of guesses. My number was:",num)
