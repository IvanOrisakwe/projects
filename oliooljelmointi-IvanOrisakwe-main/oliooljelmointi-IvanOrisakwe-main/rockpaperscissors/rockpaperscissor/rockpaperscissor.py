import random
while True: 
    x = input("Enter your choice (rock, paper, scissors): ").lower() 
    action = ["rock", "paper", "scissors"]
    if x not in action:
        print("Invalid choice. Choose rock paper or scissors.")
        continue

    else:
        y  = random.choice(action)
    
    if x == y:
        print("It's a tie!")
    elif (x == "rock" and y == "scissors") or (x == "paper" and y == "rock") or (x == "scissors" and y == "paper"):
        print("You win!")
    else:
        print("You lose!")
        
    print("Computer chose:", y)
    print("You chose:", x)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'no':
        print("Thanks for playing!")
        break