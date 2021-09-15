def guessing_game(max):
    count=1
    import random
    n=random.randint(1,max)
    print('Guess a number between 1 and 100')
    x=int(input())
    
    while x!=n:
        if(x<n):
            print('Higher!')
        elif(x>n):
            print('Lower!')
        x=int(input())
        count+=1
    print('Correct!, You took ', count, ' guess.') 