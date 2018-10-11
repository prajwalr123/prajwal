a=['1','2','3','4','5','6','7','8','9']
def print_Board():
	print(a[0],'|',a[1],'|',a[2])
	print("---------")
	print(a[3],'|',a[4],'|',a[5])
	print("---------")
	print(a[6],'|',a[7],'|',a[8])
	

player1turn=True
while True:
	print_Board()
	p=input("choose an available place: ")

	if(p in a):
		if(a[int(p)-1]=='X' or a[int(p)-1]=='O'):
			print("place taken, choose another place...")
			continue
		else:
			if player1turn:
				print("player 1>>")
				a[int(p)-1]='X'
				player1turn = not player1turn
			else:
				print("player 2>>")
				a[int(p)-1] ='O'
				player1turn =not player1turn
		#checking for rows
			for i in(0,3,6):
				if(a[i]==a[i+1] and a[i]==a[i-2]):
					if(a[i]=='X'):
						print("congratulations to player 1")
					else:
						print("congratulations to player 2")
					print_Board()
					print("Game Over");
					exit()
			#checking for columns
			for i in range(3):
				if(a[i]==a[i+3] and a[i]==a[i+6]):
					print("Game Over")
					if(a[i]=='X'):
						print("congratulations to player 1")
					else:
						print("congratulations to player 2")
					print_Board()
					exit()
				#checking for diagonal (left to right)
				if(a[0]==a[4] and a==[8]):
					print("Game Over")
					if(a[4]=='X'):
						print("congratulations to player 1")
					else:
						print("congratulations to player 2")
					print_Board()
					exit()
				#checking for diagonal (right to left)
				if(a[2]==a[4] and a[2]==a[6]):
					print("Game Over")
					if(a[4]=='X'):
						print("congratulations to player 1")
					else:
						print("congratulations to player 2")
					print_Board()
					exit()
	else:
		print("You have entered an invalid position")
		continue


