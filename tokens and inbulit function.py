#Token in python
#keywords
'''
"help('keywords')"
help("keywords")
'''
#2.
'''
import keyword
print(keyword.kwlist)
'''
#3.keyword is not changable
'''
print(True)
print(true)
'''
#identifiers
'''
a1=10
print(a1)
'''

#2
'''
_a,a_1,a_ = 90,35,78
print(_a,a_1,a_)
'''
#excepton


#2. variable
'''
myname = "pyspider"
print(myname)

num =45
print(num)

boll_ = False
print(boll_)
'''
#case - 1
'''
n1,n2 = 45,34
print(n1,n2)
'''
# case -2
# The variable is same and
# value is Different
'''
c1 = 'a'
c1 = 'b'
print(c1)
'''
#case - 3
# The variable is different and
# value is Different
'''
c1 = 'a'
c2 = 'a'
print(c1,c2)

'''
#id
'''
print(id(c2))
print(id(c1))
print(id('a'))
'''

# keyword cannot the variable
'''
import = 'keyword'
print (import)

Import = 'keyword'
print(Improt)
'''

#3.constant
'''
pi = 3.14
print(pi)

PI = 3.14
print(PI)

PI = 67
print(PI)

'''
# write a program to swap 2 number with 3rd variable and without 3rd variable
'''
a=10
b=35
temp=a
a=b
b=temp
print("after swapping a and b is ",a,b)
      
'''
#with variable
'''
n1=23
n2=10
print(n1,n2)
temp=n1
n1=n2
n2=temp
print(n1,n2)
'''
#without variable
'''
a,b=23,45
print(a,b)
a,b=b,a
print(a,b)
'''

# INBULIT FUNCTION IN PYTHON
#1.id()
'''
a='a'
print(a,id(a))
'''

#2. print()
x,y,z= 60,90,180
#sep is used to combine the
#prameters which is in same
# print statement
'''
print(x,y,z)
print(x,y,sep=',')
print(z,x,sep='5')
print(y,z,x,sep='a')
print(y,z,x,sep='-')
'''
#end is used to combine the
#parameter which is in differ
#print statement
'''
x,y,z= 60,90,180
print(x,end ='')
print(y,end=',')
print(z,end='-')
print(x,sep=',')
 '''    

#3.input
'''
print('ATM')
amount=input("Enter the amount :\n")
password=input("Enter the pin :\n")
print('Amount :',amount)
print('Pin :',password)
'''
#4. type
'print(type(amount),type(password))'
'''
a=45
print(type(a))
b='a'
print(type(b))
f=4.5
print(type(f))
tf=True
print(type(tf))
s='89a'
print( s,type(s))
'''

#5.help
'''
help('int')
help('str')
help('float')
'''
#6.dir
'print(dir(bool))'
'print(dir(float))'
#7.round
'''
print(round(2.4))
print(round(2.5))
print(round(5.6))
print(round(8.8))
print(round(7.4))
print(round(7.5))
'''

#precision
'''
print(round(4.5623,1))
print(round(4.5423,1))
print(round(4.5623,2))
print(round(4.5693,1))
print(round(101.347231,4))
print(round(101.347281,3))
print(round(101.347291,4))

'''

#8.divmod
'''
n1=45
n2=5
print('division', n1 / n2)
print('division',n1 // n2)
print('reminder',n1 % n2)

print(divmod(n1,n2))


'''
#9.abs
'''
print(abs(-34))
print(abs(3.4))
'''
#10.trunc
'''print(int(3.4))'''
'''
import math
print(math.trunc(3.4))
print(math.trunc(3.9))
print(math.trunc(51.45))
'''
'''
#15.ord
print(ord('t'),ord('l'),ord('&'))
#16.chr
print(chr(65),chr(100),chr(32))
'''
# 11.range

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
#12.enmurators
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
#create a dictonay with square of index and 1st  char of word
#program to add the number in same indexs
#13.zip

'''
l1=input("enter the list1:")
l2=input("enter the list2:")
print(list(zip(l1,l2)))
'''
'''
#14.zip longest
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

