# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:28:46 2019

@author: astro
"""

from Practice30 import pickWD


def guessLetter(Word,P,gsSet,j):
    a=0
    while a==0:
        gs=input('Guess a letter: ')
        GS=gs.upper()
        if GS in gsSet:
            print("you have guessed that before..")
        else: 
            a=1
            gsSet.add(GS)
    
    for i in range(len(Word)):
        if Word[i]==GS:
           P[i]=GS
    k=sum([1 for i in range(len(Word)) if Word[i]== GS])
   
    if k==0:
        j=j+1
        print("Incorrect, you have " + str(7-j) + " worong guesses left")
    else:
        print(' '.join(P))
    
    return(P,gsSet,j)
  

if __name__=="__main__" :
   print("Lets play hang man... 7 wrong guesses...")
   WD= pickWD()
   Progress="_"*len(WD)
   Progress = list(Progress)
   print(' '.join(Progress))
   WD= list(WD) 
   gsSet=set()   
   j=0
   while WD!=Progress and j<7:
       Progress, gsSet,j = guessLetter(WD,Progress, gsSet,j)    
   if WD==Progress:
       print("winner! you had " + str(7-j) + " guesses left")
   else:
       print("Swinging from a tree...")
       print(' '.join(WD))



   
   
   