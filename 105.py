#defining a function
i=int(input("Enter the value of i:"))
j=int(input("Enter the value of j:"))
o=input("What do you want to do? +,-,*,/ " )

def add():
	return i+j
def sub():
	return i-j
def mul():
	return i*j
def div():
	return i/j

if(o=='+'):
	print("addition=",add())
elif(o=='-'):
	print("subtraction=",sub())
elif(o=='*'):
	print("multiplication=",mul())
elif(o=='/'):
	print("division=",div())
else:
	print("give a proper number")