import random


wins = 0
losses = 0
draws = 0

while True:

    user_choice = input("Choose rock, paper, or scissors: ")

    computer_choice = random.choice(["rock", "paper", "scissors"])

    if user_choice == "quit":
        print("Later!")
        break
    elif user_choice == computer_choice:
        draws += 1
        print(f"Computer picked {computer_choice}.")
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            wins += 1
            print(f"Computer picked {computer_choice}.")
            print("You won!")
        else:
            losses += 1
            print(f"Computer picked {computer_choice}.")
            print("You lost.")
    elif user_choice == "paper":
        if computer_choice == "rock":
            wins += 1
            print(f"Computer picked {computer_choice}.")
            print("You won!")
        else:
            losses += 1
            print(f"Computer picked {computer_choice}.")
            print("You lost.")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            wins += 1
            print(f"Computer picked {computer_choice}.")
            print("You won!")
        else:
            losses += 1
            print(f"Computer picked {computer_choice}.")
            print("You lost.")
    else:
        print("Invalid input! Enter rock, paper, or scissors.")

    print(f"Wins: {wins}, losses: {losses}, draws: {draws}")