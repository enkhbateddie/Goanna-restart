import re 

f = open("demo.txt","r")

regex = input("Pattern: ")
replace = input("Replacement: ")

for line in f:
    found = re.findall(regex,line)
    if(found):
        replaced = re.sub(regex,replace,line)
        print(replaced)
f.close()
