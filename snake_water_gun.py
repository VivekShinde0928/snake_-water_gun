print('***Snake Water Gun***\n')

import random

total=0
c=0
p=0
t=0
while True:
    total = total + 1
    mylist = ['s', 'w', 'g']
    a = random.choice(mylist)

    b=input("\nEnter 's' or 'w' or 'g': ")
    if b=='s' and a=='s':
        t=t+1
        print("oops ! Tie-->computer has 's'")
        #break
    elif b=='w' and a=='s':
        c=c+1
        print("computer won---> 'snake drink water'-->computer has 's'")
        #break
    elif b=='g' and a=='s':
        p=p+1
        print("player won---> 'gun killed snake'-->computer has 's'")
        #break
    elif b=='s' and a=='w':
        p=p+1
        print("player won---> 'snake drink water'-->computer has 'w'")
        #break
    elif b=='w' and a=='w':
        t=t+1
        print("opps ! Tie-->computer has 'w'")
        #break
    elif b=='g' and a=='w':
        c=c+1
        print("computer won---> 'gun dropped in water'-->computer has 'w'")
        #break
    elif b=='s' and a=='g':
        c=c+1
        print("computer won---> 'gun killed snake'-->computer has 'g'")
        #break
    elif b=='w' and a=='g':
        p=p+1
        print("player won---> 'gun dropped in water'-->computer has 'g'")
        #break
    elif b=='g' and a=='g':
        t=t+1
        print("oops ! Tie-->computer has 'g'")
        #break
    else:
        print("Try agan!!! you entered wrong input")
        total = 0
        c = 0
        p = 0
        t = 0
        #break
    if total==5:
        print(f"\n *** Comp Won-{c}, Player Won-{p}, Tie-{t} ***")
        e=input("\nplay again? Enter 'y' or 'n' :")
        if e=='y':
            total = 0
            c = 0
            p = 0
            t = 0
        else:
          break




