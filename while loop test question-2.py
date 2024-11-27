'''1.
sentence="hello world welcome to python programming hi there"
d_={}
for word in sentence.split():
          if word[0] not in d_:
                    d_[word[0]]=[word]

          else:
                    d_[word[0]]+=[word]

print(d_)
'''
'''5.
names=['apple','google','apple','yahoo','yahoo','google','gmail','gmail','gmail']
d_={}
for word,names in enumerate(names):
          if names not in d_:
                    d_[names]=[word]
          else:
                    d_[names]+=[word]
print(d_)
'''
#2.
'''
d={'a':'hello','b':100,'c':10.1,'d':'world'}
for key,value in d.items():
          if isinstance(value,str):
                    d[key]=value[::-1]
          else:
                    d[key]=value
print(d)
'''
#3.
'''
files=['apple.txt','yahoo.pdf','gmail.pdf','google.txt','amazon.txt','facbook.txt','flipkart.pdf']
ext1='txt'
ext2='pdf'

file_ext={}
for file in files:
          f_e=file.split('.')
          if f_e[-1]==ext1:
                    if ext1 not in file_ext:
                              file_ext[ext1]=[f_e[0]]
                    else:
                              file_ext[ext1]+=[f_e[0]]
          elif f_e[-1]==ext2:
                    if ext2 not in file_ext:
                              file_ext[ext2]=[f_e[0]]
                    else:
                              file_ext[ext2]+=[f_e[0]]
print(file_ext)
'''
#4.grouping flower and animals in the below list
'''
items=['lotus-flower','lilly-flower','cat-animal','sun-flower','dog-animals']
'''
'''
l=[4,5,2.6]
l_=[]
for i in enumerate(l_):
          l_.append(i[1]**[0])
          print(l_)
'''


