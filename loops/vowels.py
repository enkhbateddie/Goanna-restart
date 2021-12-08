#Count the number of vowels in a string from STDIN
#Also print the frequency of each vowel

sentence = input("Sentence: ")

total = 0

for vowel in "aioeu":
    frequency = sentence.lower().count(vowel)
    total += frequency
    print("{} ---> {}".format(vowel,frequency))

print("{} has {} vowels".format(sentence,total))
