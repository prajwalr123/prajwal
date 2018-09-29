#1/usr/bin/python3
import random
count=0
#def my roll():
#	return random.randint(1,6)
def myroll():
	return random.randint(1,6)

while(count<=100):
	n=input("press r to roll the dice ")
	if(n=='r'):
#ROLL THE DICE
		r=random.randint(1,6)
		count=count+r
		print("u got ",r)
		print("new position is",count)

#CHECKING FOR SNAKE AND LADDER
		if(count==8):
			count=37
			print("i got the ladder")
		elif(count==11):
			count=2
			print("sorry, snake bite to u")
		elif(count==13):
			count=34
			print("i got the ladder")

		elif(count==38):
			count=9
			print("sorry, snake bite to u")

		elif(count==40):
			count=68
			print(" i got the ladder")

		elif(count==52):
			count=81
			print(" i got the ladder")


		elif(count==65):
			count=46
			print("sorry, snake bite to u")

		elif(count==76):
			count=97
			print(" i got the ladder")


		elif(count==89):
			count=70
			print(" sorry, snake bite to u")

		elif(count==93):
			count=64
			print("sorry snake bite to u")
		elif(count==100):
			print("congrats you won the game")
			exit()
		elif(count>100):
			print("stay in the same count")
			count=count-r
















