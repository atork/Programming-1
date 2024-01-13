import random

user_action = input("Enter a choice (rock, paper, scissors): ")
i = random.randint(1,3)
match i:
    case 1:
        print("you won")
    case 2:
        print("you lost")
    case 3:
        print("its a tie")


user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
if user_action == computer_action:
    print("both players selected"+user_action+" its a tie")
elif user_action == "rock" and computer_action == "scissors":
    print("computer lost")
elif user_action =="rock" and computer_action =="paper":
    print("player lost")
elif user_action == "paper" and computer_action == "rock":
    print("player won")
elif user_action == "paper" and computer_action == "scissors":
    print("computer won")
elif user_action == "scissors" and  computer_action == "paper":
    print("computer lost")
elif user_action == "scissors" and computer_action == "rock":
    print("player lost")