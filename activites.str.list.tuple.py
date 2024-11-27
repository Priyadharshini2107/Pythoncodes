#string activity 
#1.
'''
str1='welcome'
print(','.join(str1))
'''
#2.
#index
'''
str2=input("Enter")
sub_string=input("enter the sub_string")
print(str2.index(sub_string))
'''
#find
'''
str3=input("enter :")
sub_string=input("enter the sub_string")
print(str3.find(sub_string))
'''
#3.
'''
s_2=''
print(bool(s_2))
'''
#4.
'''
s ="Hello welcome to python"
sub_s="hello"
print(s.startswith(sub_s,0,len(s)))
'''
#5.
'''
s_2=input("enter the string")
print(s_2.isalnum())
'''
#6.
'''
a="10"
b="20"
print(a+b)
'''
#7.
'''
str1="welcome to tamilnadu"
print(str1[::-1])
'''
#8.
'''
str4='Hai'
str4[0]='h'
print(str4)
'''
#list activity
#1.i)

'''
name=['Apple','Google','facebook','instagram','micorsoft']
name.append(['netflix','prime','hotsart'])
print(name)
'''
#ii.
'''
name=['Apple','Google','facebook','instagram','micorsoft']
name.extend("prime")
name.extend(['netflix','prime','hotsart'])
print(name)
'''
#2.
'''
l2 = [56,78,90,56,31,90,]
l2.pop()
l2.pop(3)
l2.remove(90)
print(l2)
'''

#3.
'''
list1=[3,6,89,23,10,5,7]
print(list1)
list1.sort(reverse=False)
print(list1)
list1.sort(reverse=True)
print(list1)
'''
#4.i.) ii.)
'''
print(list("Developer in pysipder"))
print(list("Developer in pysipder".split()))
'''
'''
#tuple(activity)
#1.

t1=((45,))
print(t1)

#2.

t1=(1,2,3)
id1=id(t1)
print(id1)
t2=(4,5,6)
id2=id(t2)
print(id2)
'''
#3.
'''
t1=(1,2,3)
t2=(4,5,6)
print(*t1,*t2)
'''
#4.
#1.
'''
t=(1,2,3,4,['hai','hello',123],"python")
t2=list(t)
t2[5]="pYthon"
x=tuple(t2)
print(x)

#2.

t=(1,2,3,4,['hai','hello',123],"python")
t2=list(t)
t2[1]=9
t2[2]=10
t2[3]=11
x=tuple(t2)
print(x)
'''
#5.
'''
t2=(45,67,89,12,34)
t=list(t2)
t.append(100)
x=tuple(t)
print(x)
'''
#6.
'''
t=(1,2,3,4,['hai','hello',123],"python")
x=list(t)
x.remove(4)
x.remove("python")
print(tuple (x))

'''
