#Tuple is a collection of data of any type
#Tuple is ordered
#tuple is indexed
#Tuple is unchangeable
#Tuple allows duplicates

#Create a tuple
tuple1 = ("Tom",33,100.8)

length = len(tuple1)
print("Length = "+str(length))

#Access elements in a tuple
print("first: "+tuple1[0])
print("last: "+str(tuple1[length -1]))

#Join 2 tuples
tuple2 = ("bank","AU")

mytuple = tuple1+tuple2
print(mytuple)

del mytuple
try:
    print(mytuple)
except NameError:
    print("Tuple has been deleted")