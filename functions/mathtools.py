#Define a function that reads a number N from STDIN
#Define a function that determines the max N until -1 is entered
#Define a function that calculates the sum-series of N
#Define a function that calculates the factorial of N
#Define a main function that runs your program

#Read pattern
def readN():
    return int(input("N = "))

def maxN():
    n = readN()
    maximum = 0
    while n != -1:
        if(maximum < n):
            maximum = n
        n = readN()
    return maximum

def sumSeries(n): #1+n+3+...+(n-1)+n
    total = 0
    for e in range(1,n+1):
        total += e
    return total

def factorial(n): #1*2*3*...*(n-1)*n
    f = 1
    for e in range(1,n+1):
        f *= e
    return f

def main():
    print("Max = {} ".format(maxN()))
    n = readN()
    print("Sum Series({}) = {}".format(n,sumSeries(n)))
    print("Factorial({}) = {}".format(n,factorial(n)))
    
main()