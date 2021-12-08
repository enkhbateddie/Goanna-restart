
#While loop runs a code-block between starting point and ending point, or until a condition becomes false
# while(condition):
#   code-block
#the loop stops when condition is false
months = [31,28,31,30,31,30,31,31,30,31,30,31]
i = 0
while ( i < 8 ):
    print("Python is fun")
    total = 0
    for month in months:
        total = total + month
        print("Average days = {:.3f}".format(total/len(months)))
    i += 1 # i = i + 1
    

#for loop reads all elements in a range or a collection
# for <variable> in <sequence>:
#   code-block

months = [31,28,31,30,31,30,31,31,30,31,30,31]

#total = 0
#for month in months:
#    total = total + month
#print("Average days = {:.3f}".format(total/len(months)))

print("Average days = {:.3f}".format(sum(months)/len(months)))
