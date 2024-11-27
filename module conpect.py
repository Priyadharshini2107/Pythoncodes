
#----------++ inbult module ++-----
#1.os
     # os module in python prodces a way to inact with operaating system it
     #offer func to work with dictory files parth etc...
'''     
#i.mkdir(make or create)
import os
os.mkdir('directory1')
os.mkdir('directory2')

#ii.getcwdOS.mkdir('directory1')

print(os.getcwd())

#iii.chdir(chage)
os.chdir('directory1')
print(os.getcwd())

with open(file1,'x')as f1:
          print(f1)
print(os.getcwd())

#iv.listdir
#syn os.listdir(path=".")
print(os.listdir())
print(os.listdir(path='directory'))
     
#v.rmdir(remove)
print(os.rmdir('directory2'))
print(os.rmdir('dicrectory1'))

#vi.remove
current_path1=os.getcwd()
print(cuurent_path1)
os.chdir('directory1')
current_path2=os.getcwd()
print(cuurent_path2)
os.remove('file1')
os.rmdir('directory1')

#vii.rename
print(os.getcwd())
print(os.rename('M14.py','morining14.py'))

#viii.repalace
print(os.getcwd())
os.repalce(f1,f2)
'''
'''
#datetime
#this module class for produce manuplated dates and times

#i.datetime
#it is used to create a date and time form the

from datetime import datetime,timedelta
date_time=datetime(2025,8,3,1,25,45)
print(date_time)
print(date_time.strftime('%Y:%m:%d%H-%M-%S'))
print(date_time.date())
print(date_time.time())
# today date and time
print(datetime.today())
print(datetime.now())


#ii. timedelta
date_time=datetime(2025,8,3,10,25,45)
'update'
change_date=timedelta(days=10)
print(date_time+change_date)
print(date_time-change_date)

'update time'
change_time=timedelta(seconds=120)
print(date_time+change_date)
print(date_time-change_date)

'''
'''
#time
#i.time-to known the excution time taken syn:time.time()
import time
start_time=time.time()
print('hai')
eend_time=time.time()
print(start_time-eend_time)

#ii.sleep-to pass excution time syn:time.slepp(second)
time.sleep(5) 
print('hai')
'''

#collections

#i.defaultdict- it is user to produce the default alues for a dictionary which means
# if we try to access or modifiy the key that does not exit in dictionary
#defalut dict will automatically crete with default value
'''
'program to create a dictionary with character and its count'

str_='banana is a fruit'
'method'
print({char:str_.count(char)for char in str_})
'without method'
dict_={}
for c in str_:
          if c not in dict_:
                    dict_[c]=1
          else:
                    dict_[c]+=1
print(dict_)

# defaultdict ex:
from collections import defaultdict
dict_=defaultdict(int)
for c in str_:
          dict_[c]+=1
print(dict_)    
 '''         
#ii.deque
'''

from collections import deque


#i.rotate (shift the values)

set_=[3,4.5,2,True]
deque_=deque(set_)
deque_.rotate(1)#rigth to left(+ve)
print(deque_)
deque_.rotate(3)
print(deque_)

deque_.rotate(-1)#left to rigth (-ve)
print(deque_)
deque_.rotate(-4)
print(deque_)

'''
#--------------- ++  Generator ++ -----------------
#i.generator function
'''
def func():
          for i in range(1,5):
                    yield i
                    yield i
z=func()
print(func())
print(func())
print(list(func()))
print(list(func()))

#next () or __next__
print(next(z))
print(next(z))
print(z.__next__())
print(z.__next__())
print(next(z))

'''
#ii.generator expression/compersion
'''
print(tuple(i for i in range(1,5)))
print(tuple(i for i in range(1,5)if i%2==0))
z=(i*i if i%2==0 else i**3 for i in range(1,5))
print(next(z))
print(z.__next__())

'''
#--------------- ++ Interator ++ ----------------
#types of iter
#1.inbuit iter
#2.custoum iter

#1. Inbuit iter
  #i.iter()
  #ii.next()
'''
l=[1,'hai',4.5]
for ele in l:
          print(ele)
iter_=iter(l)
print(next(iter_))
print(next(iter_))
print(next(iter_))
print(next(iter_))

'''
#2.customer iterator
    #__iter__
    #__next__
'''
class MyIteration:
          def __int__(self,data):
                    self.data=data
                    self.index=0
          def __iter__(self):
                    return self
          def __next__(self):
                    if self.index<len(self.data):
                              item=self.data[self.index]
                              self.index+=1
                              return item
                    else:
                              stopiteration
n=MyIteration([1,'hai',4.6])
for i in n:
          print(i)
'''

#------------------- ++ Decorator ++ -------------------
'''
def outer(func):
          def wrapper():
                    print('Good Afternoon')
                    return wrapper
          @outer
          def function():
                    print('hai')
          function()
'''
#@outer
'''
def outer(func):
          def wrapper(arg):
                    print(len(arg)*'*')
                    func(arg)
                    print(len(arg)*'*')
          return wrapper
@outer
def f1(arg):
          print(arg)
f1("decorator is not easy")

'''
#looging decrator
'''
def log_deccorator(func):
          def inner(*args,**kwargs):
                    print('calling function{func__name__} with agrs {args} and kargs{kwargs}')
                    result=func(*args,*kwargs)
                    print('{function__name__} returns{results}')
                    return inner
          @log_decorator
          def add(x,y):
                    return x+y
          @log_decorator
          def sub(x,y):
                    return x-y
          add(3,1)
          sub(10,3)

'''
#Time decorator
'''
import time
def time_decorator(func):
          def inner(*agrs,**kwagrs):
                    start_time=time.time()
                    func(*args,**kwagrs)
                    end_time=time.time()
                    execution_time=end_time-start_time
                    return f'functio{func__name__}took{execution_time}second'
          return inner
          @timedectorator
          def slow_function(seconds):
                    time.sleep(second)
                    return f'function completed after{second} second'
                    print(slow_unction(4))
          @timedecorator
          def slow_function(second):
                    time.sleep(seconds)
                    return f'function completed after{second}seconds'
          print(slow_function(10))          


'''
#5.create a dictionary with function name and count of finction
'''
count=0
dict_={}
def outer (func):
          def wrapper(*agrs,**kwagrs):
                    func()
                    global count_
                    count+=1
                    dict_[func__name__]=count
                    return wrapper
          @outer
          def count_calls():
                    print("hello!...")

count_calls()
count_calls()
count_calls()
count_calls()
'''

#6.Authorization decorator
'''
def authorization_decorator(func):
          def inner(user):
                    if user.get('is_auth'):
                              return func(user)
                    else:
                              return'unauthorized access'
                    return inner
          @authorization_decorator
          def get_secret_data(_):
                    return "this is very secert data"
          @authorization_decorator
          def get_secret_data(_):
                    return"this is very secert data"
          
user1={'username':'pava',is_auth:True}
user2={'username':'nithya',auth:False}
print(get_secret_data(user1))
print(get_secret_data(user2))

'''
#json and pickel
#json
'''
student_details={'name':'priya','age':20,'subject':['python','sql','html-css-js']}
'serilazation'

import json
json_obj=json.dumps(student_details)
print(type(json_obj))


'de-serilazation'
python_obj=json.loads(json-obj)
print(type(json-obj))
'''

#pickel
'''
student_details={'name':'priya','age':20,'subject':['python','sql','html-css-js']}
'serilazation'

import pickle
pickel_obj=pickle.dumps(student_details)
print(type(pickel_obj))


'de-serilazation'
python_obj=pickle.loads(pickel_obj)
print(type(python_obj))

'''
#9.Regular experssion
#search
'''
import re
string_="Hi,my email is A@gmail.com"
pattern=input("parttern:")
print(re.search(pattern,string_))

'''
#match
'''
email=input("enter:")
pattern=input("pattern:")
print(re.match(pattern,email))

'''
#findall
'''
string_="hi,my email is A@gmail.com"
pattern='m'
print(re.findall(pattern,string))
pattern='ma'
print(re.findall(pattern,string))
'''


#Finditer
'''
password="password:1234123465432"
pattern=input("enter:")
for index in re.finditer(pattern,password):
          print(pattern,'-->start_index:',index.start(),'end_index:',index.end())

'''

#sub/subn

password="password:1234123465432"
print(re.sub('1234','4532',password))
print(re.sub('1234','4532',password))
























































