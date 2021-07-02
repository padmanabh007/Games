from numpy import *
from random import *

def check(arr):
    for i in arr :
        if count_nonzero(i == 'x')==3 :
            quit('\nYou Win\n'+'THANK YOU'.center(100,'*'))
        elif count_nonzero(i == 'o')==3 :
            quit('\nYou Lose\n'+'THANK YOU'.center(100,'*'))
    
    trap=arr.transpose()
    for i in trap :
        if count_nonzero(i == 'x')==3 :
            quit('\nYou Win\n'+'THANK YOU'.center(100,'*'))
        elif count_nonzero(i == 'o')==3 :
            quit('\nYou Lose\n'+'THANK YOU'.center(100,'*'))
    
    majordigonal=diag(arr)
    if count_nonzero(majordigonal == 'x')==3 :
        quit('\nYou Win\n'+'THANK YOU'.center(100,'*'))
    elif count_nonzero(majordigonal == 'o')==3 :
        quit('\nYou Lose\n'+'THANK YOU'.center(100,'*'))

    r=[]
    for i in arr :
        r.append(i[::-1])
    arr2=array(r)

    minordigonal=diag(arr2)
    if count_nonzero(minordigonal  == 'x')==3 :
        quit('\nYou Win\n'+'THANK YOU'.center(100,'*'))
    elif count_nonzero(minordigonal  == 'o')==3:
        quit('\nYou Lose\n'+'THANK YOU'.center(100,'*'))

def printboard(arr):
    print('\n')
    j=1
    for i in arr: 
        p=' | '.join(i)
        print(p.center(100))
        if j!=3:
            print(('---'*3).center(100))
        j+=1

if __name__ == '__main__':
    print('\n'+' WELCOME TO TIC-TAC-TOE GAME '.center(100,'*'))
    arr=array([[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']])
    printboard(arr)
    d={'1':'00','2':'01','3':'02','4':'10','5':'11','6':'12','7':'20','8':'21','9':'22'}
    cl=[]
    while ' ' in arr :
        ch=input('\nEnter the position : ')
        if ch not in  d.keys() :
            print('Wrong space ! Select another space')
            continue
        choice=list(map(int,d[ch].strip()))
        if choice in cl :
            print('Wrong space ! Select another space')
            continue
        cl.append(choice)
        arr[choice[0]][choice[1]]='x'
        printboard(arr)
        check(arr)
        while True and ' ' in arr:
            r,c=randrange(0,3,1),randrange(0,3,1)
            if [r,c] not in cl :
                break 
        cl.append([r,c])
        arr[r][c]='o'
        printboard(arr)
        check(arr)
    print('\nTIE\n'+' THANK YOU '.center(100,'*'))

