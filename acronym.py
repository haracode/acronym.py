def any(iterable): #the any function is not bulit in this verison of python (2.4.4). 
    for element in iterable: #I went to the python library (http://docs.python.org/2.7/library/functions.html#any) and found the code to manually import the any function
        if element:
            return True
    return False # any function is needed for later use


def checkNum(x): #function to check if any single character is a digit
    return any(character.isdigit() for character in x)


phrase = raw_input("Make an acronym with 2 or more words!\n")
if checkNum(phrase) == False and " " in phrase: # check if there is a number in the phrase and if there is a space, meaning there is at least 2 words
    brkPhrase = phrase.split() #Break the phrase into individual words
    letter = " " #letter varibale later used in loop
    for i in brkPhrase:
        letter = letter + i[0] #loop to take the first letter a word and combine it with the next first letter of the word 
    print "Acronym: ", letter.upper() #print the acronym in uppercase letters
elif checkNum(phrase) == True: #Error message if there was a number
    print "Oppps.. you entered a number. Please try again!"
else: #Error message is only one word was used
    print "Oppps.. Enter at least two words. Please try again!"
