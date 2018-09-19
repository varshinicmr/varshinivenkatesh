Q1)How to use relational operations in python programming?
A:By writing the following program in sublime text:
a=input("enter value of a:")
b=input("enter value of b:")
c=input("enter value of c:")
if(a>b) and (a>c):
  print(a,"is greater than")
elif(b>c):
  print(b,"is greater than")
else:
  print(c,"is greater than")
  
Output of the above program:
enter value of a:23
enter value of b:7
enter value of c:8
(23, 'is greater than')

enter value of a:45
enter value of b:100
enter value of c:200
(200, 'is greater than')
