#Dictionary is a collection of data in a form of key-value
#Dictionary is unordered
#Dictionary is indexed
#Dictionary is changeable
#Dictionary does not allow  duplicates

mydictinary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(mydictinary)

def printDictionary():
    print("\n--------------------------------------\n")
    for key in mydictinary.keys():
        print("%s:::%s"%(key,mydictinary[key]))
        

printDictionary()

del mydictinary["Akua"]
printDictionary()
    
del mydictinary["Paulo"]
printDictionary()
