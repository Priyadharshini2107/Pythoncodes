#string
'''
s1,s2='ha! guys1',"how- w@s y0ur weekend"
print(s1,s2, sep='\n')

s3=
'''

'''
print(s3)
s4= """
welcome to jspider
pyspider and qspider:)
"""
print(s4)
print(type(s4))

#constuctor
#1.
print(str())
'''
#2.typecasting
'''
i,f,c,b = str(34),str(3.4),str(3+4j),str(False)
print(type(i),i)
print(type(f),f)
print(type(c),c)
print(type(b),b)
'''
#to know no of characters
'''
s_=input("Enter a string:")
print("string :",s_,
      "It is length is :",len(s_))

'''
'''
str1="B@ng@!0r3"
print(id(str1))
print(str1,len(str1))
'''
#indexing
#starting character
'''
print(str1[0],str1[-9],
      str1[-len(str1)])
'''      
#ending
'''
print(str1[8],str1[len(str1)-1],str1[1])
print(id(str1[1]),id(str1[4]))
'''
#program to get the middle
#chacter of any string
#1.
str1="B@ng@!0r3"
middle_index= len(str1)//2
print(middle_index,str1[middle_index])

#2.
'''
str1=input("Enter :")
middle_index=len(str1)//2
print(middle_index,str1[middle_index])
'''
# program to get last 2character
#program to get the middle
#chacter of any string
#1.
'''
str1="B@ng@!0r3"
middle_index= len(str1)//2
print(middle_index,str1[middle_index])
'''
#2.
'''
str1=input("Enter :")
middle_index=len(str1)//2
print(middle_index,str1[middle_index])
'''
# program to get last 2character
1.
'''
s1=input("Enter a string:")
last_sec=len(s1)-2
print(s1[last_sec])
#2.
print(s1[-2])
'''
#2.slicing
'''
s2="It's cold here"
print(s2,s2[::],s2[0:len(s2):1])
print(len(s2))
#It's
print(s2[0:4:1],s2[:4:],
      s2[-len(s2):-10:])
#here
print(s2[-4::],s2[10::])
#cold
print(s2[5:9:],s2[-9:-5])
'''


#slicing
#when the step value is more then one
'''

s3= welcome to my channel:)
print(s3)
#chracter in even index
print(s3[0:len(s3):s2])

#chracter in even index
print(s3[::2])
#chracter in odd index
print(s3[1::2])
#welcome
print(s3[:7:])
#welcome skip odd index char
print(s3[:7:2])
#welcome skip even index chae
print(s3[1:7:2])
'''

#reversing the string
'''
s4= "welcome to my channel"
print(s4[::-1])
print(s4[len(s4):-len(s4)-1:-1])

#channel

print(s4[len(s4)-4:13:-1])#negative
print(s4[-4:-11:-1])#postive

#welcome to
print(s4[-12:-22:-1])#negative
print(s4[0:10:1])
print(s4[9::-1])#postive

#to my
print(s4[-9:-14:-1])
print(s4[12:7:-1])
''''

str1='slicing is tricky'

#ing is tr
print(str1[12:3:-1])
print(str1[-5:-14:-1])
#slicing

#is tricky
str1='slicing is tricky'

#ing is tr
print(str1[12:3:-1])
print(str1[-5:-14:-1])
#slicing
print(str1[6::-1])
print(str1[-11:-18:-1])
#is tricky
print(str1[16:7:-1])
print(str1[-1:-10:-1])

#slicing

str2='Welcome to my channel'
print(str2[::-1])
#reverse the string and skip odd index cha
print(str2[-1::-2])
#reverse the string and skip even index cha
print(str2[-2::-2])
#welcome -->reverse and skip odd index
print(str2[-15::-2])
print(str2[6::-2])
#to my--> reverse and skip even index
print(str2[-8:-14:-2])
print(str2[-9:14:-2])


#convention for variable
'''
mynameis='Ashwini'
print(mynameis)
#pascal case ---->classname
MyNameIs='Ashwini'
print(MyNameIs)
#camel case-->methoname
myNameIs='Ashwini'
print(myNameIs)
#snake case--->functionname
my_name_is='Ashwini'
print(my_name_is)
'''
#slicing
'''
str2='Welcome to my channel'
print(str2[::-1])
#reverse the string and skip odd index cha
print(str2[-1::-2])
#reverse the string and skip even index cha
print(str2[-2::-2])
#welcome -->reverse and skip odd index
print(str2[-15::-2])
print(str2[6::-2])
#to my--> reverse and skip even index
print(str2[-8:-14:-2])
print(str2[-9:14:-2])

'''

#string are immutable
'''
str4='Hai'
str4[0]='h'
print(str4)
'''

#method in string
#1.replace
'''
str1='hello world hello'
print(str1.replace('l','L'))
print(str1.replace('hello','hai'))
print(str1.replace('l','L',1))
print(str1.replace('o','@',2))
print(str1)
print(str1.replace('hello','hai'))
#exception
print(str1.replace('hlleo','hai'))

'''
#2.lower
'''
s_2=input("Enter the string:\n")
print(s_2.lower())
'''

#3.upper
'''
s_2=input("Enter the string:\n")
print(s_2.upper())
'''
#4.swapcase
'''
s_2=input("Enter the string:\n")
print(s_2.swapcase())
'''
#5.islower
'''
s_2=input("Enter the string:\n")
print(s_2.islower())
'''
#6.isupper
'''
s_2=input("Enter the string:\n")
print(s_2.isupper())
'''
#7.isalpha
'''
s_2=input("Enter the string:\n")
print(s_2.isalpha())
'''
#8.isnumeric
'''
s_2=input("Enter the string:\n")
print(s_2.isnumeric())
'''

#9.isalnum
'''
s_2=input("Enter the string:\n")
print(s_2.isalnum())
'''
#10.issapce
'''
s_2=''
print(s_2.isspace())
s_2=' '
print(s_2.isspace())
s_2='hai'
print(s_2.isspace())
'''
#11.startswithh
'''
str1=input("enter:")
sub_s=input("substring:")
print(str1.startswith(sub_s,0,len(str1)))
sub_s=input("substring:")
start_value=int(input("start-index"))
print(str1.startswith(sub_s,start_value))
'''
#12.endswith
'''
str1=input("enter:\n")
sub_s=input("substring:\n")
print(str1.endswith(sub_s,0,len(str1)))
sub_s=input("substring:")
end_value=int(input("end-index:"))
print(str1.endswith(sub_s, 0, end_value))
'''
#13.split
'''
str3="welcome to bangalore"
print(str3.split())
str3="welcome to-bangalore"
print(str3.split())
str3="welcome-to-bangalore"
print(str3.split())
'''
#separator
'''
str3="welcome-to-bangalore"
print(str3.split('-'))
print(str3.split('to'))
print(str3.split('a'))
'''
#maxsplit

str3="welcome to bangalore-"
print(str3.split('o'))
print(str3.split('o',11))
print(str3.split(' ',2))

#14.rsplit
# 15.index
'''
str1=input("Enter :\n")
sub_string=input("Enter the sub_s:\n")
print(str1.index(sub_string))
sub_string=input("Enter the sub_s:\n")
str_index=int(input())
print(str1.index(sub_string,str_inde))
'''
#exception
'''
str1=input("Enter :\n")
sub_string=input("Enter the sub_s:\n")
print(str1.index(sub_string))
'''
#16.find
'''
str1=input("Enter :\n")
sub_string=input("Enter the sub_s:\n")
print(str1.index(sub_string))
sub_string=input("Enter the sub_s:\n")
str_index=int(input())
print(str1.index(sub_string,str_inde))
'''
#--
'''
str1=input("enter :\n")
sub_string=input("Enter the sub_s:\n")
print(str1.index(sub_string))
'''
#17.count
'''
str4="Good morning maam"
print(str4.count("o"))
print(str4.count("Good"))
print(str4.count("a"))
print(str4.count("m"))
print(str4.count("1234"))
print(str4.count("o",2))
'''
#--- to remove character from the string(strip,lstrip,restrip)
#18.strip
'''
str5=input("enter:\n")
char_=input("enter:\n")
print(str5.strip(char_))
'''
#19.lstrip

str5=input("enter:\n")
char_=input("enter:\n")
print(str5.lstrip(char_))


#20.rstrip
'''
str5=input("enter :\n")
char_=input("enter :\n")
print(str5.rstrip(char_))
'''
#21.join
# for list
'''
L_=["a",'b',"7"]
print(''.join(L_))
print('-'.join(L_))
print('8'.join(L_))
print(' '.join(L_))
print('i'.join(L_))
'''
# for tuple
'''
t_=("a",'b',"7",'apple','6')
print(''.join(t_))
print('*'.join(t_))
'''
#for set
'''
s_=("a",'b',"7",'apple','6')
print('-'.join(s_))
'''
#for dict
'''
d_=("a": 8,'b': 4.5,"7": 34)
print('@'.join(d_))
'''
# for string
'''
str_="hello"
print('-'.join(str_))
'''
#operator in steing
# +,*
#adition
'''
str1=input("Enter the string:")
str2=input("Enter the string:")
print(str1+str2)
'''
#mutiple
'''
str1=input("enter the string:")
str2=input("enter the string:")
print(str1*2)
'''

#LIST
#2.List(data type)

#homogenous
'''
list1=[23,45,12,895,34,23]
print(list1)

#heterogeneous

list2=['23',[45,12,895],34.5,23,3+6j,False,0]
print(list2)
print("length of else:\n",len(list2))

#typecasting
print(type(list2))

#constructor
#default value

print(list())
'''
#type casting
#string to list
'''
#according character 
print(list('banggalore is in kar'))
#acoording to word
print('bangalore is in kar',split())
#tuple into list
print(list(('bangalore',34,4.5)))
#set into list
print(list({'bangalore',34,4.5}))
#dictionary into list
print(list({'bangalore':45,34:45,4.5:True}))
'''
#indexing of list
''''

list2=['23',[45,12,'895'],34.5,23,3+6j,False,0]

print(list2[0])
print(list2[len(list2)-2])
print(list2[-6],list2[1])
print(list2[1][1],list2[-6][-2])
print(list2[1][2],list2[-6][-1])
print(list2[1][2][1],list2[-6][-1][-2])
'''
#slincing
'''
#1.program to get even index element
list2=['23',[45,12,'895'],34.5,23,3+6j,False,0]
print(list2[0::2])

#2.progaram to get odd index element
list2=['23',[45,12,'895'],34.5,23,3+6j,False,0]
print(list2[1::2])
#3.program to get reverse the list
list2=['23',[45,12,'895'],34.5,23,3+6j,False,0]
print(list2[::-1])
#4.program to get even index element in reverse order
list2=['23',[45,12,'895'],34.5,23,3+6j,False,0]
print(list2[-1::-2])
#5.program to get odd index element in reverse order
list2=['23',[45,12,'895'],34.5,23,3+6j,False,0]
print(list2[-2::-2])
#6.reverse the nested list[45,12,'895']
list2=['23',[45,12,'895'],34.5,23,3+6j,False,0]
print(list2[1]::[-1])
#7.reverse the string'23
'''
#[34.5,23,3+6j]
list2=['23',[45,12,'895'],34.5,23,3+6j,False,0]
'''
print(list2[2:5:])
print(list2[-3:-6:-1])

''''
#[23,3+6j,False,0]
'''
print(list2[3:len(list2)])
print(list2[:-5:-1])

#[23,Flase]
print(list2[-2:-5:-2])
#[False,23]
print(list2[-2:-5:-2])
'''
#list mutable
'''
li2=[445,3.5,2.3,'hey',[True,False]]
li2[-2]='HEY'
print(li2)
'''

#slicing
''''
li2=[45,3.5,2.3,'hey',[True,False]]
li2[0:2]=[34,67]
print(li2)
li2[-2::]=['apple']
print(li2)
li2[2:4]='apple'
print(li2)
'''
#  i.methods in list
#1.append
'''
list1= [34.5,'arun',43,{1,2,3,4},[True,False]]
list1.append(3+4j)
list1.append('kalps')
print(list1)
'''
#2.Extend
'''
list1=[34.5,'arun',43,[True,False]]
list1.extend('hai')
list1.extend(['hai',43,False,78])
print(list1)
'''
#3.Insert
'''
list1=[34.5,'arun',43,{1,2,3,4}]
list1.insert(0,'bangalore')
list1.insert(4,45)
print(list1)
'''

#ii.Removing element from the list
#1.pop
'''
l2=[56,31,78,21,89]
l2.pop()
l2.pop(2)
print(l2)
'''
#2.removing
'''
l2=[56,31,78,31,89,89,56]
l2.remove(31)
l2.remove(56)
print(l2)
'''
#3.del
#'del'
l2=[56,31,78,21,89,89,56]

#'indexing'
'''
del l2[4]
del l2[-1]
print(l2)
'''
#'slicing'
'''
del l2[:2]
print(l2)

del l2[2:5]
print(l2)

del l2[::2]
print(l2)

del l2[1::2]
print(l2)

'''
# method in list
#1.reverse
'''
l3=['a',45,4.5,[4.3],True]
print(l3[:-1])
l3.reverse()
print(l3)

'''
#2.Index
'''
l3=['a',45,0,4.5,[4,2],True,1,False]
print(l3.index(False))
print(l3.index(False,3))
print(l3.index('a'))
print(l3.index(1))
'''
#count
'''
l3=['a',45,0,4.5,[4,5],True,1,False]
print(l3.count('a
'))
print(l3.count(True))
print(l3.count([3,4]))
'''
#sort
'''
list_=[3,4,12,78,78,0,1]
list_.sort()
print(list_)
list_.sort(reverse - False)
print(list_)
list_.sort(reverse - True)
print(list_)

'''
'''
li=['apple',"Apple",'graphes','van','wayand','TN',"avacado"]
print(li)
'''
#ex:
'''
l_=["3+4j","1+4j","3+5j"]
l_.sort()
print(l_)
'''
'''
l_=[True,False]
l_.sort()
print(l_)
'''

#copying list
#1.normal copying
'''
li_1=['apple',"Apple",['graphes','van','wayand'],'TN',"avacado"]
print(li_1)
print(id(li_),id(li_1))
'''
#2.shallow copy
'''
li_=['apple',"Apple",['graphes','van','wayand'],'TN',"avacado"]
li_1=li_
print(li_)
print(li_1)
print(id(li_),id(li_1))
print(id(li_[2],id(li_1[2])))
'''
#3.deep copy
'''
from copy import deepcopy
li_=['apple',"Apple",['graphes','van','wayand'],'TN',"avacado"]
li_1=deepcopy(li_)
print(li_)
print(li_1)
print(id(li_),id(li_1))
print(id(li_[2]),id(li_1[2]))
''''
#opertaor
'+''*'
'''
list1=['apple','mango']
list2=['cat','dog']
print(list1+list2]
print(list2*3)
'''
#TUPLE
T_=(45,4.5,'hau',(4,5),[23,5],54)
print(T_)
print(type(T_)

#construor
      str,list,set,dict
      #method in tuple
#count
      t_=(13,45,67,8.9,(4,))
      print(t_.count((4))
#index
'''
t_=(3,4,2.3,'apple',(4,),3.0)
print(t_.index(2.3))
print(t_.index(3))
print(t_.index(3,1))
print(t_.index('apple'))

#slincing
#1.program to get even index element

tuple2=('23',[45,12,'895'],34.5,23,3+6j,False,0)
print(tuple2[0::2])



#2.progaram to get odd index element

tuple2=('23',[45,12,'895'],
        34.5,23,3+6j,False,0)
print(tuple2[1::2])

#3.program to get reverse the list

tuple2=('23',[45,12,'895'],34.5,23,3+6j,False,0)
print(tuple2[::-1])


#4.program to get even index element in reverse order

tuple2=('23',[45,12,'895'],34.5,23,3+6j,False,0)
print(tuple2[-1::-2])

#5.program to get odd index element in reverse order

tuple2=('23',[45,12,'895'],34.5,23,3+6j,False,0)
print(tuple2[-2::-2])

#[34.5,23,3+6j]

tuple2=('23',[45,12,'895'],34.5,23,3+6j,False,0)

print(tuple2[2:5:])
print(tuple2[-3:-6:-1])

#operator
'+','*'

tuple1=('good','hello',34,12)
tuple2=('cow','dog',23,12)
print(tuple1+tuple2)
print(tuple1*@12)
'''
            #SET
            #hash()(deose not have hash value)
#'__hash__()(method or magic method or tender method

print('a'__hash__())
print(hash(4,5,6))
print(hash(4,5))
print(hash[True,False])

#type and len
'''
set_={'a',(4,),45,4.5,3-4j,False,'a'}
print(set_)
print(type(set_))
print(set())
print(len(set_))
'''
#typecasing
'''
print(set("hello"))
print(set([3,4.5,(4,5),(4,)]))
print(set((3,4.5,(4,5),(4,))))
print(set({'a':1,'b':2,'c':3}))
'''   


#methods
#adding two are more method
#1.add
'''
set_.add("shivam")
set_.add("jagatjit")
set_.add((3,4))
print(set_)
'''
#2.unioin
'''
set_1={'a',(4,),45,4.3,3-4j,False.'a'}
set_2={'a','b','c'}
set_3={4.5,3+4j,'kiwi',(9,8)}
print(set_1.union(set_2))
print(set_2.union(set_1,set_3))
'''
#3.update
'''
set_1={'a',(4,),45,4.3,3-4j,False.'a'}
set_2={'a','b','c'}
set_3={4.5,3+4j,'kiwi',(9,8)}
set_1.update(set_3)
print(set_1)
set_3.update(set_2,set_1)
print(set_3)
'''
'''
#removing the key from the set
#!.pop
set_1={'a',(4,),45,4.3,3-4j,False,'a'}
st_1.pop()
print(set_1.pop()
print(set_1)

#2. remove
set_1={'a',(4,),45,4.3,3-4j,False,'a'}
set_1.remove((4,))
print(set_1)
#key error(disadvantage)
set_1.remove((23))
print(set_1)

#3.discard
set_1={'a',(4,),45,4.3,3-4j,67,'a'}
set_1.discard((67))
print(set_1)

#'----'
set_1.discard((23))
print(set_1)
'''
#To get common key in set
#i.intersection
#ii.intersection_update

#i.intersection
'''
set_1={'a',(4,),45,4.3,3-4j,False,'a'}
set_2={'a','b','c'}
set_3={4.5,3+4j,'kiwi',(9,8)}
print(set_1.intersection(set_2))
print(set_2.intersection(set_1,set_3))
'''
#i.intersection _update
'''
set_1={'a',(4,),45,4.3,3-4j,False,'a'}
set_2={'a','b','c'}
set_3={4.5,3+4j,'kiwi',(9,8)}
set_2.intersection_update(set_1)
print(set_2)
set_1.intersection_update(set_2,set_3)
print(set_1)
'''

#to get uncommon keys in set
#i.differrance
'''

set_1={'a',(4,),45,4.3,3-4j,False,'a'}
set_2={'a','b','c','ab'}
set_3={4.5,3+4j,'kiwi',(9,8),'ab'}
print(set_2.difference(set_2))
print(set_3.difference(set_2,set_1))
'''

#ii.difference_update
'''
set_1={'a',(4,),45,4.3,3-4j,False,'a'}
set_2={'a','b','c'}
set_3={4.5,3+4j,'kiwi',(9,8)}
set_3.difference_update(set_1,set_2)
print(set_3)
set_2.difference_update(set_1)
print(set_2)
'''
#iii.symertic difference
'''
set_1={'a',(4,),45,4.3,3-4j,False,'a'}
set_2={'a','b','c','ab'}
set_3={4.5,3+4j,'kiwi',(9,8),'ab'}
print(set_2.symmetric_difference(set_1))
print(set_1.symmetric_difference(set_3))
print(set_3.symmetric_difference(set_2))
'''

#iv.symetric _difference_update
'''
set_1={'a',(4,),45,4.3,3-4j,False,'a'}
set_2={'a','b','c','ab'}
set_3={4.5,3+4j,'kiwi',(9,8),'ab'}
set_3.symmetric_difference_update(set_1)
print(set_3)
set_1.symmetric_difference_update(set_2)
print(set_1)
'''

#5.issubset
'''
s1={3,'a','&%^',9.8}
s2={3,'a',3+4j,'&%^',9.8,(45,),56.4}
print(s1.issubset(s2))

s1={3,'a','&%^',9.8}
s2={3,'a',3+4j,'&%^',(45,),56.4}
print(s1.issubset(s2))

'''
#6.issuperset
'''
s1={3,'a','&%^',9.8}
s2={3,'a',3+4j,'&%^',9.8,(45,),56.4}
print(s2.issuperset(s1))
print(s1.issuperset(s2))
'''
#7.isdisjoint
'''
s2={3,4,5,7}
s3={34,56,12,4.5}
print(s2.isdisjoint(s3))
'''
'''
#operator
#'-'

s_={3,4,5.5}
s_1={4,'kiwi',55}
print(s_-s_1)

#'^'

s_={3,4,5.5}
s_1={4,'kiwi',55}
print(s_^s_1)

#'&'

s_={3,4,5.5}
s_1={4,'kiwi',55}
print(s_&s_1)

#'|'

s_={3,4,5.5}
s_1={4,'kiwi',55}
print(s_|s_1)
'''
        #dictionay
'''
dict_={'a':[4,5,6],(True,):{3,4,5},67:4.5,False:True,'a':45,'c':[4,5,6]}
print(dict_)
print(type(dict_))
print(len(dict_))
print(dict())
'''
'''
#typecasing#1. equal to =
print(dict(a=1,b=2.6,c=45))
'''
'''
#2.tuple with list
print(dict([(34,'int'),[3.4,[4,5]],['a','b'],[34,5]])
#3.
print(dict(((34,'int'),[3.4,[4,5]],['a','b'],[34,5])))
#4.
print(dict({(34,'int'),(67,8),'45'}))
'''

#method in dictionary
      #1.to get value from the dictionary
      #i.Indexing
'''
dict_={'a':[4,5,6],(True,5):{3,4,5},67:4.5,False:True,
       'a':45,'c':[4,5,6],(1,5):'set'}
print(dict_['a'])
print(dict_[0])

#composite
print(dict_[(True,5)])
print(dict_[True])
'''
#get
'''
dict_={'a':[4,5,6],(True,5):{3,4,5},67:4.5,False:True,
       'a':45,'c':[4,5,6],(1,5):'set'}
print(dict_.get(67))
print(dict_.get(1))
print(dict_.get(1,'no value'))
print(dict_)
'''
            #3.key
'''
d_={'a':'string',3:'int',3.4:'f',(4,5,6):[True,False]}
print(d_.keys())
'''
#4.values
'''
d_={'a':'string',3:'int',3.4:'f',(4,5,6):[True,False]}
print(d_.values())
'''
#5.items
'''
d_={'a':'string',3:'int',3.4:'f',(4,5,6):[True,False]}
print(d_.items())
'''
#adding keys valuesinto a dictionary
#i.indexing
'''
d_={'a':'string',3:'int',3.4:'f',(4,5,6):[True,False]}
d_[True]=False
d_[(90,4)]='tuple'
print(d_)
'''
#ii.update
'''
d_={'a':'string',3:'int',3.4:'f',(4,5,6):[True,False]}
d_.update({90:3.4,4+4j:3-4j,'abc':'alpha'})
d_.update([[45,45],(3.4,'hai'),'ab',{True,(False,5)}])
print(d_)
'''
#removing key-value paire from dictionary
#i.popitem
'''
d_={'a':'string',3:'int',3.4:'f',(4,5,6):[True,False]}
d_.popitem()
d_.popitem()
d_.popitem()
print(d_.popitem())
print(d_)
'''
#ii.pop
'''
d_={'a':'string',3:'int',3.4:'f',(4,5,6):[True,False]}
d_.pop(3,4)
d_.pop((4,5,6))
print(d_)
'''
#fromkeys
'''
string_='string'
print(dict.fromkey(string_))
print(dict.fromkey(string_,'str'))
'''
'''
list_=[3,4,5]
print(dict.fromkeys(list_,'int'))
'''
'''
tup_=('a',)
print(dict.fromkeys(tup_))
'''
'''
set_={(90),'kiwi',3.4,56,False}
print(dict.fromkeys(set_,'key'))
'''
#opertators in dictionary
'''
d_1={3:4.5,4.4:'float',5:[5,6,7],'6':'a'}
d_2={0.4:45,'4.4':'float',5.3:[5,6,7],'69':'a'}
print({*d_1,*d_2})
'''
'''
d_1={3:4.5,4.4:'float',5:[5,6,7],'6':'a'}
d_2={0.4:45,'4.4':'float',5.3:[5,6,7],'69':'a'}
print(d_1|d_2)
'''











