import random 


while True:
	i=input("Enter'n'to quit ")
	if(i=='n'):
		print("hello!")
		exit()
	else:
		print("you got",random.randint(1,6))		
  

