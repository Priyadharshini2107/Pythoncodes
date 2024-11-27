# ---------------------------comprehesion-----------------------
#-------+list+--------
#1.progarm to square number in a range
'''
list_=[]
for i in range (1,11):
          list_.append(i*1)
print(list_)
'''
'''
print([i**2 for i in range(1,11)])
'''
#program to square the number in a range only even
'''
print(i**i for i in range(20,30)if i%2==0)
'''
#program to print'even if the number otherwise 'odd'
'''
l_number=[23,45,11,23,34,67,56,89,90]
print(['even' if n%2==0 else 'odd' for n in l_number])
'''
#program to convert string to upppercase
'''
words = ('hello', 'world', 'python')
print([word.upper() for word in words])
'''
#program to fetch all the middle element in the list
'''
list_=[[1,2,3],['hi','bye','laugh'],[2.5,3.5,8.9,9.9,2.8]]

print([sublist[len(sublist)//2] for sublist in list_ if len(sublist) % 2 != 0])
'''
#extract digit from string
'''
text='a1b2c3'
print([char for char in text if char.isdigit()])
'''
#create a list of tuple with number and its cubes
'''
numbers = [1, 2, 3, 4, 5]
print([(num, num**3) for num in numbers])
'''
#flitering only the number divisiablse by 2 and 5
'''
numbers = [10, 20, 30, 40, 50, 60,56]
print([num for num in numbers if num % 2 == 0 and num % 5 == 0])
'''
#extract 1st lethher of ecah word if it is consenent
'''
words = ['hello', 'world', 'python']
print([word[0] for word in words if word[0].lower() not in 'aeiou']
'''
#program to fetch the fruits and its index if the index is odd
'''
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print([(fruit, index) for index, fruit in enumerate(fruits) if index % 2 != 0]
'''
#program to fetch only repeated character in a string
'''
text = 'hello world'
print([char for char in set(text) if text.count(char) > 1])
'''   
#create a list of dictionary
'''
keys = ['name', 'age', 'city']
values = ['priya', 20, 'salem']
print({key: value for key, value in zip(keys, values)})
'''
#customzing number
'''
numbers = [-5, 0, 5, 10, -10]
print(['positive' if num > 0 else 'negative' for num in numbers])
'''
#create a comphersion to print postive if the value is postive otherwies print neagtive if the value is negative
'''
numbers = [-5, 0, 5, 10, -10]
print(["positive" if num > 0 else "negative" for num in numbers])
'''
#reverse a string if the length of string is more than 5 otherwise print as it is
'''
strings = ['hello', 'world', 'python', 'abc']
print([string[::-1] if len(string) > 5 else string for string in strings])

'''
#-----------++ set ++----------------
'''

#1. Convert string to uppercase:

words = ('hello', 'world', 'python')
print({word: word.upper() for word in words})

#2. Fetch all middle elements in a list:

list_ = [[1, 2, 3], ['hi', 'bye', 'laugh'], [2.5, 3.5, 8.9, 9.9, 2.8]]
print({index: sublist[len(sublist)//2] for index, sublist in enumerate(list_) if len(sublist) % 2 != 0})


#3 Extract digits from a string:

text = 'a1b2c3'
print( {char for char in text if char.isdigit()})


#4. Create a list of tuples with number and its cube:

numbers = [1, 2, 3, 4, 5]
print({(num, num**3) for num in numbers})


#5. Filter numbers divisible by 2 and 5:

numbers = [10, 20, 30, 40, 50, 60]
print( {num for num in numbers if num % 2 == 0 and num % 5 == 0})


#6. Extract 1st letter of each word if it is consonant:

words = ['hello', 'world', 'python']
print({word[0] for word in words if word[0].lower() not in 'aeiou'})



#7. Fetch fruits and their index if the index is odd:

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print({(fruit, index) for index, fruit in enumerate(fruits) if index % 2 != 0})


#8. Fetch only repeated characters in a string:

text = 'hello world'
print({char for char in set(text) if text.count(char) > 1})

#9. Create a list of dictionaries:

keys = ['name', 'age', 'city']
values = ['priya', 20, 'salem']
print({key: value for key, value in zip(keys, values)})


#10. Customize numbers:

numbers = [-5, 0, 5, 10, -10]
print( {'positive' if num > 0 else 'negative' for num in numbers})



#11. Reverse a string if length is more than 5:

strings = ['hello', 'world', 'python', 'abc']
print({string[::-1] if len(string) > 5 else string for string in strings})

#12.create a dictionay with word and it lenght if the word length is less than 5
#otherwise reveser the word
words = ['hello', 'world', 'python', 'code', 'reverse']

print({(word, len(word)) if len(word) < 5 else (word[::-1], len(word)) for word in words})

'''


#-------++dictionay comperhesion ++-------
#create a dictionay with word and its length
'''
user=input("enter the word:").split()
d_={}
for word in user:
          d_[word]=len(word)
print(d_)
print({word:len(word)for word in user})
'''

#create a dictoionary with character and its and ascii value if the char is vowel
'''
input_string=input('enter the string:')
print({char:ord(char) for char in input_string if char in 'aeiouAEIOU'})

'''
#create a dictionay with word and it lenght if the word length is less than 5
#otherwise reveser the word
'''
a=input("enter the word")
d_={}
for word in d_:
          if word<5:
                   a=(len(word),d)
          else:
                    a(word[::-1])
print(a)
'''
'''
words = ['hello', 'world', 'python', 'code', 'reverse']
print({word: len(word) if len(word) < 5 else word[::-1] for word in words})
'''

