#1. progarm to check a number is prime or not
#number div by 1 or itself
'''
number =int(input("enter a number:"))
for n in range(2,number):
          if number %n==0:
                    print("It is not a prime number")
                    break
else:
          print("It is prime number")

'''
#2.progarm to get prime number in a range(any range want giveex:range 1to 10
#1,2,3,4,,5,6,7,8,9,10 in the number what are the prime number
'''
s_v=int(input("enter a number:"))
e_v=int(input("enter a number:"))
for i in range(s_v,e_v+1):
    for j in range(2,i):
          if i%j==0:
              break
    else:
          print(i,end='')
''''
#using pass
'''
s_v=int(input("enter a number:"))
e_v=int(input("enter a number:"))
for i in range(s_v,e_v+1):
    for i<=1:
          pass
    else:
          for j in range(2,i):
              if i%j==0:
                    break
    else:
          print(i,end='')
'''

#3.progarm to get a fictorial number
'''
num_=int(input("enter a number:"))
fact_=1
for i in range (fact_,num_+1)
          fact_=fact_*i
print("factorial of",num_,'is',fact_)
'''
#4.progarm to print fibinnacci number
#0112353
#3---->0,1,1,5--->01123j
'''
num_=int(input("Enter a number"))
a=0
b=1
print(a)
print(b)
for in range(2,num):#(2,5)=2,3,4=2|3|4
          c=a+b#0+1=1|1+1=2|1+2=3
          a=b#a=1|
          b=c#b=1|
          print(c)
'''
'''
num_=int(input("Enter a number"))
a=0
b=1
if num_<=1:
          print(0)
else:
          print(a)
          print(b)
    for in range(2,num):#(2,5)=2,3,4=2|3|4
          c=a+b#0+1=1|1+1=2|1+2=3
          a=b#a=1|
          b=c#b=1|
          print(c)
'''
#5.program to check armstrong number
n=int(input("enter a number"))
len_=len(str(n))
sum_=0
for digit in str(n):
          sum_+=int(digit)**len_
if sum_=n:
          print(" is a armstrong number")
else:
          print(" is not a armstrong number")
