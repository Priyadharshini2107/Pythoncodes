#program to get the length of any ierable with method

'''
list_=[5,6,7]
tuple_=(4.5,6.7)
print(len(list_1,len(tuple_),len('hi')))
'reusability'
def length_(iterable):
          print(len(ierable))

length_([5,6,7])
length_([4.5,6.7])
length_('hi')
'''
#program to get the length of any iterable without method
'''
def length_(s):
    count=0
    for i in s:
          count+=1  
    print(count)


s="hi wlecome"
print(length_(s))
'''
#variable scope
#1.global vaeialbe
'''
a=10
def f1():
          print(a,"inside the function")

f1()
print(a,"outside the function")
'''
#2. local variable
'''
a=10
def f1():
          a=20
          print(a,"inside the function")

          
f1()
print(a,"outside the fiuntion")
'''
#i.convert local to global
'''
a=10
def f1():
          global a
          a=20
          print(a,"inside the function")

f1()
print(a,"outside function")
'''
#ii.return keyword
#1.
'''
a=10
def f1():
          a=10
          return a
a1=f1()
print(a1)
print(f1())
'''
#2.(we does not declare the value and varialbe uding only the return)
'''
def f1():
          return
a1=f1()
print(f1())
'''
#3.in tuple from
'''
def operation(a,b):
          return a+b,a*b
op=operation(10,20)
print(op)
'''
'''
def operation(a,b):
          return a+b
op=operation(10,20)
print(op)
'''
#3.non-local variable:
'''
def f1():
          num=100
          def f2():
                    num=200
                    print(num)
          f2()
          print(num)
f1()
'''
#to convert local to gobal
'''
def f1():
          num=100
          def f2():
                    nonlocal num
                    num=200
                    print(num)
          f2()
          print(num)
f1()
'''
#types of agrgument
#1.possitional argument
'''
def f1 (name,age,reg_no):
          return name,age,reg_no
f1("priya",20,70)
'''
'''
def f1 (name,age,reg_no):
          return f"name{name}\nage{age}\n reg_no{reg_no}"
f1("priya",20,70)
'''
#2.keywords argument
'''
def func (name,age):
          print(name,age)
func(34,"neha")

'''
#3.combination of positonal and key argument
'''
def f1(name,age,reg_no):
          return(name,age,reg_no)
print(f1('rani',34,3))
#excception
print(f1(34,name='rani',id=3))
'''
#4.only positional and keyword argument
#i.only positional
'''
def f1(a,b,/,c,d):
          print(a,b,c,d)
f1(10,20,45,45)
f1(10,20,c=45,d=45)
f1(10,20,45,d=45)
#excpetion
f1(10,b=20,c=45,d=45)

'''
#5.only keyword argument
'''
def f1(a,b,*,c,d):
          print(a,b,c,d)
f1(a=10,b=20,c=45,d=45)
f1(10,20,c=45,d=45)
f1(10,20,45,d=45)
'''
#5. variable positional argument
'''
def fun(a,b,c):
          print(a,b,c)
fun(3,4,5)
'''
#otherway
'''
def func(*agrs):
          print(*args)
func(3,4,5)
func('hai',[4,5,6],True)
'''
#6. variable keyword argument
'''
def func(**kwargs):
          print(kwargs)
func(a=34,b=3,c=False,d="python",e=[False,True])
'''
#7. default argument
'''
def func(a,b):
          return a**2,b**3
print(func(3,5))
print(func(4))
print(func())
'''
#PROGRAMS
#1.
'''
def f1(*a):
          if len(a)>5:
                    return True
          else:
                    return False

print(f1(3,4,5,6))
print(f1(3,4,5,6,7,8))
#USER INPUT
def f1(a=input("enter a number:")):
          if len(a.split())>5:
                    return True
          else:
                    return False
print(f1())

'''
#2.write a function print the below output
#("TRACXN",0)
#("TRACXN",1)
'''
def f1(str_,n):
          if n==0:
                    print(str_[1::2])
          elif n==1:
                    print(str_[::2])
f1("TRACXN",0)
f1("TRACXV",1)
'''
#Qtalk porgraming
#1.Write a function to check if the number is Prime
'''
number=int(input("enter  a number:")
for n in range (2,number):
           if number %n==0:
           print("it is not prime number")
           break
           else:
           print("it is a prime number")
           '''

#2.Write a method that returns the last digit of an integer. For example, the call of get_last_digit(3572) should return 2.
'''
def get_last_digit(number):
          return abs(number)%10
print (get_last_digit(123458))
print (get_last_digit(123))
'''
#3.Make a function named tail that takes a sequence (like a list, string, or tuple) and a number n and returns the last n elements from the given sequence, as a list.
'''
def tail(sequence,n):
          if n<=0:
                    return[]
          return list(sequence[-n:])
print(tail[1,2,3,4,5],3)
print(tail("hello",2)
'''
#4.Write function named is_perfect_square that accepts a number and returns True if it's a perfect square and False if it's not.
'''
def is_perfect_square(n):
          return n== int(n**0.5)**2          
print(is_perfect_square(16))
print(is_perfect_square(20))
'''
#5.Write a function which returns the sum of lengths of all the iterables
'''
def sum_of_lengths(*iterables):
          return sum(len(iterable)for iterable in iterables)
print(sum_of_lengths([1,2,3,4],"hello",(6,7)))
print(sum_of_lengths("python","AI",[1,2]))
'''
#6.Python function  to check if a given number the Fibonacci number?
'''
def fact(num):
          fact=1
          for i in range(1,num+1):
                    fact=fact*i
num=int(input("enter a number:"))
print("factorial of ",num ,'is',fact(num))
'''

   # Recursion Function
'''

"to known recursion limit"
import sys
print(sys.getrecursion limit())
sys.setrecursion limit(20)
print(sys.getrecursion limit())
def func_name():
          print("hai")
          func_name()
func_name
'''
#program to print from 1 to 10 using function concept
'''
def print_(i=1,l_=[]):
          if i<=10:
                    l_.append(i)
                    return print_(i+1,l_)
          else:
                    return l_
print(print_())'''
#program to print from 20 to 10 using function concept
'''
def print_(i=20,l_=[]):
          if i>10:
                    l_.append(i)
                    return print_(i-1,l_)
          else:
                    return l_
print(print_())'''

#program to print from 1 to 5 and sum it
'''

def print_(i=1,l_=[]):
          if i<=5:
                    l_.append(i)
                    sum=0
                    sum+=1
                    return print_(i+1,l_)
          else:
                    return l_
print(sum,print_())'''


#program to get factorial of a number
'''num_=int(input("enter a number:"))
i=1
fact_=1
while num_>=i:
          fact_=fact_*i
          i+=1
print("factorial of",num_,'is',fact_)'''
'''
def factorial(i=1,fact_=1):
          if i<=5:
                    fact_=fact_*i
                    return factorial(i+1,fact_)
          else:
                    return fact_
print(factorial())
'''
#progarm to get fibonacci sequence
'''
def fibonacci_sequence(n):
          fib_sequence=[0,1]
          if n<=0:
                    return[]
          elif n==1:
                    return[0]
          while len(fib_sequence)<n:
                    fib_sequence.append(fib_sequence[-1]+fib_sequence[-2])
          return fib_sequence[:n]
print(fibonacci_sequence(5))
'''
#program to get sum of digits
'''
def sum_of_digits(number):
    number = abs(number) 
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total
print(sum_of_digits(3572))  
print(sum_of_digits(-1234))
'''
#program to reverse a string
#normal way
'''
i=0
ne_s=''
str_=input("enter:")
while i<len(str):
          ne_s=str_[i]+ne_s
          return
          '''
'''
def reverse_(i=0,ne_s='',str_=input("enter:")):
          if i < len(str_):
                    ne_s=str_[i]+ne_s
                    return reverse_(i+1,ne_s,str_)
          else:
                    return ne_s
print(reverse_())'''
#program to get greatest common Divisor
'''
def gcd(a,b):
          if b==0:
                    return a
          else:
                    return gcd(b,a%b)

          
print(gcd(25,5)'''
