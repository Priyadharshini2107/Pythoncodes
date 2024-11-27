#decision making
#i. if condition
'''
if True:
   print('hai')

if False:
   print('hai')

if bool(1):
   print('bye')

if bool(0):
   print('bye')

if bool(0)or bool(1):
   print('bye')

if bool(0) and bool(1):
   print('bye')
'''
'''
n=input('enter:')
if n:
   print("date is persent")
'''
'''
n=input('enter:')
if n:
   print("date is persent")
print("date is not persent")
'''
#ii.if-else condition
'''
n=input('enter:')
if n:
   print("data is persent")
else:
   print("data is not persent") 
'''
#iii.nested if-else condition
'''
if True:
   print('main if')
   if True:
      print('nested if')
   else:
      print('nested else')
else:
   print('main else')
'''
'''
if False:
   print('main if')
   if False:
      print('nested if')
   else:
      print('nested else')
else:
   print('main else')
'''
#iv.elif condition(else-if)
'''
if True:
   print('a')
elif True:
   print('b')
elif True:
   print('c')
else:
   print(False)
'''
'''
if False:
   print('a')
elif True:
   print('b')
elif True:
   print('c')
else:
   print(False)
'''
'''
if False:
   print('a')
elif False:
   print('b')
elif True:
   print('c')
else:
   print(False)
'''
'''
if False:
   print('a')
elif False:
   print('b')
elif False:
   print('c')
else:
   print(False)
'''
#1.program to check the given number is odd or even
'''
num_=int(input("enter the num:"))
condition_=num_%2==0
if condition_:
   print("even number")
else:
   print("odd number")
'''
#2.write a program to check a charater is vowei or not
'''
vowel_=('a','e','i','o','u')
char_=str(input("enter the char:"))
if char_ in vowel_:
   print("the char is vowel")
else:
   print("the char is not vowel")
      
'''
#3.check wherther the string is palindrom or not
'''

a=str(input("enter the string:"))
if (a==a[::-1]):
      print("it is a palindrom ")
else:
      print("it is not a plaindrom")

'''
#4.check wherthe th number is palindrom or not
'''
a=input("enter the number:")
if (a==a[::-1]):
      print("it is a palindrom  number")
else:
      print("it is not a plaindrom number")
'''
#5.check wherther the year is leap year or not
'''
year=int(input("enter the year:"))
condition= year%4==0
if condition:
   print("It is a leap year")
else:
   print("It is not leap year")
'''
