# PROJECT QUETIONS OF DECISION MAKEING
# 1.a school has following rules for getting system
'''
mark=int(input("enter the marks:"))
if mark<=25:
          print("your grad is F")
elif mark>=25 and mark<=45:
          print("your grad is E")
elif mark>=45 and mark<=50:
          print("your grad is D")
elif mark>=50 and mark<=60:
          print("your grad is C")
elif mark>=60 and mark<=80:
          print("your grad is B")
elif mark>=80:
          print("your grad is A")
else:
          print('---')
'''
#2.program to take input age of 3pepople by user
#and determine oldestamong them
'''
age1=int(input("Enter the age1:"))
age2=int(input("enter the age2:"))
age3=int(input("enter the age3:"))
if age1>=age2 and age1>=age3:
          print(age1,"is oldest among  others")
elif age2>=age1 and age2>=age3:
          print(age2,"is oldest among  others")
else:
          print(age3,"is oldest among  others")
'''
#3.program to take input age of 3pepople by user
#and determine youngest them
'''
age1=int(input("Enter the age1:"))
age2=int(input("enter the age2:"))
age3=int(input("enter the age3:"))
if age1<=age2 and age1<=age3:
          print(age1,"is youngest of others")
elif age2<=age1 and age2<=age3:
          print(age2,"is youngest of others")
else:
          print(age3,"is youngest of others")
'''

#4. a student will not be allowed to sit in exam if his\her attendance
#is less then 75% taken follwing input user
#number of class held
#number of class attended
#and print percent of cls attended student is allowed to sit in exam or not
'''
a=int(input("enter the cls held:"))
b=int(input("enter the cls attended:"))
percent=a/b*100
if (percent>=75):
          print("student is allowed to attend the exam")
else:
          print("student not allowed to attend")
'''
#  program to get tail and head
'''
import random
num_=random.randint(0,1)
if num_==0:
          print("head")
else:
          print("tail")
'''

#program to guess number:
'''
import random
name=input("what is your name:")
print("hey",name,"Let's start the gram:")
computer_guess=random.choice((1,2,3,4,5))
user_guess=int(input("guess a number 1to5 :"))
print(computer_guess)
if user_guess==computer_guess:
          print("you win")
elif user_guess<computer_guess:
          print("guess is larger number")
elif user_guess>computer_guess:
          print("guess is lower number")
else:
          print("guess only number in the tuple")
          
'''

#program to stone,paper,scissor
'''
import random
name=input("what is your name:")
print("hey",name,"Let's start the gram:")
computer_item=random.choice(['scissor','stone','paper'])
user_input=input("scissor or stone or paper")
print(computer_item)
if computer_item==user_input:
          print("draw")
elif computer_item=='scissor':
          if user_input=='stone':
              print("you won stonehits scissor")
          else:
              print("you lost scissor cut paper")
elif computer_item=='stone':
          if user_input=='paper':
              print("you wow paper wrap the stone")
          else:
              print("you lost stone hits thescissor")
else:
          if user_input=='scissor':
              print("you won scissor cut the paper")
          else:
              print("you paper wrap the rock")
'''
