lis=[]
for i in range(1,3):
    num = random.randint(a, b)
    print(f"Player {i}:")
    guess=int(input(f"guess the number between {a} and {b}"))
    chance =1
    while(chance):
        if(guess == num):
            print(f"correct guess !! you took {chance} chances to guess it.")
            lis.append(chance)
            break
        elif(guess < num):
            print(f"please guess a larger no than {guess}")
            guess= int(input())
        elif(guess > num):
            print(f"please guess a smaller no than {guess}")
            guess= int(input())
        chance=chance+1

if(lis[0]<lis[1]):
    print(f"player 1 wins as she took less chances")
else:
    print(f"player 2 wins as she took less chances")
