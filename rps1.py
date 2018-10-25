import random
c={1:'rock',2:'paper',3:'scissor'}
r=random.randint(1,3)
d=['r','p','s']
t=random.choice(d)
print(t)
q=input("enter 'r' for rock,'p' for paper,'s' for scissor")
if(q=="c"):
	print("tie")
elif(q=="r" and c=="p"):
	print("c wins")
elif(q=="r" and c=="s"):
	print("p wins")
elif(q=="p" and c=="s"):
	print("c wins")
elif(q=="p" and c=="r"):
	print("p wins")
elif(q=="s" and c=="r"):
	print("c wins")
elif(q=="s" and c=="p"):
	print("p wins")
else:
	'break'