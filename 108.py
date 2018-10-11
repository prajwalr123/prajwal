#dictionary
import random
a=['r','p','s']
h1=0
h2=0
while(True):
	u=input("your choice r/p/s ")
	c=random.choice(a)
	print("your choice",u,"computer choice",c)
	if(u=='r'or u=='p'or u=='s'):
		if (u==c):
			print("tie")
		elif((u=='r' and c=='p') or (u=='p'and c=='s') or (u=='s' and c=='r')):
			h1=h1+1
			print("computer win",h1,"times")
		else:
			h2=h2+1
			print("U win",h2,"times")
	else:
     		print("Give proper input")
     		exit()
	if(h1==3 or h2==3):
		if(h1==3):
			print("I'm sorry,computer won the game")
		else:
			print("Congrats U Won the game,have a nice dude")
			exit()#
