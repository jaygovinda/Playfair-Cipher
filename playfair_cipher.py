# PLAYFAIR CIPHER USED IN WORLD WAR I
from random import *
import math
play=[['L','G','D','B','A'],['Q','M','H','E','C'],['U','R','N',chr(randint(73,74)),'F'],['X','V','S','O','K'],['Z','Y','W','T','P']]
def find(c):
    for sublist in play:
        if c in sublist:
           return (play.index(sublist),sublist.index(c))
def playfair(s):
    cipher=""
    if len(s)%2==1:
        if s[-1]!='X':
            s+='X'
        else:
            s+='Y'
    for i in range(int(len(s)/2)):
        if find(s[2*i])[0]==find(s[2*i+1])[0]: #Same row
            for j in range(2):
                cipher+=play[find(s[2*i+j])[0]][(find(s[2*i+j])[1]+1)%5]
        elif find(s[2*i])[1]==find(s[2*i+1])[1]: #Same column
            for j in range(2):
                cipher+=play[(find(s[2*i+j])[0]+1)%5][find(s[2*i+j])[1]]
        else: #Diff row and column
            for j in range(2):
                f=int(j+math.pow(-1,j))
                cipher+=play[find(s[2*i+j])[0]][find(s[2*i+f])[1]]
    return cipher
t=int(input("Enter no.of test cases\n"))
while t>0:
    s=input("Enter the Plain Text\n")
    s=s.upper()
    print("Cipher text: "+playfair(s))
    t=t-1
