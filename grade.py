a=int(input("marks"))
if(a>=90):
	print("grade-A+")
elif(a>=80):
	print("grade-A")
elif(a>=70):
	print("grade-B+")
elif(a>=60):
	print("grade-B")
elif(a>=40):
	print("grade-C")
else:
	print("fail")



 python grade.py
marks90
grade-A+
dl210@soetcse:~/varshini$ 85
85: command not found
dl210@soetcse:~/varshini$ python grade.py
marks85
grade-A
dl210@soetcse:~/varshini$ python grade.py
marks35
fail

