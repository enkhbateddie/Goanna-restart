#Set is a collection of data of any type
#Set is unordered
#Set is unindexed
#Set is changeable
#Set is unqiue, does not allow duplicate elements

#Create a set
set1 = {"Welcome","to","Python"}
print(set1)

#Add element to a set
set1.add(2021)
print(set1)
set1.update(["Dec",6])
print(set1)
set1.add(2021)
print(set1)

#remove element from set
set1.remove(6)
print(set1)
set1.discard("Dec")
print(set1)
set1.pop()
print(set1)

#Joinning sets
set2 = {"Dec",6}
myset = set1.union(set2)
print(myset)

del myset
try:
    print(myset)
except NameError:
    print("Set does not exist")