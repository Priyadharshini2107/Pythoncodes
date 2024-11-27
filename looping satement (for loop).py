
#FOR LOOP SATEMENT
# program to iterate in iterable
'''
str_="python"
for i in str_:
          print(i)
'''
'''
list_=["python","java","css","perl",5,2.5]
for i in list_:
          print(i)
'''
'''
tuple_=("python","java","css","perl",5,2.5)
for i in tuple_:
          print(i)
'''
'''
set_={"python","java","css","perl",5,2.5}
for i in set_:
          print(i)

'''
'''
dict_={"python":56,"java":56.'perl':45,45:'int',2.4:[4,5,6]}
#get keys
for item in dict_:
          print(item)
for key in dict_.keys():
          print(key)
#grt values
for v in dict_.items():
          print(v)
#get the items
for i in dict_.itemes():
          print(i)
#unpack
for item in dict_.ietms():
          print(item[0].item[1])
'''
#control statement
#1.break
#program to break when the number is 5
'''
i=1
while i <10:
          if i==5:
                    break
          else:
                    print(i)
          i+=1
'''
#2. continue
# program to skip all the even number
'''
t_=(34,5,3,68,4,90,77,23)
for num in t_:
          if num%2==0:
                    continue
          print(num)
'''
#3.pass
'''
for i in [4,5,6]:
          pass
for i in 'hai':
          print(i)
'''

#program to print abc.py output:py
'''
in_=input("enter the filename:").split('.')
print(in_[-1])
'''
#using inbulit function in using fro loop
#1.range

# program to print number from 1to 10
'''i=1
while i<11:
          print(i)
          i+=1'''
#range(typecaseed)
'''
r1=range (1,11)
print (list(r1)
'''
#for loop
'''
r1=range(1,11)
for n in r1:
       print(n,end=' ')
'''
# program to print number from 10to1
'''
for n in range (10,0,-1):
          print(n,end=' ')
'''
#program to print the number from -10 to -1
'''
for n in range (-10,0):
          print(n,end=' ')
'''
#program to print the number from -10 to 5
'''
for n in range (-10,6):
          print(n,end=' ')
'''
'''
#program to print the number from 20 to -15
for n in range (20,-16,1):
          print(n,end=' ')
'''
'''
#program to print the number from -20 to -15
for n in range (-20,-14,1):
          print(n,end=' ')
'''
#progarm to get only even number from user -input
'''
start_v=int(input("enter the startvalue"))
end_v=int(input("enter the endvalue"))
for num in range (start_v,end_v):
          if num%2==0:
                    print(num,end=' ')'''

#progarm to get only odd number from user -input
'''
start_v=int(input("enter the startvalue"))
end_v=int(input("enter the endvalue"))
for num in range (start_v,end_v):
          if num%2!=0:
                    print(num,end=' ')
'''
'''
#program to get the words and indexs using for loop
str_=input("enter the word:").split()
for index_ in range(len(str_)):
                    print(index_,str_[index_])
                  
#packed into tuple
str_=input("enter the word:").split()
t_=()
for index_ in range(len(str_)):
          t_+=(index_,str_[index_],)
print(t_)
'''
#2.enmurators
#typecase
'''
str1=input("enter the word").split()
print(tuple(enumerate(str1)))
print(list(enumerate(str1)))
for t_ in enumerate(str1,1):
          print(t_)
'''
# create a tuple with index and length of each words'
'''
str_="hello guys see on the screen and do this program"
t_=()
for i,word in enumerate (str_.split()):
          t_+=((i,len(word)),)
print(t_)
   '''
#create a set with index and words only with even length
'''
str1="shareing is caring as always hai"
s_=set()
for i,word in enumerate (str1.split()):
          if len(word)%2==0:
                    s_.add(word)
print(s_)
'''
#3.zip/ziplongest method
#program to add the number in same indexs
'''
l1=input("enter the list1:")
l2=input("enter the list2:")
print(list(zip(l1,l2)))
'''
'''
l1=input("enter the list1:").split()
l2=input("enter the list2:").split()
from itertools import zip_longest
for i,j in zip_longest(l1,l2,fillvalue=10):
          print(f'{int(i)}+{int(j)}={int(i)}+{int(j)}')
'''
'''
l1=input("enter the list1:").split()
l2=input("enter the list2:").split()
from itertools import zip_longest
for i,j in zip_longest(tuple(l1),tuple(l2),fillvalue=10):
          print(f'square{int(i)}={int(i)**2}and{int(j)}={int(j)**3}')
          print(int(i)**2,int(j)**3)
   '''       
#QTALK PORGRAM

#1.print number from 1to10
'''
r1=range(1,11)
for i in r1:
          print(i,end='')
'''
#2.write a program to find the sum of the frist 10 natural nummber
'''
a=input("enter the value")
total=0
for i in range(total,a+1):
          total+=1
          print("the sum of the frist 10 natural number:",i)
   '''
#3.write program to all even number between 1 and 20
'''
for i in range(1,21):
          if i%2==0:
                    print(i)
'''
#4.write a program to reverse a given number
'''
num=input("enter a number:")
reverse=0
for i in str(num):
          print("reverse number:",int(str(num)[::-1]))
   '''      
'''          
num=input("enter a number")
print("reverse number:",int(str(num)[::-1]))'''
#5. check if prime or not
#num div by 1 or itself
'''
number=int(input("enter  a number:")
for n in range (2,number):
           if number %n==0:
           print("it is not prime number")
           break
           else:
           print("it is a prime number")
           '''
#6.write a program to print fibonacci series up to a given number'n'

#0112353
#3---->0,1,1,5--->01123j
'''
num_=int(input("Enter a number"))
a=0
b=1
print(a)
print(b)
for i in range(2,num_):
          c=a+b
          a=b
          b=c
          print(c)
'''
'''
n=int(input("enter a number"))
len_=len(str(n))
sum_=0
for digit in str(n):
          sum_+=int(digit)**len_
if sum_== n:
          print('f{n} is a armstrong number')
else:
          print('f{n} is not a armstrong number')
'''
#7.write a program to find the fictrial of given number
'''
num_=int(input("enter a number:"))
fact_=1
for i in range (fact_,num_+1):
          fact_=fact_*i
print("factorial of",num_,'is',fact_)
'''
#8.program to find the sum of the digits of the given number
'''
num = int(input("Enter a number: "))
sum_of_digits = 0

for i in str(num):
    sum_of_digits += int(i)

print("Sum of digits:", sum_of_digits)
'''
#9.program to count the number of digits in a given number
'''
n=input("enter a digit:")
count = 0
for digit in str(n):
          count += 1
print("Number of digits:", count)
'''
#10.print all prime number between 1 to 100
'''
s_v=int(input("enter a number"))
e_v=int(input("enter a number:"))
for i in range(s_v,e_v+1):
          for j in range (2,i):
                    if i%j==0:
                     break
          else:
                    print(i,end='')
'''               

#11.program to check armsrong number
'''
n=int(input("enter a number"))
len_=len(str(n))
sum_=0
for digit in str(n):
          sum_+=int(digit)**len_
          if sum_=n:
                    print("is a armstrong number")
          else:
                    print("is not arstrong number")
                    
'''
#12.program to find the sum of even digit in a given number
'''
num = int(input("Enter a number: "))
sum_of_digits = 0

for i in str(num):
          if int(i)%2==0:
                    sum_of_digits += int(i)

print("Sum of even digits:", sum_of_digits)
'''
#13.program to find the sum of square of the digit in a number
'''
num=int(input("enter the number:"))
sum_of_squares=0

for i in str(num):
          sum_of_squares+=int(i)**2
print("sum of squares of digit:",sum_of_squares)
'''
#14. program to find the sum of HCF highest common factor of two number
'''
num1=int(input("enter frist number:"))
num2=int(input("enter second number:"))
hcf=0
for i in range (1,min(num1,num2)+1):
          if num1%i==0 and num2%i==0:
                    hcf=i
print("HCF using For Loop:",hcf)

'''
#15. write a program to for a number guessing game
''''
import random

number_to_guess = random.randint(1, 100)
attempts = 0

for attempt in range(10):  
    user_guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number correctly in {attempts} attempts.")
        break

if attempts == 10:
    print(f"Sorry, you didn't guess the number. The correct number was {number_to_guess}.")

'''
#range questions
#sum of range of number
start = 1
end = 10
sum = 0

for i in range(start, end + 1):
    sum += i

print("Sum of numbers from", start, "to", end, "is:", sum)
