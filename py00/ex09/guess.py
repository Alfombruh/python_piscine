import	random
import	sys
 
    
if __name__ == "__main__":
	ran = random.randint(1, 99)
	step = 0;
	while True:
		step += 1
		try:
			num = int(input("What's your guess between 1 and 99?\n>>"))
			if num < ran:
				print ("Too low!")
				step 
			if num > ran:
				print ("Too high!")
			if num == ran:
				if  ran == 42:
					print("The answer to the ultimate question of life, the universe and everything is 42.")
				if step == 1:
					print("Congratulations! You got it first try!")
					exit()
				print("Congratulations you've got it!")
				print(f"You won in {step} attemps!")
				exit()
		except ValueError:
			print("That's not a number")
		