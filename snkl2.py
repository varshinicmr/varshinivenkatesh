import random
count=0
while(count<=100):
	a=input("press r to roll")
	if(a=="r"):
		r=random.randint(1,6)
		print(r)
		count=count+r
		print("score is",count)
		if(count==100):
			print("you won")
			print("your score is",count)
		elif(count==11):
			count=2
			print("snake bite")
		elif(count==25):
			count=4
			print("snake bite")
		elif(count==38):
			count=9
			print("snake bite")
		elif(count==65):
			count=46
			print("snake bite")
		elif(count==89):
			count=70
			print("snake bite")
		elif(count==93):
			count=64
			print("snake bite")
		elif(count==8):
			count=37
			print("climb ladder")
		elif(count==13):
			count=34
			print("climb ladder")
		elif(count==40):
			count=68
			print("climb ladder")
		elif(count==52):
			count=81
			print("climb ladder")
		elif(count==76):
			count=97
			print("climb ladder")
	else:
		break

print("climb ladder")

etcse:~/varshini$ python3 snkl2.py
press r to rollr
1
score is 1
press r to rollr
6
score is 7
press r to rollr
5
score is 12
press r to rollr
6
score is 18
press r to rollr
5
score is 23
press r to rollr
6
score is 29
press r to rollr
6
score is 35
press r to rollr
5
score is 40
climb ladder
press r to rollr
5
score is 73
press r to rollr
3
score is 76
climb ladder
press r to rollr
4
score is 101





