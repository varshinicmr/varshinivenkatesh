PRINTING RANDOM NO. USING DICE FUNCTION:
import random
while True:
	a=input("press y to roll")
	if(a=="y"):
		r=random.randint(1,6)
		print(r)
	else:
		print("bye")
		break





