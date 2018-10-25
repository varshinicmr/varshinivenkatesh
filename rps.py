import random
c=['r','p','s']
s1=0
s2=0
while True:
	q=input("enter value r/p/s")
	if(q==c):
		print("tie")
	elif(q=='r'):
		if(c=='p'):
			print("c win")
			s1+=1
		else:
			print("q wins")
			s2+=1
	elif(q=='p'):
		if(c=='s'):
			print("c win")
			s1+=2
		else:
			print("q wins")
			s2+=2
	elif(q=='s'):
		if(c=='p'):
			print("c win")
		else:
			print("q wins")	
	if(s1=="3"):
		print("s1 win")
	else:
		print("s2 wins")
		break