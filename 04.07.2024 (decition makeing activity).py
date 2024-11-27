
#DECISION MAKEING ACTIVITYES AND PROGRAMES(4/7/2024)

#check the perfect square(2*2=4)
'''
i=int(input("Enter :"))
s=i**0.5
if s*s==i:
          print(i,"is a perfect square")
else:
          print(i, "is not a perfect square")

'''
#check if the given character is alphabet or number or special char
'''
a=input("enter ")
if (a.isalnum()):

          print("it is alphabet and number")
else:
          print("it is a special char")
          
'''
#another method
'''
a=input("enter ")
if (a.isalpha()):
          print("it is alphabet ")
elif (a.isnumaric()):
          print("it is a number")
elif not a.isalnum():
          print("it is special char")
else:
          print("-----")
'''
#used to find the length and using only 1 lingth is used it will
#give the print statement otherwise it will
#print the enter the one more char
'''
a=input("enter ")
if len(a)==1 a.isalpha():
    print("it is alphabet ")
elif len(a)==1 a.isnumaric():
    print("it is a number")
elif len (a) not a.isalnum():
    print("it is special char")
else:
    print("enter the one more char")
'''
# check the mark is >35 pass and >60 1st class
'''
marks=int(input("enter the mark:")
if marks>60:
    print("1st class")
elif 35<= marks <60:
    print("pass")
else:
    print("fail")
'''
 #checking the starting char of a string is vowel or not
'''
s_=input("enter the string:")
start_char=s_[0]
if start_char in 'aeiouAEIOU':
 print( 'vowel')
else:
 print('not vowel')
'''
# check if the given list has even len
''' 
element=input("enter the element:").split()
if len(element)%2==0:
    print("even length")
else:
    print("odd lenght")
          
'''

#check the number of key in the dicitionary if the number is even
#printhas it is otherwis add new key  to make it even and print it
'''
d={}
d.update({4:5,'a':4,'d':67})
if len(d)%2==0:
    print(d)
else:
    key=input("enter key:")
    value=input("enter valueL")
    d[key]=value
    print(d)
'''


#program to check largest number in user input
'''
n1=int(input("enter:"))
n2=int(input("enter:"))
n3=int(input("enter:"))
if n1>=n2 and n1>=n3:
    print(n1,"is greater")
elif n2>=n1 and n2>=n3:
    print(n2,"is gretest")
else:
    print(n3,"is greatest")
'''
#1.in a number check if the 1st number is even or odd(done)
'''
num_=input("enter the number:")
x=str(num_)
num_1=x[0]
if int(num_1)%2==0:
          print("num_1,even")
else:
          print("num_2, odd")
'''
#2.in a number check if the 2nd last number is even or odd
'''
num_=input("enter the number:")
x=str(num_)
num1_=x[-2]
if int(num1_)%2==0:
          print(num1_,"even")
else:
          print(num1_,"odd")
'''
#3.program to check if the given datatype is of string datatype
'''
a_=input('enter")
print(type(a_),a_)
'''
#4.program to check a data is float datatype
'''
a=input("enter the value")
print(type(a),a)
'''
#5.program to check list is empty or not(done)
'''
a=input("enter the date:")
if len(a)==0:
          print("list is empty")
else:
          print("list is not empty")
          
'''
#6.program to return the length of string if character are persent(done)
'''
t=input("enter the string")
a=t.isalnum()
if a:
         print("present")
         length=len(t)
         print("length is",length)
else:
         print("nothing")
'''
#7.program to get the last element in list(dene)
'''
list_=input("enter the list").split()
print(list_[-1])
'''
#8.program to get the middle char in string(done)
'''
str_=input("Enter:")
middle_index=len(str_)//2
print(middle_index,str_[middle_index])
'''
#9.program to check the data is number or special charcte
#(done)
'''
a=input("enter the data:")
num=a.isnumeric()
if num:
         print("the entered data is number")
else:
         print("the entered data is not a number")
         
'''
#10.prograan to check the inger is positive or negative
'''
num=int(input("enter the number"))
if num>=0:
          print(num,"is postive")
else:
          print(num,"is negative")
'''
#11.program to check smallest number in user input
'''
n1=int(input("enter:"))
n2=int(input("enter:"))
n3=int(input("enter:"))
if n1<=n2 and n1<=n3:
    print(n1,"is smallest")
elif n2<=n1 and n2<=n3:
    print(n2,"is smallest")
else:
    print(n3,"is smallest")

'''
#12.program to check the tuple is empty or not(done)
'''
t=input("enter the data:")
if len(t)==0:
         print("the tuple is empty")
else:
         print("the tuple is not empty")
'''
#13.program to check the number the number is divisible by 5 or 8(done)
'''
num=int(input("enter the number:"))
if num%5==0:
         print("the number is divisible by 5")
elif num%8==0:
         print("the number is divisible by 8")
else:
         print("invalid")
'''
# 14.constructor a marksheet using elif ladder(done)
'''
mark=int(input("enter the marks:"))
if mark>=90:
          print("your grad is A")
elif mark>=80 and mark<=90:
          print("your grad is B")
elif mark>=70 and mark<=80:
          print("your grad is C")
elif mark>=60 and mark<=70:
          print("your grad is D")
elif mark>=40 and mark<=60:
          print("your grad is E")
elif mark<=35:
          print("your grad is F")
else:
          print('---')
'''
#15.take the user input length and breadth of rectangle is
#equal print square or not
length=float(input("enter the length:"))
breath=float(input("enter the breath:"))
if is_square==0(length,breath):
          print("the rectangle is square")
else:
          print("the rectangle is not square")

# progam to check the number is prime square or not(no need)
