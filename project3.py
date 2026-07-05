import random

choices = ["stone", "paper", "scissor"]

computer = random.choice(choices)
user = input("Enter Stone, Paper, or Scissor: ").lower()

if user not in choices:
    print("Invalid Choice!")
elif user == computer:
    print("It's a Draw!")
elif (user == "stone" and computer == "scissor") or \
     (user == "paper" and computer == "stone") or \
     (user == "scissor" and computer == "paper"):
    print("You Win!")
else:
    print("Computer Wins!")

print("Your Choice:", user)
print("Computer Choice:", computer)
