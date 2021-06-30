#Hangman Game Using Python

from random import *

Score=0
def Game(c) :
    global Score
    cl=list(c.strip())
    for i in range(0,len(cl)//2) :
        cl[randrange(1,len(cl),1)]='_'
    st=''.join(cl)
    for k in range(3) :
        print('\n'+f'Have {3-k} attempts remaining')
        person=input(f'{st} :').split()
        if st.count('_') != len(person) :
            print('You can enter words should be equal to the blank space')
            continue
        s,j='',0
        for i in range(len(st)):
            if st[i]=='_' :
                s=s+person[j].upper()
                j+=1
            else :
                s=s+st[i].upper()
        print(s)
        if s==c.rstrip().upper() :
            print('Got it')
            Score+=1
            break
    else :
        print(f'You failed to find that word and the word is {c.upper()}')


if __name__=='__main__':
    print('\n')
    print(' WELCOME TO THE HANGMAN GAME '.center(100,'*'))
    if input('\nAre you ready to play (y/n) : ').lower()!= 'y' :
        quit('\n'+' Thank You '.center(100,'*'))
    else :
        f=open('Words.txt') #Path of the Words.txt of 
        l=[]
        for i in f :
            if len(i)>2 :
                l.append(i)
    print('\n(You have only 3 attempt to guess and should be entered in a<space>b format eg._n_:a d)')
    ml=[]
    n=int(input('\nHow many words you want to try : '))
    for t in range(n) :
        c=choices(l)
        if c not in ml :
            ml.append(*c)
            Game(*c)
        else :
            t-=1
    print(f'You have got {Score} words correct out of {n}')
    print('\n'+' THANK YOU '.center(100,'*'))
