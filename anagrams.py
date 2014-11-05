#!/usr/bin/python
import sys
def isAnagramOf(attempt, original):
    # all the same case 
    attempt = attempt.strip()
    if len(attempt) < 1: # only actual words 
        return False
    attempt, original = attempt.lower(), original.lower()
    for character in attempt:
        position = original.find(character)
        if (position == -1):
            return False
        original = original.replace(character, '', 1)
    return True
 
def getAnagramsFor(text):
    anagrams = []
    wordlist = open("wordlist.txt", 'r')
    for line in wordlist:
        line = line.strip("\n") #strip the carriage return 
        if isAnagramOf(line, text):
            anagrams.append(line)
    return anagrams
 
matching_anagrams = getAnagramsFor(sys.argv[1])
#print(len(matching_anagrams), "total anagrams generated")
for ana in matching_anagrams:
    print(ana)
