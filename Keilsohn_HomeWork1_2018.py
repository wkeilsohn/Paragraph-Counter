# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 08:56:23 2018

@author: William Keilsohn
"""

#Collects user input for a paragraph
parag = input("Please provide a paragraph or section of text:")

#Define a function to split the paragraph into parts


per = "." #Could not actually find this online. Just gonna role with it.


def spliter(string):
    sentenceList = []
    sentenceList = string.split(per) #https://www.geeksforgeeks.org/python-string-split/ (The 'split' function)
    sentenceList.pop(len(sentenceList)-1) #Removes the extra empty string.
    return sentenceList
#print(spliter(parag)) # Tests for correct output. 

sentenceArray = spliter(parag) #Define a variabel for use later.

#Count the number of sentences

def senCount(lis):
    totalSen = len(lis)
    print("\n There are " + str(totalSen) + " sentences in the provided paragraph.")
    return totalSen
'''
The last "sentence" is a blank string. This causes the problem of increasing the list, and 
thus the count on the number of sentences by one. This can either be fixed by removing it
when I define the list (what I choose to do for convience sake) or here when I look to count
the number of sentences (less efficient).
'''
senCount(sentenceArray) #Answers the first question.

#Count the total number of words in the paragraph

def wordCount(string):
    wordList = []
    wordList = string.split()
    totalWord = len(wordList)
    return totalWord

totalWords = wordCount(parag)
#Answers the question.
print("\n There are a total of " + str(totalWords) + " words in the paragraph.")

#Print out the sentence with the most words

def senLong(lis):
    maxLength = 0
    longArray = []
    sentenceLong = ""
    for i in lis:
        if wordCount(i) > maxLength: #checks the length of the word, and if long enough, replaces the previos longest word. 
            maxLength = wordCount(i)
            sentenceLong = i
        elif wordCount(i) == maxLength: #Also handels strings/words of equal length
            longArray.append(i)                
    longArray.append(sentenceLong) #Creates a list of the longest words.
    for x in longArray: #prints a list of the longest words. 
        print("\n" + str(longArray.index(x) + 1) + ": " + x) #As this could produce a 'list' rather than just one value, I want to number the sentences and make them easier to read. 

print("\n The longest sentence(s) in the paragraph is/are:")
senLong(sentenceArray) #Answers the question

#Print out the sentence with the fewest words. 

def senShort(lis):
    minLength = 13955 #http://www.openculture.com/2014/07/5-very-long-literary-sentences.html (Longest sentence on record)
    shortArray = []
    sentenceShort = ""
    for i in lis:
        if wordCount(i) < minLength:
            minLength = wordCount(i)
            shortArray =[]
            sentenceShort = i
        elif wordCount(i) == minLength:
            shortArray.append(i)
    shortArray.append(sentenceShort)
    for x in shortArray:
        print("\n" + str(shortArray.index(x) + 1) + ": " + x)

print("\n The shortest sentence(s) in the paragraph is/are:")
senShort(sentenceArray) #Answers the question

#Sort the words in the list and print out the sorted words

def wordSort(lis):
    wordList = []
    combinedList = []
    for i in lis: #Seperates out each word an forms a long list of words.
        wordList = i.split()
        combinedList = combinedList + wordList # Places them back into one long list
    combinedList.sort(key = str.lower) #https://www.programiz.com/python-programming/methods/list/sort  (The 'sort' function)
    return combinedList #returns a long list, sorted as if it was all lower case

sortedList = wordSort(sentenceArray)# Provides only a sorted list

#I don't particularly like repeated/duplicated words so I'm gonna remove them.
#print(sortedList) #If you don't mind the repeated words, this should provide them all. Otherwise I prefer the below function.

def cleanList(lis):
    cleanLis = []
    a = 0
    for i in lis:
        if i not in cleanLis: #https://stackoverflow.com/questions/10406130/check-if-something-is-not-in-a-list-in-python (The 'not in' condition)
            cleanLis.append(i) #Note: This doesn't account for capital vs. lowecase duplicates
    while a < (len(cleanLis) - 1): #Want a while loop here to avoid going off the end of the list.
        if cleanLis[a] == str.lower(cleanLis[a + 1]): #Because the uppercase value always comes second in the list.
            cleanLis.remove(cleanLis[a]) #There should only be one possible duplicate so just take it out. Also, might as well leave in the capital.
        a += 1
    for x in cleanLis:
        print("\n" + str(cleanLis.index(x) + 1) + ": " + x) #As above I want to make the output easier to read by numbering the print-outs.

print("\n The sorted words are as follows:")
cleanList(sortedList) #Answers question

'''
From what I can tell, python thinks that any group of text surrounded by spaces 
or which simply has nothing after it (i.e. the end of the paragraph) is a word. It doesn't actually have a dictionay
it pulls words from, nor appear to have the ability to spell check. This seems to include numbers and symbols aswell.
I am basing this answer off of my testing with Lorem ipsum: https://loremipsum.io/
'''