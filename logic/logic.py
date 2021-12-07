
#simple if (without else)
# if( condition):
    #code
name = input("Name: ")  #use single equal for assigning value into variable
if (name == "George"):  #use == to compare two entities
    print("Welcome ")


#if-else statment
#if (condition):
    #code
#else:
    #code
x = int(input("x = "))
if (x > 2):
    print("x > 2")
else:
    print(" x is not greater than 2")

#cascading if-statement
# if(condition1):
#   code
#elif (condition 2):
#   code
#elif (condition 3):
#   code
#.......
#.......
#else:
#   code
x = int(input("x = "))
if (x > 5):
    print("x > 5")
elif(x < 5):
    print("x < 5")
else:
    print("x == 5")
    
#Nested if-statement (is a statement that includes one or more if statements)
#if(condition1):
#   if(condition2):
#       code
#   else:
#       code
#else:
#   code

x = int(input("x = "))
if( x > 0):
    if(x%2 == 0):
        print("x is even")  
    else:
        print("x is odd")
else:
    print("x is negative")
