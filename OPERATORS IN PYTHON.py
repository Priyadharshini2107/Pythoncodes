#operators in python

#1.Arithmetic operators
'+,-,*,/,//,%,***'
'''
a=int(input("enter the value a:"))
b=int(input("enter the value b:"))
print(a+b)
print(a-b)
print(a+b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a***b)
'''
#2.relational opertors
'''
print(3<4,4>3)
print(3<=4,4<=4,5<0.1)
print(3>=4,4>=4,5>0.1)
print('hai'=='hai','hai'=='hai')
print('hai'!='hai','hai'!='hi')
print(3>4,5>0.1)
print('hai'!='hai','hai'!='bye')
'''
#3.logical operators
'or' 'and' 'not'
#or--->this operator returns true if one condition will be coorect
'''
print(45<45 or 45>=45)
print(20>30 or 30<50)
'''
#and---> this returns true if both statement or condition is true
'''
print(1<5 and 6>4)
print(4>1 and 3>2)
'''
#not---> this reverse the result return false if the result is true
'''
print(not(5>3 and 5>10))
print(not(4>1 and 5>2))
'''
#4.bitwise operator
#1.or--->'|'convert the number to binary then perfrom the or operation
'''
n1=34
n2=40
print(n1|n2)
n3=5
print(n1|n2|n3)
'''
#2.and-->'&'
'''
n1=32
n2=40
print(n1&n2)
n3=62
print(n1&n2&n3)
'''
#3.not-->'-'
'''
print(-34)
print(--40)
'''
#4.xor-->
#same number-->0 and different number--->]
'''
n1=45
n2=40
print(n1^n2)
n3=20
n4=20
print(n3^n4)
'''
#5.assignment operators
#=
'''
n=86
print(n)
'''
#+=
'''
n=n+1
n+=10
print(n)
'''
#*=
'''
n='hi'
n*=4
print(n)
'''
#/=
'''
n=9
n/=3
print(n)
'''
#%=
'''
n=34
n%=2
print(n)
'''
#-=
'''
n=32
n-=2
print(n)
'''
#**=
'''
n=34
n**=8
print(n)
'''
#//=
n=8
n//=2
print(n)

#6.identitt operator
'''
#i.is
n=20
n1=20
print(n is n1)
#ii.is not
n2=20
n3='hey'
print(n2 is not n3)
'''
#7.member ship
'''
#i. in
print('h'in'hai','H'in 'hai')
print('h'='hai')
print('bye'in['hai','hello','bye'])
print('bye'in{'hai':3,'hello':45,'bye':4.5})

#ii. not in
print(45 not in{'hai':3,'hello':45,'bye':4.5})
print('hai'not in{'hai':3,'hello':45,'bye':4.5})
'''
