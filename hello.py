print("Hello world") 

f=0xff

    print(f)
    
    print(type(f)) #the  data type

    print(9>8)
a=10.237

    print(type(a))

h=int(a)

    print (h)

    print(hex(10)) #change of data type
    
    ###########################################################################################
    
    #####String

s = "akshaykumar"
    print (s)
s1='''akshaykumar23399'''
    print(s1)
    print(s[2])           #the string location
    
    print(s*4)            #multiply operation on s string
    
    print(len(s1))        #length of the particular string
    
    print(s[5:7])         #print particular lenght characters of a string
    
    print(s[5:])          #print the starting to end strings lenght words
    
    print(s[:7])           #print the part from starting to 7
    
    print(s[-3:])         #print the string in backtrack manner
    
    print(s[0:5:2])       #jumping in the string
    
    print(s[5::-2])       #reverse string by jumping 2 and starting by 5
    
    print(s[::-1])        #reverse the string 
    
    print(s.strip())      #strip the string
    
    print(s.ltrip())      #strip from left
    
    print(s.rstrip())     #strip from right
    
    print(s.find("kum"))   # find the exact location in the string
    
    print(s.find("kum",0,5))  #find the exact location in the string with given intervals
    
    print (s.count("a"))      #count a word appearence in the string
    
    print(s.replace("kum", "rum" ))   #replacing the string from old to new
    
    print(s.upper())    #print uppercase
    
    print(s.lower())    #print lower case

    print(s.title())    #print everyword with uppercase
    
    ############################################################################################################
    
    #list printing
    
    lst=[10,20,'akshay',-10,-20]

    print(lst)               #list printing
    
    print(lst[2])            #list indexing
    
    print(lst[2:4])          #list indexing with starting and ending value
    
    print(lst*2)             #multiply list
    
    print(len(lst))          #lenght of list
    
    lst.append(20)           #adding new object in list
    
    lst.remove(10)           #removing a object from list
    
    del(lst[2])              #deleting the targeted value in list
    
    lst.clear()              #clearing the complete list
    
    print(max(lst))          #printing the max value of list
    
    print(min(lst))          #printing the min value of list
 
    lst.insert(3,88)         #insertin the value #lst.insert(index,object)
    
    lst.sort()               #sorting
    
    lst.sort(reverse=True)   #reverse sorting
    
    ###########################################################################################################
    
          #Tuple
          #Tuple can'nt be modified
          
          
    tpl=(50,60,70,80)            #print tuple #Always use comma while intalizing the single value in tuple
    
    print(tpl[3])                #tuple indexing
     
    print(tpl*3)                 #multiply tuple
     
    print(tpl.count(50))         #count the times the given value printed
    
    print(tpl.index(80))         #indexing of the given value
    
    ##################################################################
    
         #list to tuple
    
    lst=[50,60,70,80,50,50,50]        #list initialization

    print(type(lst))

    tpl1=tuple(lst)

   print(type(tpl1))
#####################################################################

##########################################################################

#set does'nt allow duplicates & does'nt support indexing, slicing, operations like multiply

s={20,30,40,50,6,66,"xyz"}               #print set 
s.update([88,99])                        #update set
s.remove(30)                             #remove set
f=frozenset(s)                           #to frezz the set

#########################################################################################

#Range type

a=range(5)                               #set the range it's excude the max value you passed like it will print from 0to4 not 5!
a=range(1,10)                            #set the starting and ending poin of the range
a=range(1,10,2)                          #set the starting and ending also initialize the diffrence 
for i in a:                              #put i in a
    print(i)                             #keep in mind to mantain social distancing from left
    
    
##############################################################################################

#BYTE & BYtearray

lst=[10,20,30,4,5,6]                    #list
print(type(lst))
b=bytes(lst)                            #list converted to byte
print(type(b))

b1=bytearray(lst)                       #byte converted to byte array
print(type(b1))
b1[2]=44                                #byte array is element is removed with new element
print(b1)                               #final print

##########################################################################################################

#Dictionary

dict={1:"akshay", 2: "Kumar", 3: "23399"}   #dectionary declaration
print(dict)                                 #printing dict


print(dict.items())                         #printing the items of dictionary

a=dict.keys()                               #printing keys of dict
for i in a: print(i)

v=dict.values()                             #printing values of dict
for i in v: print(i)

print(dict[2])                              #printing defined value of dict


########################################################################################################

    #Aithmetic Operations

    a,b=10,5                             

    print('Addition:',a+b)                   #Addition          
    print('subtraction',a-b)
    print('mul',a*b)
    print('div',a/b)
    print('Mod',a%b)
    print('pow',a**b)
    print('floor Div', a//b)


    #Assingment Operator


    = a=10 #means  a=x+y #Assing 10 to a
    += a+=b #means a=a+b 

    #example
     
     a=b=c=20
     print(a,b,c)

     x,y=15,25

     x+=y


     x*=y
     print(x)



#Comparison operator


x,y=15,25

print(x==y)
print(x<y)
print(x>y)
print(x>=y)
print(x<=y)



print(x!=y)


#Logical Operator

x,y=15,25

print(x==15 and y==25)
print((x==35 or y==25))

#Print and input command

print("akshay \n kumar")
print("hello"*3)


a,b=10,20
print(a,b,sep='++++')

#print editing

name="Akshay"
marks=66.33

print("name is",name, "number are,marks")
print("name is %s, Marks are %.2f "%(name,marks))
print('name is {}, Marks are {}'.format(name,marks))

#Input 
s1=input()

print(s1)

s=input("input your name")

print(s)

i=int(input("int number"))

print(i)

print(type(i))   #data type

#spliting the string

lst= {x for x in input("akshaykumar aaja:").split()}
print(lst)

lst= {int(x) for x in input("akshaykumar aaja:").split('')}  #to chanege the input data type

###########################################################################

#small student id program

rd =int(input('student id'))
name = input('name you have')
marks = float (input('numbers you got'))

print('1234',rd,'name',name,'marks',marks)

#average of three numbers
x,y,z = [int (x) for x in input ('enter three numbers: ').split()]
average =  (a+b+c)/3
print('average of your given inputs:', average)

#area of circle

r= float (input('area is: '))
pi=22/7
area=pi*r**2                         #logical part
print(area)

#importing math module

import math                            #math module is imported

r= float (input('area is: '))

area=math.pi*r**2                     #math module is used instead of declaring pi

print(area)










    



    
  










    
    
    
    
    
    
