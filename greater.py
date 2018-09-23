4.COMPARING TWO NUMBERS:
	
a=input("enter value for a:")
b=input("enter value for b:")
if(a>b):
    print(a,"is greater than",b)
elif(a==b):
    print(a,"is equal to",b)
elif(b>a):
	print(b,"is greater than",a)

Output of the above program:
enter value for a:1000
enter value for b:2000
(2000, 'is greater than', 1000)


5.COMPARING THREE NUMBERS:

#comparing 3 no.s
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
