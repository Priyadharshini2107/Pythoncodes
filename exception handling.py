
#------++ Inbulit error ++---------
'''
#1.import/module not found error
import non_module
#2.Index error
list_=[2,3,4]
print(list_(4))
#3.key error
dict_={'key':'value'}
print(dict_['key'])
#4.name error
a=10
print(b)
#5.type error
print(int([4,5,6]))
#6.value error
print(int('34asd'))
#7.Zero division error
print(23/0)
#8.Indentation error
for i in[3,4,5]:
#9.syntax error
print('hai'
#10.attribute error
import math
      print(math.Pi)

'''
#--------++ Type of Exception handling ++------------
#1.default Exception handling
'Zero division error'
'''
n1=int(input("enter the 1stnum:"))
n2=int(input("enter the 2nd num:"))
try:
      print(n1/n2)
except Exception:
      print("number cannot be divided by 0")
'''      

'type error'
'''
n1=input("enter the data:")
try:
          print(n1+3)
except Exception:
          print("please check the type")
'''
#2. specific Exception handling:
'''
n1=int(input("enter the 1stnum:"))
n2=int(input("enter the 2nd num:"))
d_={}
try:
      print(n1/n2)
      d[[4,5]]=90
      print(d)
except Zerodivisionerror:
          print("division by zero")
except Exception:
      print("number cannot be divided by 0")
'''
#3. multiple Exception handling:
'''
n1=int(input("enter the 1stnum:"))
n2=int(input("enter the 2nd num:"))
d_={}
try:
          print(n1/n2)
          d[[4,5]]=90
          print(a)
except ZeroDivisionError:
          print("division by zero")
except Type error:
          print("key must in immutable")

'''
#4.Generic Exception handling:
'''
n1=int(input("enter the 1st num:"))
n2=int(input("enter the 2nd num:"))
d={}
try:
          print(n1/n2)
          d[{4,5}]=90
          print(d)
except ZeroDivisionError as z:
          print(z)
except TypeError as t:
          print(t)
'''
#.(user want to create the own error)'custom expection handling'



#  syn:       pascal-case
#class ErrorName(Exception):
#         pass



#note rasie keyword it is used to manutualy tigger and exception
#and tis usefull when we wanted to singal that an error as orrued
#in the code



#synn:    raise ErrorName("message")

#example:::
'''
print(int('abc'))
'''
#example vote:
'''
class AgeError(Exception):
          pass
age=int(input("what is your age?"))
if age>=18:
          print("person is eligible to vote")
else:
          raise AgeError("person is not eligible to vote")#  we are raise the erroe

'''

#anotherway
'''
class AgeError(Exception):
          pass
age=int(input("what is your age?"))
try:
          if age>=18:
                    print("person is eligible to vote")
          else:
                    raise AgeError#  we are raise the erroe
except AgeError:
          print("person is not eligiable to vote")
'''

#module is the fiel containes the python definition functions vaiables
#and class that we can reuse the acorrs the deff program
#module helps the oragaining and strucred

#i. from modulename import m1,m2(to acess the specified method)
#ii.from modulename import *(to acess any method)
#iii. from modulename import mod as m1(to remane the method)
#iv.import modulename(to access the module)
#v.modulename.m1
#vi.import moduename as m1

#types of module
#i.user defind modlue(creating the new modules the labaries)2
#ii.In-bulit-module
























