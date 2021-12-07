


#function returns nothing  
def showStatus():
    print("Server is running...")
    

#function returns 1 value
def multiply(a,b):
    return a*b
    
     

print(multiply(2,3))

try:
    showStatus()
except NameError:
    print("Cannot find function name")
