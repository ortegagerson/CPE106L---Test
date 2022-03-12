"""
Author: Amiel Mir O. ordas
Filename: generator_modified.py
This program can read and take the words that are inside text files named nouns.txt, verbs.txt, articles.txt, and prepositions.txt. 
The words that are taken will be used to generate and to display sentences using a simple grammar
and vocabulary.  Words are chosen at random.
"""

import random

def getWords(file_name): #This function reads the file and insert the words to a list then converts that list into a tuple then returns that tuple
    file = open(file_name, "r") #Opens the file and set it at read mode
    wordsList = [] #Initializing a list
    wordTuple = () #Initializing a tuple
    readFile = file.readlines() #Reading the lines of the file and putting it in this readFile list
    for word in readFile: #A for loop that iterates through the readFile list
        if (word != "\n"): #This checks if the word is equal to next line
            wordsList.append(word.strip()) #If its not equal to next line, it strips or removes the next line ("\n") and puts it in the wordsList list
    wordTuple = tuple(wordsList) #After the for loop, the wordsList list will be converted to a tuple named wordTuple
    return wordTuple #It will then return the Tuple

articles = getWords("articles.txt.txt") #Calling the function getWords and also passing a string named "articles.txt.txt" to the function then initializing it to the tuple named articles
nouns = getWords("nouns.txt.txt") #Calling the function and also passing a string named "nouns.txt.txt" to the function then initializing it to the tuple named nouns
verbs = getWords("verbs.txt.txt") #Calling the function getWords and also passing a string named "verbs.txt.txt" then initializing it to the tuple verbs
prepositions = getWords("prepositions.txt.txt") #Calling the function getWordsand also passing a string named "prepositions.txt.txt" then initializing it to the tuple prepositions

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())
    
# The entry point for program execution
if __name__ == "__main__":
    main()


