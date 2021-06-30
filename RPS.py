#Rock Paper Scissor game uisng python

print(' WELCOME TO THE GAME '.center(30,'*'))
if input('Are you ready (y/n): ').lower()=='n' :
    quit('\nTHANK YOU ')
else:
    p,c=0,0
    for i in range(int(input('Total many how round you want to play : '))) :
        print('\n')
        person=int(input("1-Rock\n2-Paper\n3-Scissor\n(1/2/3)Enter your choice : "))
        if person>3 or person<1 :
            print('Wrong Input')
            continue
        computer=__import__('random').randrange(1,4,1)
        if computer==1:
            print('Computer : Rock')
            if computer==person :
                print('Tie')
            elif person==2:
                print('You scores ')
                p+=1
            elif person==3:
                print('Computer scores ')
                c+=1
        elif computer==2:
            print('Computer : Paper')
            if computer==person :
                print('Tie')
            elif person==1:
                print('Computer scores ')
                c+=1
            elif person==3:
                print('You scores ')
                p+=1
        elif computer==3:
            print('Computer : Scissor')
            if computer==person :
                print('Tie')
            elif person==1:
                print('You scores ')
                p+=1
            elif person==2:
                print('Computer scores ')
                c+=1
    print(f'\nSCORE\nYou : {p} \t Computer : {c}')
    if p>c :
        print(' YOU WIN '.center(30,'*'))
    elif p<c:
        print(' YOU LOSE '.center(30,'*'))
    elif p==c :
        print(' TIE '.center(30,'*'))
    print('\nTHANK YOU')
