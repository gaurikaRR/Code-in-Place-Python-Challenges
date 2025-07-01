#The ancient game of Nimm
stones=20
TurnCounter=4
while stones>0:
    print("There are",stones,"stones left.")
    taken1=int(input("Player 1 would you like to remove 1 or 2 stones? "))
    if taken1>2:
        a=int(input("Please enter 1 or 2: "))
        taken1=a
    stones=stones-taken1
    TurnCounter=TurnCounter+1
    #Additionally the above makes sure that no player takes more than 2 stones with each turn
    print(" ")
    print("There are",stones,"stones left.")
    taken2=int(input("Player 2 would you like to remove 1 or 2 stones?"))
    if taken2>2:
        b = int(input("Please enter 1 or 2: "))
        taken2=b
    stones=stones-taken2
    TurnCounter=TurnCounter-1
    print(" ")
    #The above chunk of code helps switch player by switching variable TurnCounter
    if stones==1:
        if TurnCounter==5:
            print("There are", stones, "stones left.")
            taken1 = int(input("Player 2 would you like to remove 1 or 2 stones? "))
            if taken1!=1:
                a = int(input("Please enter 1: "))
                taken1 = a
            stones = stones - taken1
            print(" ")
            print("Player 1 wins!")
    if stones==1:
        if TurnCounter==4:
            print("There are", stones, "stones left.")
            taken1 = int(input("Player 1 would you like to remove 1 or 2 stones? "))
            if taken1!=1:
                a = int(input("Please enter 1: "))
                taken1 = a
            stones = stones - taken1
            print(" ")
            print("Player 2 wins!")
    #The above blocks function when the only 1 stone remains.
    #It also makes sure that if a certain player takes the last stone,
    #then the player right before is the winner

