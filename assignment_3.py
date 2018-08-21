# Q1- Create a list with user defined inputs.
list=[]
s1=input("Enter The Elements of the List ")
list.append(s1)
s2=input("Enter The Elements of the List ")
list.append(s2)
s3=input("Enter The Elements of the List ")
list.append(s3)
s4=input("Enter The Elements of the List ")
list.append(s1)
s5=input("Enter The Elements of the List ")
list.append(s5)
print(list)
print("\n")

# Q2-Add the following list to above created list: 
#[‘google’,’apple’,’facebook’,’microsoft’,’tesla’] 

list2=['google','apple','facebook','microsoft','tesla']

list.append(list2)

print(list)
print("\n")

# Q3-Count the number of time an object occurs in a list. 

print(list.count('google'))
print("\n")


# Q4-Create a list with numbers and sort it in ascending order.

list=[1,8,6,2,6,9,1,2,4,6,7]
list2=[]
list2=sorted(list)
print(list2)
print("\n")

# Q5- Given are two one-dimensional arrays A and B which are sorted in ascending order. Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List] 

A=[1,3,5,6,9,0]
B=[33,4,78,35,77,22]
C=[]
A.sort()
B.sort()
C.extend(A)
C.extend(B)
print(C)
print("\n")


# Q.6- Count even and odd numbers in that list.

list=[1,2,3,4,5,6,7,8,9,10]
even=odd=0
for i in list:
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print(even)
print(odd)
print("\n")

# <--TUPLES-->
# Question 1
#Topic not done in the class

# Question 2
#Topic not done in the class

# <--STRINGS-->

# Q.1- Convert a string to uppercase.

str="this is a sample string"
print(str.upper())
print("\n")

 
# Q.2- Print true if the string contains all numeric characters. 

str=input("Enter String ")
print(str.isnumeric())
print("\n")

# Q.3 Replace the word "World" with your name in the string "Hello World".

str="Hello World"
print("Before Replace :- ",str)
str1=str.replace("World","Pulkit")
print("After Replace :- ",str1)
