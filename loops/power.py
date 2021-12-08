#For every number read from STDIN, show all powered by 2 numbers from 0 until this number

n = int(input("N = "))

i = 0
while ( i <= n):
    print("{} power 2 ---> {}".format(i,pow(i,2)))  #i ---> i**2
    i +=1
print()   
for num in range(0,n+1):
    print("{} power 2 ---> {}".format(num,pow(num,2)))
