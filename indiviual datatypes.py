# INDIVUAL DATATYPE
#1.integer
#float--->int
#str(number)--->int
#b00l--->int
'''
print(int())
print(int(4.5))
print(int(4.5),int('4'))
print(int(False),int(True))

'''
# exception
'''
print(int('4a'))
print(int(4+4j))
print(int('4.5'))
'''
#user input
'''
num=input("Enter a num :")
print(num,type(num))
num=int(input("Enter a num :"))
print(num,type(num))
'''
#operators
'''
i1=int(input("Enter the 1st num :"))
i2=int(input("Enter the 2nd num :"))
print("add:",i1+i2)
print("sub:",i1-i2)
print("mul:",i1*i2)
print("div:",i1/i2)
print("mod:",i1%i2)
print("floor-div:",i1//i2)
print("Expo:",i1**i2)

'''
#2.float
#float--->int
#str(number)--->int
#b00l--->int
'''
f1,f2=45.5 ,-4.5
print(f1,f2)
print(type(f2))
'''
#constructor
#1.
'''
print(float())
'''
#2.
'''
print(float(4),float('45'))
print(float(True))

'''
#exception
'''
print(float(4+5j))
print(float('4.5a'))
'''

#user input
'''
f1=float(input("Enter a dical-value:\n"))
print(f1,type(f1))
'''
#operator
'''
x=float(input("Enter the 1st num :"))
y=float(input("Enter the 2nd num :"))
print("add:",x+y)
print("sub:",x-y)
print("mul:",x*y)
print("div:",x/y)
print("mod:",x%y)
print("floor-div:",x//y)
print("Expo:",x**y)

'''
#3.complex
'''
c1,c2=4+34j,3.4-45.7j
print(c1,c2)
'''
#constuctor
1.
'''print(complex())
#2.typecasting
#int--->complex
print(complex(45),complex(45j))
#float-->complex
print(complex(45.6),complex(45.6j))
#bool-->complex
print(complex(True))
#sting--->complex
print(complex('90'),
      complex('4.5'),
      complex('4j'))
''''

#program to check th opertores

'''
x=complex(input("Enter the 1st num "))
y=complex(input("Enter the 2nd num "))
print("Add:",x+y)
print("sub:",x-y)
print("mul:",x*y)
print("div:",x/y)
print("mod:",x%y)
print("floor-div:",x//y)


''''
#4.boolean
'''
b1,b2=True,False
print(b1,2)
print(type(b2))
'''
#constructor
#1.
'''
print(bool())
#note
print(bool(0),bool(34))
print(bool(0.0),bool(34.2))
print(bool(0j),bool(34+3j))
print(bool(False),bool(True))
'''

#user input
#string
'''
i=bool(input("Enter :"))
print(i,type(i))
'''
#integer
'''
i=bool(int(input("Enter :")))
print(i,type(i))
#float
i=bool(float(input("Enter :")))
print(i,type(i))
#complex
i=bool(complex(input("Enter :")))
print(i,type(i))
'''




