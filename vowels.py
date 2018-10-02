#Jordan Brooks
#Practice project to learn python
#Tells you how many vowels are in the sentance you typed

vowel = 0

x = input('Enter sentence: ')


for a in x:

    if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':

        vowel += 1      

print("You said:  " + x)

print("There are " + str(vowel) + " vowels in your sentence") 

input("Press enter to exit")

#Type 'The quick brown fox jumped over the lazy dog'
#should output 12
#CAN BE USED FOR ANY SENTENCE