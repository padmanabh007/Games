#Rock Paper Scissor game uisng python simplified

print(' WELCOME TO THE GAME '.center(30,'*'))
if input('Are you ready (y/n): ').lower()=='n' :
    quit('\nTHANK YOU ')
else:
    l=['Rock','Paper','Scissors'] #List options of ROCK PAPAER SCISSOR
    p,c=0,0
    for i in range(int(input('Total many how round you want to play : '))) :
        print('\n')
        n=int(input("1-Rock\n2-Paper\n3-Scissors\n(1/2/3)Enter your choice : "))
        if n>3 or n<1 :
            print('Wrong Input missed one chance')
            continue
        person=l[n-1]
        computer=__import__('random').choice(l)
        print('Computer : ',computer)
        if computer == person :
            print('Tie')
        elif (computer == 'Rock' and person == 'Scissors' )or(computer == 'Paper' and person == 'Rock' )or(computer == 'Scissors' and person == 'Paper' ):
            print('Computer scores')
            c+=1
        elif (person == 'Rock' and computer == 'Scissors' )or(person == 'Paper' and computer == 'Rock' )or(person == 'Scissors' and computer == 'Paper' ):
            print('You Scores')
            p+=1

    print(f'\nSCORE\nYou : {p} \t Computer : {c}')
    if p>c :
        print(' YOU WIN '.center(30,'*'))
    elif p<c:
        print(' YOU LOSE '.center(30,'*'))
    elif p==c :
        print(' TIE '.center(30,'*'))
    print('\nTHANK YOU')
