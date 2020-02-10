import random
continue_game = True
while continue_game!=False:
    num = random.randint(1,10)
    guess = None
    while guess != num:
        guess = int(input("Guess a number between 1 and 10   "))  
        if guess==num:
            print("YOU WONNN")
            break
        else:
            if guess<num:
                print("TOO LOW")
            else:
                print("TOO HIGH")

    check = input("Do you want to keep playing? Y/N   ")    
    if check=="Y" or check=="y":
        continue_game=True
    else:
         continue_game=False
    
