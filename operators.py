def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mult(a,b):
	return a*b
def divide(a,b):
	return a/b

i=int(input("enter value of a: "))
j=int(input("enter value of b: "))
o=input("what do you want to do? +,-,*,/: ")

if(o=='+'):
	res=add(i,j)
elif(o=='-'):
	res=sub(i,j)
elif(o=='*'):
	res=mult(i,j)
elif(o=='/'):
	res=divide(i,j)

print(res)



enter value of a: 10
enter value of b: 5
what do you want to do? +,-,X,/: +
15
dl210@soetcse:~/varshini$ python3 operators.py
enter value of a: 20
enter value of b: 20
what do you want to do? +,-,x,/: -
0
dl210@soetcse:~/varshini$ python3 operators.py
enter value of a: 40
enter value of b: 10
what do you want to do? +,-,x,/: /
4.0
dl210@soetcse:~/varshini$ python3 operators.py
enter value of a: 20
enter value of b: 40
what do you want to do? +,-,x,/: x
Traceback (most recent call last):
  File "operators.py", line 19, in <module>
    res=mult(i,j)
  File "operators.py", line 6, in mult
    return axb
NameError: name 'axb' is not defined
dl210@soetcse:~/varshini$ python3 operators.py
enter value of a: 4
enter value of b: 7
what do you want to do? +,-,x,/: x
28
dl210@soetcse:~/varshini$ python3 operators.py
enter value of a: 7
enter value of b: 8
what do you want to do? +,-,x,/: x
Traceback (most recent call last):
  File "operators.py", line 23, in <module>
    print(res)
NameError: name 'res' is not defined
dl210@soetcse:~/varshini$ python3 operators.py
enter value of a: 8
enter value of b: 9
what do you want to do? +,-,x,/: *
72
