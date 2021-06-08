# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 12:38:11 2020

@author: bella
"""

import pandas as pd
import random

file = "thucunimorphs.txt"
data = pd.read_csv(file, sep='\t', skiprows=2, names=list('abcdefghijkl'))

givenAnswer = ""

while (givenAnswer != 'Quit'): 
    while True:
        randidx = random.randint(0, 166527)
        untrimmed = data.iloc[randidx]['i']
        
        if (type(untrimmed) == float):
            continue
        
        wordlist = untrimmed.split()
        pos = wordlist[0][4:6]

        if (pos == 'N' and len(wordlist) == 5):
            gender = wordlist[-3]
            case = wordlist[-2]
            number = wordlist[-1]
            break
        elif ((pos == 'V' or pos == 'P') and len(wordlist) == 7):
            tense = wordlist[-5]
            mood = wordlist[-4]
            voice = wordlist[-3]
            person = wordlist[-2]
            number = wordlist[-1]
            form = data.iloc[randidx]['e']
            break

    #print(wordlist)
    randquest = random.randint(2,3)
    if (randquest == 1):
        if (pos == 'N'):
            print("What gender is " + data.iloc[randidx]['e'] + "? (Lemma: " + data.iloc[randidx]['f'] + ")")
            print("Input 'Quit' to exit. Otherwise, input 'A', 'B', or 'C'.")
            print("A. " + "masculine")
            print("B. " + "feminine")
            print("C. " + "neuter")
    
            givenAnswer = input("Input: ")
            if (givenAnswer == 'A'):
                if (gender == 'masc'):
                    print("Correct!")
                else:
                    print("Incorrect. The answer is " + gender + ".")
            elif (givenAnswer == 'B'):
                if (gender == 'fem'):
                    print("Correct!")
                else:
                    print("Incorrect. The answer is " + gender + ".")
            elif (givenAnswer == 'C'):
                if (gender == 'neut'):
                    print("Correct!")
                else:
                    print("Incorrect. The answer is " + gender + ".")
            elif (givenAnswer == 'Quit'):
                break
        
    elif (randquest == 2):
        if (pos == 'N'):
            print("What case is " + data.iloc[randidx]['e'] + "? (Lemma: " + data.iloc[randidx]['f'] + ")")
            print("Input 'Quit' to exit. Otherwise, input 'A', 'B', or 'C'.")
            print("A. " + "nominative")
            print("B. " + "genitive")
            print("C. " + "dative")
            print("D. " + "accusative")
            print("E. " + "vocative")
    
            givenAnswer = input("Input: ")
            if (givenAnswer == 'A'):
                if (case == 'nom'):
                    print("Correct!")
                else:
                    print("Incorrect. The answer is " + case + ".")
            elif (givenAnswer == 'B'):
                if (case == 'gen'):
                    print("Correct!")
                else:
                    print("Incorrect. The answer is " + case + ".")
            elif (givenAnswer == 'C'):
                if (case == 'dat'):
                    print("Correct!")
                else:
                    print("Incorrect. The answer is " + case + ".")
            elif (givenAnswer == 'D'):
                if (case == 'acc'):
                    print("Correct!")
                else:
                    print("Incorrect. The answer is " + case + ".")
            elif (givenAnswer == 'E'):
                if (case == 'voc'):
                    print("Correct!")
                else:
                    print("Incorrect. The answer is " + case + ".")
            elif (givenAnswer == 'Quit'):
                break
        
    elif (randquest == 3):
        if (pos == 'N'):
            print("What number is " + data.iloc[randidx]['e'] + "? (Lemma: " + data.iloc[randidx]['f'] + ")")
            print("Input 'Quit' to exit. Otherwise, input 'A', 'B', or 'C'.")
            print("A. " + "singular")
            print("B. " + "plural")
            print("C. " + "dative")
    
            givenAnswer = input("Input: ")
            if (givenAnswer == 'A'):
                if (number == 'sg'):
                    print("Correct!")
                else:
                    print("Incorrect. The answer is " + number + ".")
            elif (givenAnswer == 'B'):
                if (number == 'pl'):
                    print("Correct!")
                else:
                    print("Incorrect. The answer is " + number + ".")
            elif (givenAnswer == 'Quit'):
                break
                
                
