import random


while True:
	i=input("Enter 'q' to quit,press'r' to roll the dice")
	if(i=='q'):
		print("Bye!")
		exit()
	else:
		print("you got",random.randint(1,6))


	