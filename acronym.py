#Program creates an acronym for two or more words. 

def any(iterable): #the any function is not bulit in this verison of python (2.4.4). 
    for element in iterable: #I went to the python library (http://docs.python.org/2.7/library/functions.html#any) and found the code to manually import the any function
        if element:
            return True
    return False


def checkNum(x): #function to check if any single character is a digit
    return any(character.isdigit() for character in x)


phrase = raw_input("Make an acronym with 2 or more words!\n")
if checkNum(phrase) == False and " " in phrase: # check for number and space (verify at least 2 words)
    brkPhrase = phrase.split() #Break the phrase into individual words
    letter = " " 
    for i in brkPhrase:
        letter = letter + i[0] #loop to take the first letter a word and combine it with the next first letter of the word 
    print "Acronym: ", letter.upper() 
elif checkNum(phrase) == True: #Error for number
    print "Oppps.. you entered a number. Please try again!"
else: #Error message is only one word was used
    print "Oppps.. Enter at least two words. Please try again!"
