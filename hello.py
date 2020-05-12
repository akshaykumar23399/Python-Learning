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
    
    #list printing
    
    lst=[10,20,'akshay',-10,-20]

    print(lst) #list printing
    
    print(lst[2]) #list indexing
    
    print(lst[2:4]) #list indexing with starting and ending value
    
    print(lst*2)    #multiply list
    
    print(len(lst))  #lenght of list
    
    lst.append(20)  #adding new object in list
    
    lst.remove(10)  #removing a object from list
    
    del(lst[2])      #deleting the targeted value in list
    
    lst.clear()      #clearing the complete list
    
    print(max(lst))  #printing the max value of list
    
    print(min(lst))   #printing the min value of list
 
    lst.insert(3,88)  #insertin the value #lst.insert(index,object)
    
    lst.sort()        #sorting
    
    lst.sort(reverse=True)   #reverse sorting
    
          #Tuple
          #Tuple can'nt be modified
          
          
    tpl=(50,60,70,80)  #print tuple #Always use comma while intalizing the single value in tuple
    
    print(tpl[3])   #tuple indexing
    
    
    print(tpl*3)    #multiply tuple
    
    
    
    print(tpl.count(50))         #count the times the given value printed
    
    print(tpl.index(80))         #indexing of the given value
    
         #list to tuple
    
    lst=[50,60,70,80,50,50,50]    

    print(type(lst))

    tpl1=tuple(lst)

   print(type(tpl1))






    
    
    
    
    
    
