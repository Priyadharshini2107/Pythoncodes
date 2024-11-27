   # 1.class and object
'''
class  MaruthiSuzuki:
          car_name='swift'
          color='white'
          fuel='petrol'
          gear='manual'
car1=MaruthiSuzuki()
car2=MaruthiSuzuki()
'accessing'
#class name
print(MaruthiSuzuki.car_name)
print(MaruthiSuzuki.gear)
#object name
print(car1.color)
print(car2.fuel)
'modifying'
#class name
'modifying in class will make change in the object too'
print(MaruthiSuzuki.color)
MaruthiSuzuki.color='red'
print(MaruthiSuzuki.color)
print(car1.color,car2.color)
#object nname
print(car1.gear)
car1.gear='auto'
print(car1.gear)
print(car2.gear)
print(MaruthiSuzuki.gear)
'''
#2.Instance variable
'''
'object have the same data'
class College:
          college_name="sona"
def __init__(self):
          self.stu_name='priya'
          self.regno=70
          self.branch='cs'
          self.age=20
print(self.stu_name,self.regno,self.branch,self.age,self.college)
student1=College()
print(College.college_name)
print(student1.college_name)
print(student1.brach)
student2=College()
print(College.college_name)
print(student2.age)
print(student2.regno)


'''
'''
'objec have diffternt data'
class College:
          college_name='Audi-sakara'
          def __init__(self,name,regno,branch,age):
                    self.student_name=name
                    self.registerno=regno
                    self.branch=branch
                    self.age=age
          print(self.student_name,self.registerno,self.branch,self.age)
student1=College('ashwini',3,'cs',23)
student2=College('sanker',45,'AI',43)
'''
#method
#1.instance method
'''
class Iphone:
          phone_name='15pro'
'instance variable'

          def __init__(self,storeage,camera,ram,color):
                    self.storeage=storeage
                    self.camera=camera
                    self.ram=ram
                    self.color=color
'instance method'
          def phone_details(self):
                     print(

                        storeage:self{storeage}
                        camera:self{camera}
                        ram:self{ram}
                        color:self{color}
                        )
phone1=Iphone(256,'12px',16,'blue')
phone1.phone_details()
Iphone.phone_details(phone1)s
'''
#2. class method
'''
class Iphone:
          phon_name='15pro'
          def __init__(self:stroage,camera,ram,color):
                    self.stroage=storeage
                    slef.camera=camara
                    self.ram=ram
                    self.color=color
          def phone_details(self):
                    print(
                        storeage:self{storeage}
                        camera:self{camera}
                        ram:self{ram}
                        color:self{color}
                        )
          self.phonr.phone_name='oneplus'
          print(self.phone_name)
          @classmethod
          def details2(cls):
                    print(cls.phone_name)
                    cls.phone_name='redmi
                    print(cls.phonee_name)
phone1=Iphone(256,12px,16,blue)
phone1.phone_details()
Iphone.phone_details(phhone1)
Iphone.details2()
phone1.details2()
'''
#3.static method
'''
class Iphone:
          phon_name='15pro'
          def __init__(self:stroage,camera,ram,color):
                    self.stroage=storeage
                    slef.camera=camara
                    self.ram=ram
                    self.color=color
          def phone_details(self):
                    print(
                        storeage:self{storeage}
                        camera:self{camera}
                        ram:self{ram}
                        color:self{color}
                        )
          self.phonr.phone_name='oneplus'
          print(self.phone_name)
          @staticmethod
          def details3():
                    print('static_method is independent of self and cls')
                    print([i for i in range(1,11)])
                    phone1.details3()
                    Iphone.details3()'''

             #-----------Example programs--------------



#1.calculation program
'''
class Calculation:
          def __init__(self,stu_name,stu_rn,marks):
                    self.student_name=stu_name
                    self.stydent_rn=stu_rn
                    self.student_mark=marks
          def student_details(self):
                    return 
student_name:{self.student_name}
student_reg_no:{self.student_rn}]
          def total_marks(self):
                    return sum(sef.student_mark)
          def average_mark(self):
                    return self.total_marks()/len(self.student_name)
          def percentage(self):
                    return self.total_marks()*100
student1=Calculation('nithya',65,[85,67,92])
print(student1.student_details())
print("the total marks is",student1.total_mark())
print(student1.average_mark())
print(student1.percentage())
'''

#2.atm
'''
class ATM:
          
          def __init__ (self,per_name,am_,lang_):
                    self.person_name=per_name
                    self.amount=am_
                    self.language=lang_
          def Bank_Account(self):
                    return(f'''#person_name:{self.person_name}
#amount:{self.amount}
''')
          def deposite(selt,amt_dep):
                    self.amount+=amt_dep
                    return self.amount
          def withdraw(self,amt_withdraw):
                    if self.amount>=amt_withdraw:
                              self.amount-=amt_withdraw
                              return slef.amount
                    else:
                    print("invalid balance")
          def diplay (self):
                    return(f person_name:{self.person_name}
amount:{self.amount})
person1=ATM('shivani',2500,'English')
print(person1.Bank_Account())
print("The person deposite:",person1.deposite(1000))
print("The person withdraw:",person1.withdraw(500))
print("The person total amount:",person1.display())
                    
 '''                 
#3. recatangel and width length and area perimeter
'''
class Rectangle:
    def __int__(self,length,width):
        self.lenght=length
        self.width=width
        def d1(self):
            return f
length:{self.length}
width:{self.width)
        def area(self):
          return (self:length*self.width)
        def perimeter(self):
          return(self.length+self.width)*2
data1=Rectangle(2,4)
print(data1.d1())
print(data1.area())
print(data2.perimeter())
'''
#4.calculation of some program in string
'''
class String:
          def __init__(self,str_):
                    self.String=str_
                    def Program(self):
                              return f#self.string={self.string}
                    def reversestring(self):
                              n=input("enter a string:")
                              st_=''
                              i=0
                              while(i<len(n)):
                                        st_=n[i]+st_
                                        i+=1
                                        return st_
                              def addingstring(self):
                                        str1=input("enter:")
                                        str2=input("enter:")
                                        return str1+str2
                              def iterablestring (self):
                                        stri_=input("value")
                                        return(','.join(stri_))
                              def middlechar(self):
                                        list_=input("Enter:").split()
                                        for word in list_:
                                                  w_=(word[-1])
                                        return(chr(ord(w_)))
                    string1=String("hello world")
                    print(string1.Programs())
                    print("Reverse a string:",string1.reversestring())
                    print("Adding 2string:",string1.addingstring())
                    print("iterable into string:",string1.iterablestring())
                    print("Middle character:",string1.middlechar())
                    '''
#5.calculate word 1 and word2
'''
class ClassName:
          def __init__(self,w_1,w_2):
                    self.s1=w_1
                    self.s2=w_2
          def d_(self):
                    return fw1={self.s1}
w2={self.s2}
          def display(self):
                    new_str=''
                    for a,b in zip(self.s1,self.s2):
                              new_str+=a
                              new_str+=b
                    return new_str
          str1=ClassName('abc','pqr')
          print(str1.d_())
          print(str1.display())
'''
#6.Repeated word return true otherwise false
'''
class A:
          def __init__(self.l1):
                    self.w1=l1
          def word_(self):
                    return f#l1={self.w1}
          def display(self):
                    l1='ab ab'.split()
                    d_=self.w1.split()
                    for word in l1:
                              
                              if word not in d_:
                                        return False
                              else:
                                        return True
          va1=A('abab')
          print(va1.wor_())
          print(va1.display())'''
                    
                    
#.
'''
a=input("enter :")
d_s=a*2
m_s=d_s[1:-1:]
if a in m_s:
          print(a.count(a[:2]),"times repeated")
else:
          print(False)


'''        
#----another method-----
''''
class C:
          
          def
          def __init__(self):
                    self.str_=''
          def repeated_(self):
                    self.m_s=(self.a_+self.a_)[1:-1]
          if self.a_ in self.m_s:
                    for char in self.a_:
                              if char not in selt.str_:
                                        self.str_+=char
                    print("{self.str_},is reperated,{self.a_.count(self.a_[:len(str_)])})
           else:
                print(False)
a1=C()
print(C)

'''

#---------------------- ++ Inheritance ++ ------------------------

#types
#1.Single level inheritance
'''
class SuperClass:
          'class variable'
          
          class_name="superclass"
          'instance variable'
          def __init__ (self):
                    print('In superclass')
          def instance_me(self):
                    print(self.class_name)
class Subclass(SuperClass):
          def __init__(self):
                    print("In subclass")
                    super().__init__()
obj1=Subclass()
print(obj1.class_name)
obj1.instance_me()
'''
#2.Multiple level inheritance
'''class BassClass2:
          def __init__(self):
                    self.a=20
class SubClass(BassClass1,BassClass2):
          def __init__(self):
                    self.a=50
                    print(self.a)
                    super().__init__()
                    print(self .a)
c1=SubClass()
print(c1.a)                    

'''

#3.Multi level inheritance
'''
class BaseClass1:
          def __init__(self):
                    self.a=10
          def display_(self):
                    print('method in BaseClass')
class SubClass1(BaseClass1):
          def __init__(self):
                    self.a=20
                    print(self.a)
                    super().__init__()
class SubClass2 (SubClass1):
          def display_(self):
                    print(self.a)
obj1=SubClass2()
print(obj1.a)

'''                          
#4.hiersrchical-level
'''
class BaseClass:
     def __init__(self):
          self.a=10
          print(self.a)
     def dispaly_(self):
               print("method in baseclass")
class Subclass1(BaseClass):
          def __init__(self):
                    print('In subclass')
                    super().__init__()
class Subclass2(BaseClass):
          def display_(self):
                    print('method in subclass')
                    super().display()
obj1=Subclass1()
obj1.display()
obj2=Subclass2()
obj2.display()
'''

# ------------- ++ Encapsulation ++ ---------------
#public,protected,private
'''
class Atm:
     bank=input("bank-name?")
def __init__(self,lan_,balance,pin):
     self.language=lan_
     self._amount=balance
     self.__password=pin
def object_method(self):
     print(f
language:{self.language},
balance:{self._amount},
pin:{self.__password})
@classmethod:
     def __class_method(cls):
          print(cls.bank)
user1=Atm(Tamil,500,1234)
print(user1.language)
print(user1._amount)
print(user1.__password)
user1.object_method()
user1.__class_method()
print(dir(user1))
print(user1.__init__)

'''
#property decorator
'''
class Student:
          def __init__(self):
                    self.__mark=35
          @property
          def method(self):
                    pass
          @method.getter
          def method(self):
                    return self.__mark
          @method .setter
          def method(self):
                    self.__mark=new_value
          @method.deleter
          def method(self):
                    def self.__mark
                    print('value deleted')
stu1=Sudent()
print("Initial value:",stu1.method)
stu1.method=40
print("modified value:",stu1.method)
del stu1.method
'''
#program in encapsulation


#1. rectangle,width,height,area
'''
class Rectangle:
          def __init__(self,width,height):
                    self.__width=width
                    self.__height=height
          @property
          def area(self):
                    return self.__width*self.__height
          @property
          def length(self):
                    return self.__height
          @length.setter
          def length(self,value):
                    self.__hegith= value
          @property
          def breadth (self):
                    return self.__width
          @breadth.setter
          def breadth(self,value):
                    self.__width=value
area1=Rectangle(10,20)
print('length',area1.length,'width',area1.breadth)
print('area of initial value:',area1.area)
area1.length=20
area1.breadth=34
print('length',area1.length,'width',area1.breadth)
print("area of modified value:",area1.area)

'''
#cricle,ArithmeticError radius,radius,diameter,circumference
'''
class Circle:
          def __init__(self,radius):
                    self.__radius=radius
                    self.pi=3.14
          @property
          def radius(self):
                    return self.__radius
          @radius.setter
          def radius(self,value):
                    self.__radius=value
          @diameter
          def diameter(self):
                    return 2*self.__radius
          def circumference(self):
                    return 2*self.pi*self.__radius
radius1=Circle(10)
print("radius of circle",radius1.radius)
print("diameter of the circle",radius1.diameter)
print('circumference of the circle',radius1.circumference)
'''

#--------- +++ polymophisum +++ ---------------
#i.polymophisum wit respect to function
'len'
'''
print(len('polymophisum'))
print(len([3,4.5,'hai']))
print(len({3,4.5,'hai'}))
print(len({2:3,5:4.4}))
'''

#ii.polymophisum with respect to operator
'''
'+'
print(5+6,'5'+'6')
'*'
print(4+5,*[3,1,6],'hai'*3)
'-'
print({24-10,54,5,1}-{3,4,7,1})
'&'
a=10
b=20
print({4,5,1}&{3,4,1},a&b)
'|'
print(a|b)
print({4:5}|{3:4})
'''
#iii.polymophisum with respect to method
'''
class A:
          def display(self):
                    print("hi")
class B:
          def display(self):
                    print("hello")
#one way to access value
a1=A()
a1.display()
a2=B()
a2.dispaly()
#second way
for method in (a1,a2):
          method.display()
  '''
#iv. polymorphism with respect to inheritance
'''
class A:
          def display(self):
                    print("In method A")
class B(A):
          def display(self):
                    print("In method B")
b=B()
b.display()
'''
#another method
'''
class A:
          def display(self):
                    print("In method A")
class B(A):
          def display(self):
                    print("In method B")
                    super().display()
b=B()
b.display()
'''
#abstraction method
'''
from abc import ABC,abstractmethod

class WhatAppFrontEnd(ABC):
     def chat_box(self):
          pass
     def status_box(self):
          pass
     def call_window(self):
          pass
     def setting(elf):
          pass
class WhatAppBackEnd(WhatAppFrontEnd):
     @abstractmethod
     def chat_box(self):
          print("Message is sent")
     def status_box(self):
          print("dipaying the status")
     def call_windows(self):
                print("calling")
     def settings_(self):
                print("open setting")
try:
     user1=WhatAppBackEnd()
     user1.chat_box()
except Exception:
                print("user is not suppoes to access the backend")


'''
#raise keyword
'''
class AgeError(Exception):
          pass
age=int(input("you age"))
if age>=18:
          print("person is egileble")
else:
          raise AgeError("person is not eligible")

'''
'''
class AgeError(Exception):
          pass
age=int(input("you age"))
if age>=18:
          print("person is egileble")
else:
          raise AgeError
except AgeError:
          print("person is not eligibale to vote")

'''

# progarms in the oops concept progarm
#single-level
'''
class A:
          def __init__(self,name,age):
                    self.name=name
                    self.age=age
          def display(self):
                    print(f"name:{self.name},age:{self.age}")
class B:
          def __init__(self.state):
                    self.state=state
          def vote(self,age):
                    if age>=18:
                              print(f"{self.state}:{age} is eligable to vote")
                    else:
                               print(f"{self.state}:{age} is not eligable to vote")
person=A("pratyu",21)
person.display()
vote=B("ap")
vote.vote(person.age)
'''
#multi level
'''
class Number:
          def __init__(self,num_list):
                    self.num_list=num_list
          def diplay(self):
                    print("Number list:",self.num_list)
class Even(Number):
          def pack_even(self):
                    even_nums=[num for num in self.num_list if num%2==0]
                    print("Even Number:",even_nums)
class Odd(Number):
          def pack_odd(self):
                    odd_nums=[num for num in self.num_list if num%2!==0]
                    print("Odd Number:",odd_nums)
num_list=[1,2,3,4,5,6]
even_nums=Even(num_list)
even_nums.dipaly()
even_nums.pack_even()
odd_nums=Odd(num_list)
odd_nums.dipaly()
odd_nums.pack_odd()
                    
'''                 




































