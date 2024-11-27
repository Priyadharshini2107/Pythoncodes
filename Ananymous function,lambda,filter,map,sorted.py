 #-----++ ANONYMOUS FUNCTION ++--------

  #---++Lambda++----
'''
'1.program to square a number'

square_ = lambda num: num*num
print(square_(4))#16


#'program to find the sqaure and cube

square_cube = lambda num: (num*num,num**3)
print(square_cube(4))#16

#3.program to check a character is vowel or not

vowe_not  = lambda v: v in 'aeiouAEIOU'
print(vowe_not('a'))#True
print(vowe_not('0'))
print(vowe_not('l'))
print(vowe_not('e'))

#4. program to check a number is even or not

even_not = lambda num : num %2 ==0
print(even_not(5))

even_not = lambda e: e in (0,2,4,6,8)
print(even_not(5))

#5. write a python program to create a lambda function that add 15 to a given number


add_ = lambda num: num+15
print(add_(5))

#6. create a lambda function that multiplies 2 arguments

mul_ = lambda num,num2: num*num2
print(mul_(5,6))


#7.program to add two numbers

add_ = lambda num,num1: num+num1
print(add_(3,5))
#8. program to solve the expression a**2+b**2+2*a*b
expression_ = lambda a,b:(a**2+b**2+2*a*b)
print(expression_(2,3))

#9.program to solve the expression 2*a+3*b+4*c

expression_ = lambda a,b,c:(2*a+3*b+4*c)
print(expression_(2,3,4))

#10. program to return last data of any sequence
last_data = lambda data:data[-1]
print("last data:",last_data('python'))


#11. program to check if a string is palindrom or not

str = lambda a:(a == a[::-1])
print(str('123'))
print(str('424'))

#12. write a python program to convert negative number to positive

n = lambda a:abs(a)
print(n(-12))

#13. check if a data is present in a list (take list of strings)

data  = lambda iterable,data : iterable == data[0]
print(data(['python','java'],'python'))
'''
   #-----++ FILTER ++-------
'''
#filter.....filter(function name, iterable)
#even or not
'''
def is_even(numbers):
    if int(numbers) % 2==0:
        return int(numbers)
z = filter(is_even,[34,33,56,12,45])
print(list(z))
'''
#By using filter check even or not

is_even = lambda numbers : int(numbers) % 2==0
print(tuple(filter(is_even,(34,33,56,12,45))))

#2.program to get all the vowels in a string

vowel = lambda v:v in 'aeiouAEIOU'
print(tuple(filter(vowel,('python programming'))))

#3.defined a function to check if a strings length is more then 5

strings = ['apple', 'banana','kiwi','fig','pear']
def func(strings):
    return len(strings) > 5
print(list(filter(strings,{})))



strings = lambda str : len(str) > 5
print(tuple(filter(strings,['apple', 'banana','kiwi','fig','pear'])))

#4. define a function to check if a person's age is 18 or more

people = [
    {'name':'Alice','age':25},
    {'name':'bob','age':17},
    {'name':'Charlie','age':30},
    {'name':'David','age':15}
    ]
def is_adult(people):
    return people['age'] >= 18
print(list(filter(is_adult,{})))


is_adult  = lambda person: person['age'] >= 18
print(list(filter(is_adult,people)))

          #-----------++ QTALK ++-----------

#---++Programs on filter -----

#Program to print only even numbers in the range 1-50

even_num = lambda a: a%2 == 0
print(tuple(filter(even_num,range(1,51))))


#Program to print only odd numbers in the range 1-50

odd_num = lambda a: a%2!= 0
print(tuple(filter(odd_num,range(1,51))))


#"Build a list with only even length string using filter func
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
even = lambda names: len(names) % 2 == 0
print(list(filter(even,names)))

#Returns the string if the string is starting from vowel character"


names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']
string = lambda str: str[0].lower() in 'aeiou'
print(list(filter(string,names)))


#"Program to return only positive values in the list

numbers = [-2, -1, 0, 1, 2]
positive_num = lambda num:num>=0
print(list(filter(positive_num,numbers)))

#Program to print prime numbers from 1-50

prime_num = lambda a : a > 1 and all(a % i for i in range(2,a)) 
print(tuple(filter(prime_num,range(2,50))))


#Program to extract only negative numbers from the list

numbers = [-2, -1, 0, 1, 2]
negative_num = lambda num: num<0
print(list(filter(negative_num,numbers)))
'''

          #----------++ Qtalk ++------------

#------++ map ++---------

#Write a Python program to square and cube every number in a given list of integers.

def square_and_cube(nums):
    return list(map(lambda x: (x**2, x**3), nums))

nums = [1, 2, 3, 4, 5]
result = square_and_cube(nums)
print(result)

#Write a Python program to find if a given string starts with a given character.

def starts_with(string, char):
    return list(map(lambda x: x.startswith(char), string))

string = ["apple", "banana", "apricot", "grape"]
char = "a"
result = starts_with(string, char)
print(result)


#Write a Python program to convert negative numbers in a given list to positive numbers.
'''
def convert_to_positive(nums):
    return list(map(lambda x: abs(x), nums))

nums = [-1, -2, 3, -4, 5]
result = convert_to_positive(nums)
print(result)
'''

#Write a python program to return a list of elements raised to the power of their indices
'''
def power_of_index(nums):
    return list(map(lambda x: x[1]**x[0], enumerate(nums)))

nums = [2, 3, 4, 5]
result = power_of_index(nums)
print(result)
'''
#Write a Python program to calculate the sum of the positive and negative numbers of a given list.

def sum_of_positives_and_negatives(nums):
    positive_sum = sum(map(lambda x: x if x > 0 else 0, nums))
    negative_sum = sum(map(lambda x: x if x < 0 else 0, nums))
    return positive_sum, negative_sum

nums = [-1, 2, -3, 4, 5, -6]
positive_sum, negative_sum = sum_of_positives_and_negatives(nums)
print("Sum of positives:", positive_sum)
print("Sum of negatives:", negative_sum)

#--------++ sorted ++------------

#program to sort below list

number1=[3,1,4,5,6,7,7,8,3,4,6]
print(sorted (number1))
print(sorted(number1,reverse=True))

#program to sort according the length of string
'''
random_word=['bank','stack-over-flow','sprcific','very-cool']
print(sorted(random_word))
'''
#sort according to 1st character
'''
random_word=['bank','stack-over-flow','sprcific','very-cool']
print(sorted(random_word))
'''
#sort according to 1ast character
'''
random_word=['bank','stack-over-flow','sprcific','very-cool']
print(sorted(random_word,key=lambda word:word[-1]))
'''
#sort absoute value
'''
complex_number=[3+4j,1-1j,-1+2j,4+5j]
print(sorted(complex_number,key=abs))
'''
# ---- program for sorted -----
#1.sorting dictionay by keys
'''
my_dict = {"banana": 3, "apple": 3, "cherry": 3, "date": 4}
sorted_by_keys = dict(sorted(my_dict.items(), key=lambda item: item[0]))
print(sorted_by_keys)
'''
#2.sorting dictionay by values
'''
my_dict = {"banana": 3, "apple": 3, "cherry": 3, "date": 4}
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_by_values)
'''

#3.sorting a list of dictionary by a specify key
'''
students = [
    {'name': 'bob', 'age': 17, 'grade': 'A'},
    {'name': 'Charlie', 'age': 30, 'grade': 'C'},
    {'name': 'David', 'age': 15, 'grade': 'C'}
]

sorted_students_by_age = sorted(students, key=lambda x: x['age'])
print(sorted_students_by_age)
'''
#sorting with multiple keys
'''
students = [
    {'name': 'bob', 'age': 17, 'grade': 'A'},
    {'name': 'Charlie', 'age': 30, 'grade': 'C'},
    {'name': 'David', 'age': 15, 'grade': 'C'}
]

sorted_students = sorted(students, key=lambda x: (x['grade'], x['age']))
print(sorted_students)
'''
#sorting with list in lists
#data=[[1,2],[5,4],[2,3]]
'''
data = [[1, 2], [5, 4], [2, 3]]
sorted_data = sorted(data)
print(sorted_data)
'''
#sorting a set of tuples by length string
#name={(bob,copper),(chailer,rakesh),(james,bound)}
'''
names = {('bob', 'copper'), ('chailer', 'rakesh'), ('james', 'bound')}
sorted_names = sorted(names, key=lambda x: len(x[0]))
print(sorted_names)
'''
