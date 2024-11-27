8#"looping"
#while loop
#porgram to print number from 1to5
'''i=1
while i<=5:
        print(i)
        i=i+1
         '''
#program to print number from 5 to 1
'''i=5
while i>=1:
          print(i)
          i-=1'''
#write a pgram to print "bangalore"10 times
'''
j=1
while j<=10:
          print('bangalore',j)
          j+=1
   
'''
#program to print you name n time
'''
3j=1
n=int(input("Enter the times:"))
while(j<=n):
          print("priya")
          j+=1
'''
'''
name_=input("what is your name?")
n=int(input("gives me the count?"))
i=1
while i<=n:
          print(name_,i)
          i+=1
'''
#program to start the number from start to end
'''
a=int(input("strat value"))
b=int(input("ending value"))
while (a<=b):
          print(a*a)
          a+=1
         
'''
#packing list (with method---append)
'''
a=int(input("strat value"))
b=int(input("ending value"))
l_=[]
while (a<=b):
          l_.append(a*a)
          a+=1
          print(l_)
   
'''
#packing list (without method --apend)
'''
a=int(input("strat value"))
b=int(input("ending value"))
l_=[]
while (a<=b):
          l_=l_+(a*a)
          a+=1
          print(l_)
   
'''
#program to get the characher and its INDEXES
'''
str_=input("enter the string_:")
index_=0
while index_<len(str_):
          print(index_,str_[index_])
          index_+=1
'''
#program to print nested list with charater and its ASCII value
'''
str_=input("enter a string")
i=0
l_=[]
while i < len(str_):
          l_+=[[str_[i],ord(str_[i])]]
          i+=1
          print(l_)
          
'''
#program to get elemeny and its lenght by taking the input from user
'''
a_=input("enter the string:")
b_=a_.split()
start_=0
while start_<len(b_):
          print(b_[start_],len(b_[start_])
                start+=1
'''

#QTALK PROGRAM FOR STDUTY
#1.pogram to convert lowercase to uppercase
'''
a=str(input("enter the string:"))
print(a.upper())
'''
#2.porgarm to convert uppercase to lowercase
'''
b=str(input("enter the string:"))
print(b.lower())
'''

#3.convet uppercasse to lowercase to lower to upercase with using method
'''
inp_=input("enter :")
if inp_.islower():
          print(inp_.upper())
else:
          print(inp_.lower())
          
'''

#4.convet uppercasse to lowercase to lower to upercase without using method
#one character
'''
inp_=input("enter:")
if'a'<=inp_<='z':
          print (chr(ord(inp_)-32))
elif'A'<=inp_<='Z':
          print(chr(ord(inp_)+32))
else:
          print(invalid)

'''

#5.program to print indexs and its charater of the string
'''
a=str(input("enter the string:"))
index_=0
while index_<len(a):
          print(index_,a[index_])
          index_+=1
'''
# 6.program to convert upper to lower and lower to upper without using
# method using inbulit method for more one char(multiple char)

'''
str_=input("enter :")
index_=0
while index_<len(str_):
          if 'a'<=str_[index_]<='z':
                    print(chr(ord(str_[index_])-32))
          elif'A'<=str_[index_]<='Z':
                    print(chr(ord(str_[index_])+32))
index_+=1
'''
#without method
'''
str_=input("enter :")
index_=0
new_str=''
while index_<len(str_):
 if 'a'<=str_[index_]<='z':
          new_str+=(chr(ord(str_[index_])-32)
 elif'A'<=str_[index_]<='Z':
          new_str+=(chr(ord(str_[index_])+32)
 else:
          new_str+=string_[index_]
          index_+=1
'''
#7.program to get the string in reverse order
#1.
'''
inp_=input("enter the string:")
print(inp_[::-1])
'''
#2.
'''
inp_=input("enter the string:")
i=0
n_s=''
while i<len(inp_):
    n_s=inp_[i]+n_s
    i+=1
    print(n_s)
'''
#8.progarm to get the lenght of string in a list
'''
name=['eve','james','bill','steve','mill','amul']
i=0
l_=[]
while i<len(names):
          l_.append(len(name[i])
          i+=1
print(l_)
'''
#9.progarm to get the 1st character of string in a list
'''
names=['eve','james','bill','steve','mill','amul']
first_chars=[]
i=0
while i<len(names):
          first_chars.append(names[i][0])
          i+=1
print(first_chars)
'''
#10.program to get the end char of each string in list
'''

names=['eve','james','bill','steve','mill','amul']
last_chars=[]
i=0
while i<len(names):
          last_chars.append(names[i][-1])
          i+=1
print(last_chars)
'''

#11.program create a dictionary with starting character one word in the list
'''
names=['eve','james','bill','steve','mill','amul']
dic_={}
i=0
while i<len(names):
    dic_[names[i][0]]= names[i]
    i+=1
print(dic_)
'''
#12.create a dictionary with word and length word in the list
'''
names=['eve','james','bill','steve','mill','amul']
dic_={}
i=0
while i<len(names):
          dic_[names[i]]=len(names[i])
          i+=1
print(dic_)


'''
#13.Progarm to print only the words starting with vowel

names=['eve','james','bill','steve','mill','amul']
vowels_=('a','e','i','o','u')
i=0
while i<len(names):
          if (names[i][0] in vowels_):
                    print(names[i])
          i+=1   

          
#14.program to get the number start with of even number
'''
number=[2,3,4,45,29,12,90,77,65]
i=0
while i<len(number):
          if int(str(number[i])[0])%2==0:
                    print(number [i])
                    i+=1
'''
#15.program to get the number start with of odd number
'''
n=[2,3,4,45,29,12,90,77,65]

numbers_starting_with_odd=[]
i=0
while i<len(n):
          if int(str(number[i])[0])in{1,3,5,7,9}:
                    numbers_starting_with_odd.append(i[i])
          i+=1
print(number_starting_with_odd)
'''
#16.progarm to get  the factorial of a number
'''
num_=int(input("enter a number:"))
i=1
fact_=1
while num_>=i:
          fact_=fact_*i
          i+=1
print("factorial of",num_,'is',fact_)
'''
#Progarm to get 1 to 10

i=1
while i<=10:
          print(i)
          i=i+1

#Progarm to get -1 to -10
'''
i=-1
while i>=-10:
          print(i)
       i=i-1
'''
#Progarm to get 10 to 1
'''
i=10
while i>=1:
          print(i)
          i-=1
'''
#Progarm to get 1 to user input
'''
user_input=int(input("enter the number"))
i=1
while i<=user_input:
          print(i)
          i=i+1
'''
#Progarm to get -20 to -10
'''
i=-20
while i<=-10:
          print(i)
          i=i+1
   '''       
#Progarm to get 1 to -10
'''
i=1
while i>=-10:
          print(i)
          i+=1
print()
   '''
'''
#Progarm to get -1 to 20
i=-1
while i>=20:
          print(i)
          i+=1
print()

#Progarm to get 10 to -1

i=10
while i>=-1:
          print(i)
          i-=1
print()

'''
#1.Built a dictionary of word and length pair
#word="This is a bunch of word"
'''
s_ = "This is a bunch  words"
words_=s_.split()
w_=dict()
i=0
while i<len(words_):
          w_[words_[i]]=len(words_[i])
          i+=1
print(w_)
'''
#2.fliping keys and value of dictionay
'''
dic={'a':1,'b':4,'c':8}
items_=dic.items()
items_list=list(items_)
print(items_list)
d_={}
i=0
while i<len(items_list):
          d_[items_list[i][1]]=items_list[i][0]
          i+=1
print(d_)
'''
#3.progarm to count the number of each in string

name="guido van rossum"
d_=dict()
j=0
while j<len(name):
          d_[name[j]]=name.count(name[j])
          j+=1
print(d_)

#4. progarm to create a dictionary with word and its count
'''
sentence = "hello world welcomes to python - hai world welcome to Java"
import string
translator = str.maketrans('', '', string.punctuation)
clean_sentence = sentence.translate(translator).lower()
words = clean_sentence.split()
word_count = {}
index = 0
while index < len(words):
    word = words[index]
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
    index += 1
print(word_count)
'''
#5. dictionary of charracter and ascii value of pair
'''
n= "absAbS"
a = {}
i = 0
while i < len(n):
    a[n[i]] = ord(n[i])
    i += 1
print(a)
'''
#6.buliting a dictionary whoes price value is more thean 200
'''
prices={'AEMC':24.45,
       'APAL':612.45,
       'JBM':200.45,
       'HP':37.80,
       'FB':10.75}
price_tuple=tuple(prices.items())
i=0
d_price={}
while i<len(price_tuplr):
    if price_tuple[i][1]>200:
          d_price[price_tuple[i][0]]=price_tuple[i][1]
          i+=1
print(d_price)
'''
#7.progarm to get all the alphabet from the string
'''
s= "absAbS123!@#"
a = ""
i = 0
while i < len(s):
    if( s[i].isalpha())
        a += s[i]
    i += 1
print(a)
''''
#8.progarm to get all the special character in string
'''
s = "absAbS123!@#"
a = ""
i = 0
while i < len(s):
    if not s[i] .isalnum():
    a+=s[i]
    i+= 1
print(a)
'''
#9.progarm to get only the integer from the list
'''
data=['hai','hello',10,'12.3',12,19,16.3}
i=0
while i<len(data):
    if (type (data[i])== int:
        print(data[1])
    i+=1

print(l_)
''' 

#10.program to get only the vowels in a string
'''
s="python selenium"
i=0
s_=''
while i<len(s):
        if(s[i] in ('a','e','i','o','u')
           s_+=s[i]
           i+=1
print("vowels in string:",s_)
'''
#11.progarm to get only alphanumaric character from a string
'''
s_=input("enter a string")
i=0
s_=''
while i<len(st_):
           if(st_[i].isalnum()):
       `        s_+=st_[i]
           i+=1
print(s_)
'''        
#12.write a program to check if the given list of string which is palindrom
'''
p_=['123','121','dad','mom','hello','hai']
i=0
while i<len(p_):
           if p_[i]==p_[i][::-1]:
           print(p_[i],"It is palindrom")
           else:
           print(p_[i],"It is not palindrom")
           i+=1
'''
#13.replace all the vowel with* in the string hello world
'''
string="hello world"
s=''
while i len(string):
           if(string[i] in ('a','e','i','o','u'):
              s_+=string.replace(string[i],'*')
              i+=2
              print("vowel in string:",s_)
 '''
#14.write a program to find the highest common factor of tow number while loop
'''
num1=int(input("Enter the frist number:"))
num2=int(input("enter the second number:"))
hcf=0
i=1
while i<=min(num1,num2):
        if num1%i==0 and num2%i==0:
                hcf=i
        i+=1
'''

