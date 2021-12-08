
#There are two types of functions

#1 - Function that returns a value or values
# def <function-name> (<arguments>):
#   <code-block>
#   return <value(s)>
def add(a,b):
    a += 3 # ----> 8
    b += 4 # ----> 7
    return a+b, a-b

plus, minus = add(5,3)
print("{} + {} = {}".format(5,3,plus))
print("{} - {} = {}".format(5,3,minus))

#2 - Function that completes a task and returns nothing
# def <function-name> (<arguments>):
#   <code-block>
def showrange():     
    print(list(range(1,10)))
showrange()

def showeven():
    mylist = list(range(1,10))
    for e in mylist:
        if (e%2 == 0):
            print(e)
showeven()
