#playing the game of rock paper scizeer
a={1:'r',2:'p',3:'s'}
import random
c=a[random.randint(1,3)]
print("computer choice is",c)
u=input("Enter rock paper and scizeer :")
if(u==c):
	print("COMPUTER AND USER ARE TIE")
elif(u=='p' and c=='s' or u=='s' and c=='r' or u=='r' and c=='p'):
	print("SORRY BRO U LOSS")
else:
	print("CONGRATS U WON BRO")
 




		